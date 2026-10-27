import os

os.environ["DB_DRIVER"] = "sqlite"
os.environ["DB_USER"] = ""
os.environ["DB_PASSWORD"] = ""
os.environ["DB_HOST"] = ""
os.environ["DB_PORT"] = "0"
os.environ["DB_NAME"] = "test.db"


from src.presentation.api.factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
