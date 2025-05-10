#!/bin/bash

set -e

REPO_URL="https://github.com/art-cmyk/git-identity-tools.git"

echo "🔧 Checking for pipx..."
if command -v pipx >/dev/null 2>&1; then
  echo "✅ pipx found. Installing via pipx..."
  pipx install --force "git+${REPO_URL}"
else
  echo "⚠️ pipx not found. Falling back to pip install --user."
  python3 -m pip install --user --upgrade "git+${REPO_URL}"
fi

echo "🎉 Installation complete. You can now use:"
echo "    git-identity-sync"
echo "    git-identity-status"