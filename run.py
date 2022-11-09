import os
from app import app,db


if __name__ == "__main__":
    db.create_all()
    app.secret_key = os.urandom(12)
    app.run(host = "127.0.0.1",debug=True, port=4000)
