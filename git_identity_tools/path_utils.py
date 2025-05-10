import os


def get_org_and_enterprise(repo_path, base_path):
    """
    Infer org and enterprise from repo path relative to base.

    Rules:
    - <base>/<org> ➝ org=enterprise=<org>
    - <base>/<org>/<repo> ➝ org=enterprise=<org>
    - <base>/<enterprise>/<org>/<repo> ➝ exact
    """
    if os.path.abspath(repo_path) == os.path.abspath(base_path):
        return None, None

    parts = os.path.relpath(repo_path, base_path).split(os.sep)

    if len(parts) == 1:
        org = enterprise = parts[0]
    elif len(parts) == 2:
        org = enterprise = parts[0]
    elif len(parts) >= 3:
        enterprise = parts[0]
        org = parts[1]
    else:
        org = enterprise = None

    return org, enterprise