# arduino-disco

A tool to discover Arduino boards connected via serial ports.

## Installation

```bash
pip install .
```

## Usage

```bash
arduino-disco
```

## Development

To bump the version:

```bash
pip install -e .[dev]
bumpver update --patch
```

To set up pre-commit hooks:

```bash
pip install -e .[dev]
pre-commit install
```
