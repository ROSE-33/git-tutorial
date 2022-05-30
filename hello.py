from pip import main
from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p> Learn Python Web </p>"
@app.route("/user/admin")
def hello_admin():
    return "<h1> Welcome back Admin<h1>"


@app.route('/user/<name>')
def hello_user(name):
    if name == "admin":
        return redirect(url_for(hello_admin()))
    else: return f"<h1> Hello {name}! <h1>"

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f"<p> Hello Blog {blog_id} </p> "



if __name__ == "__main__":
    app.run(debug = True)
