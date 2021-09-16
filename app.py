from flask import Flask, request, render_template, redirect, url_for
from flask_wtf.recaptcha import validators

from forms import TheForm
from models import posts

app = Flask(__name__)
app.config["SECRET_KEY"] = "ni"

@app.route("/", methods=["GET", "POST"])
def dispatch():
    if request.method == "POST":
        what = request.form.get("what")
        if what == "new":
            return redirect(url_for("add"))
        elif what == "all":
            return redirect(url_for("all"))

    return render_template("dispatch.html")

@app.route("/add/", methods=["POST", "GET"])
def add():
    form = TheForm()
    #error="" ewentualnie potem
    if request.method == "POST":
        if form.validate_on_submit():
            posts.create(form.data)
            posts.save_all()
        return redirect(url_for("dispatch"))

    return render_template("new.html", form=form, posts=posts.all())

@app.route("/all/", methods=["GET", "POST"])
def all():
    form = TheForm()
    if request.method == "POST":
        return redirect(url_for("all"))
    return render_template("all.html", form=form, posts=posts.all())

@app.route("/all/<int:post_id>/", methods=["GET", "POST"])
def edit(post_id):
    post = posts.get(post_id - 1)
    form = TheForm(data=post)

    if request.method == "POST":
        if form.validate_on_submit():
            posts.update(post_id - 1, form.data)
        return redirect(url_for("all"))
    return render_template("edit.html", form=form, post_id=post_id)


if __name__ == "__main__":
    app.run(debug=True)