import os
import argparse
import subprocess
from git_identity_tools.path_utils import get_org_and_enterprise


def find_git_repos(base_path):
    for root, dirs, files in os.walk(base_path):
        if ".git" in dirs:
            yield root


def get_git_identity(repo):
    try:
        name = subprocess.check_output(["git", "-C", repo, "config", "user.name"]).decode().strip()
        email = subprocess.check_output(["git", "-C", repo, "config", "user.email"]).decode().strip()
        return name, email
    except subprocess.CalledProcessError:
        return None, None


def main():
    parser = argparse.ArgumentParser(description="Show Git identity for all repos.")
    parser.add_argument("--base", default=os.path.expanduser("~/source"), help="Base directory to scan")
    parser.add_argument("--org", help="Only show repos under this org")
    parser.add_argument("--enterprise", help="Only show repos under this enterprise")

    args = parser.parse_args()

    for repo in find_git_repos(args.base):
        org, enterprise = get_org_and_enterprise(repo, args.base)

        if args.org and args.org != org:
            continue
        if args.enterprise and args.enterprise != enterprise:
            continue

        name, email = get_git_identity(repo)
        if name and email:
            print(f"{repo}: {name} <{email}>")
        else:
            print(f"{repo}: ⚠️  Git identity not set")
