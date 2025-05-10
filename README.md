# 🪪 git-identity-tools

**git-identity-tools** is a lightweight CLI utility to manage Git identities across your local repositories based on folder hierarchy. It lets you automatically set `user.name` and `user.email` in each repo based on which **organization** or **enterprise** the repo belongs to.

---

## ✨ Features

- ✅ Automatically applies Git identity based on folder structure  
- ✅ Supports `--dry-run`, `--org`, and `--enterprise` filters  
- ✅ Prints Git identity status across all repos  
- ✅ Cross-platform support (macOS, Linux, Windows and WSL2)  
- ✅ Uses a private config file for sensitive identity mappings  
- ✅ Installable via pipx, pip, or install script  

---

## 📁 Expected Folder Layout

    ~/source/<enterprise>/<org>/<repo>/

Example:

    ~/source/Microsoft/copilot-ai/project-x/
    ~/source/art-cmyk/my-personal-project/

---

## 🛠️ Installation

### Option 1: Using pipx (recommended)

    pipx install git+https://github.com/art-cmyk/git-identity-tools.git

### Option 2: Using pip

    pip install --user git+https://github.com/art-cmyk/git-identity-tools.git

### Option 3: One-liner with install script

    curl -sSL https://raw.githubusercontent.com/art-cmyk/git-identity-tools/main/scripts/install.sh | bash

---

## 🔧 Usage

### Sync Git Identities

    git-identity-sync                     # Apply identities to all repos
    git-identity-sync --dry-run           # Preview what would change
    git-identity-sync --org copilot-ai      # Only apply to a specific org
    git-identity-sync --enterprise Microsoft     # Only apply to a specific enterprise

### Show Git Identity Status

    git-identity-status                   # Show current Git identities
    git-identity-status --org Paycase
    git-identity-status --enterprise art-cmyk

---

## 🔐 Identities Configuration

Create a file at:

    ~/.config/git-identity-tools/identities.conf

Example:

    [org:art-cmyk]
    name = art-cmyk
    email = 14794711+art-cmyk@users.noreply.github.com

    [org:sample-org]
    name = Rama Krishna
    email = rama.krishna@vaikunttha.ai

    [enterprise:Microsoft]
    name = Rama Krishna
    email = rama.krishna@microsoft.com

> 🔒 This file is ignored via `.gitignore` so your identity mappings remain private.

---

## 🧪 Testing

To test your setup:

    git-identity-sync --dry-run
    git-identity-status

---

## 📄 License

MIT © 2025 art-cmyk
