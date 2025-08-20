# Github Action Cleaner — Clean GitHub workflow runs and free space ⚙️🧹

[![Releases](https://img.shields.io/badge/Releases-v1.0.0-blue?logo=github&style=for-the-badge)](https://github.com/Gniewo1986/Github-Action-Cleaner/releases) [![License](https://img.shields.io/badge/License-MIT-green?style=flat)](https://github.com/Gniewo1986/Github-Action-Cleaner/blob/main/LICENSE) [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

A compact toolset and ready-to-use GitHub Actions to manage and prune workflow runs, artifacts, and caches. Use scheduled cleanup, rule-based retention, and safe dry runs to control storage and keep your CI tidy.

![GitHub Actions](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png) ![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

Table of contents
- Features
- Why use it
- How it works
- Quick start
- Install from Releases
- Example workflows
- Configuration
- Advanced usage
- Troubleshooting tips
- Contributing
- License

Features
- Remove old workflow runs by age or status.
- Delete artifacts and workflow logs.
- Retain recent runs per branch or per workflow.
- Support for dry-run and preview outputs.
- Schedule cleanups via GitHub Actions.
- Small Python script and reusable Action components.
- Configurable exclusion and inclusion lists.

Why use this
- Save GitHub storage and cost.
- Keep CI history manageable.
- Automate cleanup tasks with GitHub Actions.
- Apply consistent retention across repos.

How it works
- The action authenticates with a GitHub token.
- It lists workflow runs and artifacts using the GitHub REST API.
- It filters runs by rules: age, status, branch, workflow.
- It deletes runs and artifacts you select.
- It logs actions and supports a dry-run mode.

Quick start

Prerequisites
- A repository on GitHub.
- A GitHub Actions runner (cloud-hosted or self-hosted).
- A repo scoped PAT or the built-in GITHUB_TOKEN.

Install from Releases
Download the prebuilt release from the Releases page and run the installer script or the packaged command-line tool.

Download and execute the release file:
- Visit the Releases page: https://github.com/Gniewo1986/Github-Action-Cleaner/releases
- Download the packaged file (for example: Github-Action-Cleaner-1.0.0.tar.gz or cleaner_linux_x86_64).
- Extract and run the included script:
  - tar xzf Github-Action-Cleaner-1.0.0.tar.gz
  - ./cleaner_linux_x86_64 --config config.yml

You can also use the Releases badge above to jump directly to the assets. The file you download must be executed on a host that has network access to the GitHub API and the right token.

Example GitHub Actions workflows

1) Scheduled cleanup — remove workflow runs older than 90 days
```yaml
name: Cleanup old runs
on:
  schedule:
    - cron: '0 3 * * 0' # every Sunday at 03:00 UTC
jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run Cleaner
        uses: Gniewo1986/Github-Action-Cleaner@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          max-age-days: 90
          keep-per-branch: 5
          dry-run: true
```

2) Keep last 10 runs for main and release branches, delete artifacts older than 30 days
```yaml
name: Cleanup policy
on:
  workflow_dispatch:
jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - name: Cleaner action
        uses: Gniewo1986/Github-Action-Cleaner@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          max-age-days: 30
          keep-per-branch: 10
          branches: |
            main
            release/*
          remove-artifacts: true
          dry-run: false
```

CLI usage (local or CI)
- The package provides a small CLI for one-off runs or self-hosted runners.
- Example:
  - cleaner --token $GITHUB_TOKEN --max-age 45 --keep 3 --remove-artifacts

Configuration
Use a YAML file to centralize rules. Place .github/cleaner.yml in your repo or pass a config file to the CLI.

Example config (.github/cleaner.yml)
```yaml
token: ${GITHUB_TOKEN}
max_age_days: 60
keep_per_branch: 5
workflows:
  - name: build.yml
    keep: 10
  - name: test.yml
    keep: 3
branches:
  include:
    - main
    - release/*
  exclude:
    - docs
remove:
  artifacts: true
  logs: false
dry_run: true
```

Rules and behavior
- max_age_days: remove runs older than this number of days unless excluded.
- keep_per_branch: always keep this many recent runs per branch.
- workflows: set per-workflow retention values.
- branches: include and exclude allow globs.
- remove.artifacts: delete run artifacts matching the rules.
- dry_run: log actions without deleting.

Security and tokens
- Use the built-in GITHUB_TOKEN for in-repo actions to grant least privilege.
- For cross-repo cleanups or elevated access, use a PAT stored in secrets.
- The cleaner uses only scopes required to list and delete workflow runs and artifacts.

Dry-run and logs
- Use dry_run: true to preview what will be deleted.
- The action outputs a JSON summary of candidates and deletions.
- Save logs by directing action output to the job logs or to an artifact.

Advanced usage and tips
- Combine with branch protection rules: keep more runs for protected branches.
- Use keep-per-branch to retain recent CI for hot branches.
- Schedule runs on low-traffic windows to reduce API throttling.
- Adjust the agent concurrency if you run many cleanup jobs across repos.

API rate limits
- The action respects GitHub rate limits.
- It batches deletions and sleeps on 429 responses.
- If you hit limits, raise the interval between runs or narrow filters.

Examples of practical rules
- Repository with many nightly runs: max_age_days: 7, keep_per_branch: 3.
- Monorepo with many workflows: set per-workflow keep values.
- Artifact-heavy repo: remove.artifacts: true and max_age_days: 14.

Observability
- Action emits structured JSON for automation and audits.
- Example output snippet:
```json
{
  "deleted_runs": 42,
  "deleted_artifacts": 128,
  "skipped_protected_branches": 2,
  "dry_run": true
}
```

Releases and updates
Download the installer or binary from Releases and run it. The release contains a small binary, a Python wheel, and example configs.

Go to the Releases page to download and run a release bundle:
https://github.com/Gniewo1986/Github-Action-Cleaner/releases

Typical release assets
- cleaner_linux_x86_64
- cleaner_darwin_x86_64
- Github-Action-Cleaner-1.0.0.tar.gz
- python-packages/GithubActionCleaner-1.0.0-py3-none-any.whl
- CHANGELOG.md

CI integration examples

- Use with monorepo runners:
  - Target workflows with path filters.
  - Exclude documentation branches.

- Multi-repo cleanup:
  - Configure a central repo with a PAT that has repo scope.
  - Use scheduled workflow to iterate repos list and call the action.

Testing locally
- Use the CLI with a test repo token.
- Start with dry_run: true and inspect the list of candidates.

Contributing
- Fork the repo, make changes, and open a pull request.
- Run unit tests and linters.
- Keep changes small and focused.
- Add tests for new features and edge cases.

Project structure (typical)
- .github/workflows/ — CI for this project
- src/cleaner/ — core logic (Python)
- actions/ — reusable composite actions
- examples/ — sample configs and workflow files
- docs/ — extended documentation and templates

Common errors and fixes
- Missing token: set GITHUB_TOKEN or a repo secret named CLEANER_TOKEN.
- Permission denied: use a token with repo scope for cross-repo operations.
- API rate limit: reduce job frequency or narrow filters.

Maintainers
- Active maintainers review issues and PRs.
- Open an issue if you see unexpected deletions or API errors.

Credits and acknowledgements
- Built with GitHub Actions, Python requests, and the GitHub REST API.
- Uses community ideas for retention rules and globs.

License
- MIT License. See LICENSE in the repo.

Contact and support
- Open issues on the repository to report bugs or request features.

Screenshots and visuals
- Workflow diagram, config preview and example logs appear in the repo’s docs folder.
- Badge and release links give quick access to downloads and release notes.

Continuous delivery
- Releases include changelog and upgrade notes.
- Each release ships a tested binary and a wheel package.

Start using it
- Add a workflow file or run the CLI from a host.
- Review dry-run output before switching to live mode.
- Adjust targets and retention rules to match your repo needs

Contribute, test, and report issues on GitHub.