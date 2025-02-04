# Python Practice Sessions

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Notebook-7.3.1-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![mypy](https://img.shields.io/badge/mypy-1.14.1-blueviolet?logo=mypy&logoColor=white)](http://mypy-lang.org/)
[![pytest](https://img.shields.io/badge/pytest-8.3.4-yellow?logo=pytest&logoColor=white)](https://pytest.org/)
[![uv](https://img.shields.io/badge/uv-0.5.21-00ADD8?logo=astral&logoColor=white)](https://docs.astral.sh/uv/)
[![PyCharm](https://img.shields.io/badge/PyCharm-2024.3.1-blue?logo=jetbrains&logoColor=white)](https://www.jetbrains.com/pycharm/)

## About the Repository

This repository is dedicated to my Python programming practice. It contains programs written in both functional and
object-oriented paradigms. I explore various techniques, including:

- Static typing (`mypy`)
- Unit testing (`pytest`)
- Working with notebooks (`Jupyter Notebook`)
- Managing dependencies using `uv`

# uv

An extremely fast Python package and project manager, written in Rust.

![uv Benchmark](https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310#only-dark)

## Highlights

- 🚀 A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.
- ⚡️ 10-100x faster than `pip`.
- 🐍 Installs and manages Python versions.
- 🛠️ Runs and installs Python applications.
- ❇️ Runs scripts, with support for inline dependency metadata.
- 🗂️ Provides comprehensive project management, with a universal lockfile.
- 🔩 Includes a `pip`-compatible interface for a performance boost with a familiar CLI.
- 🏢 Supports Cargo-style workspaces for scalable projects.
- 💾 Disk-space efficient, with a global cache for dependency deduplication.
- ⏬ Installable without Rust or Python via `curl` or `pip`.
- 🖥️ Supports macOS, Linux, and Windows.

**uv** is backed by Astral, the creators of Ruff.

## About the Repository

This repository is dedicated to my Python programming practice. It contains programs written in both functional and
object-oriented paradigms. I explore various techniques, including:

- Static typing (`mypy`)
- Unit testing (`pytest`)
- Working with notebooks (`Jupyter Notebook`)
- Managing dependencies using `uv`
- Object-Oriented Programming (OOP) concepts:
    - Classes
    - Inheritance
    - Decorators
    - Logging
    - Abstract classes
    - Exceptions
    - Context managers

## Repository Structure

- **Functional Programming**  
  Programs written following the principles of functional programming.
- **Object-Oriented Programming**  
  Projects based on object-oriented programming using classes and methods.
- **Tests and Typing**  
  Contains unit tests and code with static typing.
- **Jupyter Notebooks**  
  Interactive notebooks with experiments and analyses.

## How to Run?

1. Install `uv` (a recommended way to manage Python tools):

   ```bash
   pipx install uv
   ```

For Linux and macOS, determine your shell (e.g., with `echo $SHELL`), then run one of:

```bash
# For Bash
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

# For Zsh
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
```

To enable shell autocompletion for uvx:

For Linux and macOS, determine your shell (e.g., with `echo $SHELL`), then run one of:

```bash
# For Bash
echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc

# For Zsh
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

2. Activate `uv` for for project :

   ```bash 
   uv init
   ``` 

3. Install dependencies :

    ```bash
   uv add mypy ruff pytest --dev 
   ```
4. Active venv :

    ```bash
   source .venv/bin/activate
    ```

## 🧑‍💻 Author

Piotr Lipiński

Feel free to contribute, submit issues, or ask questions! 😊
