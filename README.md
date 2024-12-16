# LogViewer

## Demo

https://disk.yandex.ru/i/wJ2lqMOT1wY2dw

## Setup project

### Install `uv`

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh  # For Linux
```

```sh
brew install uv  # For MacOS
```


### Dependencies & Virtual environment

```sh
uv sync --all-extras --dev
```


### Launch application

```sh
uv run streamlit run 1_Main.py
```
