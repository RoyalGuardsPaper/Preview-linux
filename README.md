# Preview

Preview is a Linux desktop application for viewing images and PDF documents. It
is an early starter project: the current version opens a basic application
window, and document viewing features are planned next.

Version: 0.1.0  
Initial development and packaging target: Fedora and Fedora-based distributions.

## Current status

- Basic PySide6 application window
- Python package and `preview` launch command
- Development setup, test, and build commands
- Basic startup test

Image and PDF viewing, desktop launcher integration, and file associations are
not implemented yet.

## Requirements

- Python 3.10 or newer
- `venv` support for Python
- Fedora development tools and Qt runtime libraries as needed by PySide6

PySide6 is installed as a Python dependency. Some systems may need operating
system packages for Python development headers and virtual environment support.
The exact Fedora package instructions will be added after testing on Fedora.

## Development setup

Clone the repository, enter its directory, then run:

```sh
make setup
make run
```

`make setup` creates a `.venv` virtual environment in the repository and installs
the application and development dependencies there. `make run` launches the
graphical application from that environment.

Other useful commands:

```sh
make test   # Run the automated tests
make build  # Build a wheel and source distribution in dist/
make clean  # Remove build output and test caches
```

## License

Preview is licensed under GPL-3.0-only. See [LICENSE](LICENSE) for details.
