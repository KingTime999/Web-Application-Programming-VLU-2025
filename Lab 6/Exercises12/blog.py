from flask import Flask, render_template, abort

app = Flask(__name__)

# Dữ liệu bài viết mẫu
posts = {
    1: {"title": "First Post", "content": "Hello, world!"},
    2: {"title": "Second Post", "content": "This is another blog post."},
    3: {"title": "Third Post", "content": "Flask makes web development easy."}
}

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = posts.get(post_id)
    if not post:
        return "Post not found", 404
    return render_template('blog.html', title=post["title"], content=post["content"])

if __name__ == '__main__':
    app.run(debug=True, port=5011)
