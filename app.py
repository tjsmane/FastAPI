from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dynamic Web App</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 50px; display: flex; justify-content: center; }
            .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
            h1 { color: #333; font-size: 24px; margin-bottom: 10px; }
            p { color: #666; margin-bottom: 20px; }
            input[type="text"] { width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; font-size: 16px; }
            button { width: 100%; background-color: #007bff; color: white; padding: 12px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; transition: background-color 0.3s; }
            button:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to FastAPI</h1>
            <p>This is a dynamic web app deployed on Render.</p>
            <form action="/greet" method="post">
                <input type="text" name="name" placeholder="Enter your name" required>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/greet", response_class=HTMLResponse)
async def greet_user(name: str = Form(...)):
    print(f"Successfully received form submission: {name} 🎉")
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greeting</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 50px; display: flex; justify-content: center; }}
            .card {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }}
            h1 {{ color: #28a745; font-size: 28px; margin-bottom: 10px; }}
            p {{ color: #555; font-size: 18px; margin-bottom: 25px; }}
            a {{ display: inline-block; background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; transition: background-color 0.3s; }}
            a:hover {{ background-color: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, {name}!</h1>
            <p>Your dynamic form submission was successful.</p>
            <a href="/">Go Back</a>
        </div>
    </body>
    </html>
    """
