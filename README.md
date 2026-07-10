# FastAPI

FastAPI is a modern, high-performance Python web framework for building APIs quickly and efficiently.

## FastAPI Features

- **Fast** — One of the fastest Python frameworks available, on par with NodeJS and Go
- **Easy** — Designed to be simple to use and learn
- **Automatic Docs** — Generates interactive API documentation automatically at `/docs`
- **Type Safe** — Built on Python type hints for cleaner, more reliable code

## Requirements

- Python 3.7+
- fastapi
- uvicorn

## Installation

```bash
pip install fastapi uvicornbuild, deploy, and launch
```

## Quick Start

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

## Run the Server

```bash
uvicorn main:app --reload
```

Then open your browser at `http://127.0.0.1:8000`

## Auto-Generated Docs

| URL | Description |
|-----|-------------|
| `/docs` | Interactive Swagger UI |
| `/redoc` | ReDoc documentation |


