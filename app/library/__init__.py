from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    books = [
        {
            "id": 1,
            "title": "Python Basics",
            "author": "John Smith",
            "available": True,
        },
        {
            "id": 2,
            "title": "DevOps Fundamentals",
            "author": "Jane Doe",
            "available": True,
        },
    ]

    @app.get("/")
    def home():
        return jsonify({
            "message": "Smart Library Management Platform"
        })

    @app.get("/books")
    def list_books():
        return jsonify(books)

    @app.post("/books")
    def add_book():
        data = request.get_json(silent=True) or {}

        if not data.get("title") or not data.get("author"):
            return jsonify({
                "error": "title and author are required"
            }), 400

        book = {
            "id": max((b["id"] for b in books), default=0) + 1,
            "title": data["title"],
            "author": data["author"],
            "available": True,
        }

        books.append(book)
        return jsonify(book), 201

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
