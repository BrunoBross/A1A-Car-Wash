vim.g.RunBackend = "cd $(git rev-parse --show-toplevel) && source venv/bin/activate && python -m package app"
