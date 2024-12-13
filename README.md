# Torch/HF project template

GitHub project template to quickly spin up Torch/HF based ML projects for NVIDIA and Apple Silicon enabled devices.

## Dependencies

- Git
- Python >= 3.12
- Rye: `curl -sSf https://rye.astral.sh/get | bash`, with the following options
  - Run a Python installed and managed by Rye
  - Default toolchain: >= cpython@3.12
  - Add Rye to `PATH`
  - Add `source "$HOME/.rye/env` to your `~/.bashrc` or `~/.zshrc`

## Usage

1. Create a new GitHub repo and select this repo as a template
2. Modify pyproject.toml to use your own project name/version/author string
3. Run `rye sync` in the root directory
