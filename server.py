from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os
load_dotenv("api.env")
# Flask app
app = Flask(__name__)

@app.route("/")
def blog():
    blog_url = os.getenv("API")
    response = requests.get(blog_url)
    posts=response.json()
    return render_template("index.html", posts=posts)

@app.route("/blog/<int:post_id>")
def get_post(post_id):

    blog_url = os.getenv("API")
    response = requests.get(blog_url)
    posts=response.json()

    for blog_post in posts:

        if blog_post["id"] == post_id:
            post_title = blog_post["title"]
            post_subtitle = blog_post["subtitle"]
            post_body = blog_post["body"]

    return render_template("post.html", post_title=post_title, post_subtitle=post_subtitle, post_body=post_body)

# run flask server when python script runs
if __name__ == "__main__":
    app.run(debug=True)