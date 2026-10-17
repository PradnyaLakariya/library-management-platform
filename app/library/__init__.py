from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import REGISTRY


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

    requests_total = Counter(
        "library_http_requests_total",
        "Total requests to the library application",
        ["endpoint", "method"],
        registry=REGISTRY,
    )

    @app.before_request
    def count_request():
        endpoint = request.endpoint or "unknown"
        requests_total.labels(
            endpoint=endpoint,
            method=request.method,
        ).inc()

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

    @app.get("/metrics")
    def metrics():
        return generate_latest(REGISTRY), 200, {
            "Content-Type": CONTENT_TYPE_LATEST
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
