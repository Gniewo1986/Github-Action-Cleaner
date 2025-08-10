# scripts/delete_all_workflow_runs.py
#
# Deletes all workflow runs in the current repository except the current run.
# Authenticates using the GITHUB_TOKEN environment variable.
# Prints informative output for each action, matching the original JS script's logging.

import os
import sys
import requests

# Get GitHub token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set.")
    sys.exit(1)

# Get repository info from environment variables set by GitHub Actions
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_RUN_ID = os.getenv("GITHUB_RUN_ID")

if not GITHUB_REPOSITORY or not GITHUB_RUN_ID:
    print("Error: GITHUB_REPOSITORY or GITHUB_RUN_ID environment variable not set.")
    sys.exit(1)

owner, repo = GITHUB_REPOSITORY.split("/")

# GitHub API base URL
API_BASE = "https://api.github.com"

# Set up headers for authentication
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "User-Agent": "delete-all-workflow-runs-script"
}

page = 1
deleted = 0

while True:
    # List workflow runs for the repository (paginated)
    url = f"{API_BASE}/repos/{owner}/{repo}/actions/runs"
    params = {
        "per_page": 100,
        "page": page
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error fetching workflow runs: {response.status_code} {response.text}")
        sys.exit(1)
    runs = response.json().get("workflow_runs", [])
    if not runs:
        break
    for run in runs:
        run_id = str(run["id"])
        if run_id == str(GITHUB_RUN_ID):
            print(f"Skipping current run id={run['id']}")
            continue
        print(f"Deleting run id={run['id']}, name={run.get('name')}, status={run.get('status')}, conclusion={run.get('conclusion')}")
        del_url = f"{API_BASE}/repos/{owner}/{repo}/actions/runs/{run['id']}"
        del_resp = requests.delete(del_url, headers=headers)
        if del_resp.status_code == 204:
            deleted += 1
        else:
            print(f"  Failed to delete run id={run['id']}: {del_resp.status_code} {del_resp.text}")
    page += 1

if deleted == 0:
    print("No workflow runs found to delete (except current run).")
else:
    print(f"Deleted {deleted} workflow runs (except current run).")