from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Hardcoded list of blog posts for simplicity
POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
    {"id": 3, "title": "Flask API", "content": "Creating APIs with Flask."},
    {"id": 4, "title": "Python Web Development", "content": "Building web applications with Python."},
]

# Helper function to generate a new unique post ID
def generate_unique_id():
    if not POSTS:
        return 1
    max_id = max(post['id'] for post in POSTS)
    return max_id + 1

@app.route('/api/posts', methods=['GET'])
def get_posts():
    sort_by = request.args.get('sort', None)
    sort_direction = request.args.get('direction', None)

    # Validate sort_by and sort_direction values
    valid_sort_fields = ['title', 'content']
    valid_sort_directions = ['asc', 'desc']

    if sort_by and sort_by not in valid_sort_fields:
        abort(400, f"Invalid sort field. Allowed values: {', '.join(valid_sort_fields)}")
    if sort_direction and sort_direction not in valid_sort_directions:
        abort(400, f"Invalid sort direction. Allowed values: {', '.join(valid_sort_directions)}")

    # Sort the posts based on provided parameters, or keep the original order
    sorted_posts = sorted(POSTS, key=lambda post: post.get(sort_by, 0), reverse=(sort_direction == 'desc'))

    return jsonify(sorted_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
