# FastAPI

FastAPI is a modern, high-performance Python web framework for building APIs quickly and efficiently.

## Why FastAPI?

- **Fast** — One of the fastest Python frameworks available, on par with NodeJS and Go
- **Easy** — Designed to be simple to use and learn
- **Automatic Docs** — Generates interactive API documentation automatically at `/docs`
- **Type Safe** — Built on Python type hints for cleaner, more reliable code

## Installation

```bash
pip install fastapi uvicorn
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

## Requirements

- Python 3.7+
- fastapi
- uvicorn
