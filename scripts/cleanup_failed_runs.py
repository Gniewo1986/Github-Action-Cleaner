# scripts/delete_failed_workflow_runs.py
#
# Deletes up to 100 most recent failed workflow runs in the current GitHub repository.
# Authenticates using a GitHub token from the GITHUB_TOKEN environment variable.
# Prints informative output for each action, matching the JS script's logging.

import os
import sys
import requests

# Get GitHub token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set.")
    sys.exit(1)

# GitHub API base URL
API_URL = "https://api.github.com"

# Get repository owner and name from environment variables set by GitHub Actions,
# or fallback to parsing from the remote URL if running locally.
REPO = os.getenv("GITHUB_REPOSITORY")
if not REPO:
    print("Error: GITHUB_REPOSITORY environment variable not set (expected format: owner/repo).")
    sys.exit(1)

owner, repo = REPO.split("/", 1)

# Set up headers for authentication
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def main():
    # Fetch up to 100 most recent completed workflow runs
    params = {
        "status": "completed",
        "per_page": 100
    }
    runs_url = f"{API_URL}/repos/{owner}/{repo}/actions/runs"
    response = requests.get(runs_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error fetching workflow runs: {response.status_code} {response.text}")
        sys.exit(1)

    runs = response.json().get("workflow_runs", [])
    # Only keep runs that actually failed
    failed_runs = [run for run in runs if run.get("conclusion") == "failure"]

    if not failed_runs:
        print("No failed workflow runs found.")
        return

    for run in failed_runs:
        run_id = run.get("id")
        run_name = run.get("name")
        print(f"Deleting failed run id={run_id}, name={run_name}")
        del_url = f"{API_URL}/repos/{owner}/{repo}/actions/runs/{run_id}"
        del_resp = requests.delete(del_url, headers=headers)
        if del_resp.status_code == 204:
            print(f"Deleted run id={run_id}")
        else:
            print(f"Failed to delete run id={run_id}: {del_resp.status_code} {del_resp.text}")

if __name__ == "__main__":
    main()