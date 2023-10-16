# LineBot Playground

## Requirements

- [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/docs/#installation)
- Python 3.11

## Setup Development Environment

### Install Poetry

```shell
brew install poetry
```

### Setup Poetry

```shell
poetry env use python3.11
```

### Install Poetry Packages

```shell
poetry shell
poetry install
```

## Run

```shell
uvicorn app.main:app --reload
```

or

```shell
python -m apps
```

## CI/CD

### Github Actions

```shell
cp .github/workflows/ci.yml.template .github/workflows/ci.yml
```
- Replace `mixin_backend` with your project name.

### Helm Chart

- Replace `mixin_backend` with your project name.
- Change your ingress host in `values-{env}.yaml` file.
