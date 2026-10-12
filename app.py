
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My CATS Test App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f5f9;
                text-align: center;
                padding: 60px 20px;
            }
            .card {
                background: white;
                padding: 35px;
                max-width: 450px;
                margin: auto;
                border-radius: 12px;
                box-shadow: 0 4px 15px #ddd;
            }
            h1 { color: #2457a7; }
            .status { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Test App!</h1>
            <p><b>Name:</b> Tanzeer Ahamed</p>
            <p><b>Role:</b> DevOps Engineer</p>
            <p><b>Platform:</b> CATS</p>
            <p class="status">Application is running!</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
