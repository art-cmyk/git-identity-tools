import os
import argparse
import subprocess
from git_identity_tools.identities import load_identities, get_identity
from git_identity_tools.path_utils import get_org_and_enterprise


def find_git_repos(base_path):
    for root, dirs, files in os.walk(base_path):
        if ".git" in dirs:
            yield root


def apply_git_identity(repo, name, email, dry_run):
    if dry_run:
        print(f"[DRY-RUN] Would set identity in {repo} to {name} <{email}>")
    else:
        subprocess.run(["git", "-C", repo, "config", "user.name", name])
        subprocess.run(["git", "-C", repo, "config", "user.email", email])
        print(f"✅ Set identity in {repo} to {name} <{email}>")


def main():
    parser = argparse.ArgumentParser(description="Sync Git identities based on repo org/enterprise structure.")
    parser.add_argument("--base", default=os.path.expanduser("~/source"), help="Base directory to scan")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying them")
    parser.add_argument("--org", help="Only sync repos under this org")
    parser.add_argument("--enterprise", help="Only sync repos under this enterprise")
    parser.add_argument("--config", help="Path to identities.conf")

    args = parser.parse_args()
    config = load_identities(args.config)

    for repo in find_git_repos(args.base):
        org, enterprise = get_org_and_enterprise(repo, args.base)

        if args.org and args.org != org:
            continue
        if args.enterprise and args.enterprise != enterprise:
            continue

        name, email = get_identity(config, org, enterprise)
        if name and email:
            apply_git_identity(repo, name, email, args.dry_run)
        else:
            print(f"⚠️  No identity found for org='{org}' (enterprise='{enterprise}') in {repo}")
