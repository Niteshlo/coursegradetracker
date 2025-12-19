from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def index():
    return render_template("index.html")


@pages_bp.route("/courses")
def courses():
    return render_template("courses.html")


@pages_bp.route("/grades")
def grades():
    return render_template("grades.html")


@pages_bp.route("/assignments")
def assignments():
    return render_template("assignments.html")


@pages_bp.route("/summary")
def summary():
    return render_template("summary.html")
