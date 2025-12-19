from flask import Blueprint, request, jsonify
from typing import List, Dict
from routes.courses import courses

grades_bp = Blueprint("grades", __name__)

grades: List[Dict] = []
VALID_GRADES = {"A", "B", "C", "D", "F"}


@grades_bp.route("/api/grades", methods=["GET"])
def get_grades():
    return jsonify(grades)


@grades_bp.route("/api/grades", methods=["POST"])
def add_grade():
    data = request.get_json()
    course_id = data.get("course_id")
    assignment_name = data.get("assignment")
    grade = data.get("grade", "").upper()

    if grade not in VALID_GRADES:
        return jsonify({"error": "Invalid grade"}), 400

    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        return jsonify({"error": "Course not found"}), 400

    grade_entry = {
        "course_id": course_id,
        "course": course["name"],
        "credits": course["credits"],
        "assignment": assignment_name,
        "grade": grade
    }

    grades.append(grade_entry)
    return jsonify({"message": "Grade added"}), 201


@grades_bp.route("/api/grades/<int:index>", methods=["DELETE"])
def delete_grade(index):
    if 0 <= index < len(grades):
        grades.pop(index)
        return jsonify({"message": "Grade deleted"})
    return jsonify({"error": "Index out of range"}), 400


@grades_bp.route("/api/grades/reset", methods=["DELETE"])
def reset_grades():
    grades.clear()
    return jsonify({"message": "Grades reset"})
