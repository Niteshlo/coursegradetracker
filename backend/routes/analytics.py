from flask import Blueprint, jsonify
from routes.grades import grades

analytics_bp = Blueprint("analytics", __name__)

GRADE_POINTS = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}


@analytics_bp.route("/api/gpa")
def calculate_gpa():
    total_points = 0.0
    total_credits = 0

    for g in grades:
        total_points += GRADE_POINTS[g["grade"]] * g["credits"]
        total_credits += g["credits"]

    gpa = round(total_points / total_credits, 2) if total_credits else 0.0
    return jsonify({"gpa": gpa})


@analytics_bp.route("/api/stats")
def stats():
    return jsonify({
        "total_courses": len(set(g["course"] for g in grades)),
        "total_grades": len(grades),
        "total_credits": sum(g["credits"] for g in grades)
    })
