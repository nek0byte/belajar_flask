from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Message

bp = Blueprint("board", __name__)


@bp.route("/")
def home():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return render_template("index.html", messages=messages)


@bp.route("/about")
def about():
    return "<h1>Tentang</h1><p>Ini adalah mini project belajar Flask.</p>"


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        msg = Message(
            title=request.form["title"],
            author=request.form["author"],
            body=request.form["body"],
        )
        db.session.add(msg)
        db.session.commit()
        flash("Pesan berhasil ditambahkan!", "success")
        return redirect(url_for("board.home"))
    return render_template("create.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    msg = db.session.get(Message, id)
    if msg is None:
        flash("Pesan tidak ditemukan!", "error")
        return redirect(url_for("board.home"))

    if request.method == "POST":
        msg.title = request.form["title"]
        msg.author = request.form["author"]
        msg.body = request.form["body"]
        db.session.commit()
        flash("Pesan berhasil diubah!", "success")
        return redirect(url_for("board.home"))

    return render_template("edit.html", message=msg)


@bp.route("/delete/<int:id>")
def delete(id):
    msg = db.session.get(Message, id)
    if msg is None:
        flash("Pesan tidak ditemukan!", "error")
    else:
        db.session.delete(msg)
        db.session.commit()
        flash("Pesan berhasil dihapus!", "success")
    return redirect(url_for("board.home"))
