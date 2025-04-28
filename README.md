# fastapi-template

A simple template for FastAPI

## Install dependencies

```bash
uv sync
```

```bash
# run in dev mode
uv run fastapi dev
# run in prod mode
uv run fastapi run
```

## Build docker image

```sh
docker build -t fastapi-app .
docker run -p 8000:80 fastapi-app
```
