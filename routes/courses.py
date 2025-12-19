from flask import Blueprint, request, jsonify
from typing import List, Dict

courses_bp = Blueprint("courses", __name__)

courses: List[Dict] = []
course_id_counter = 1


@courses_bp.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)


@courses_bp.route("/api/courses", methods=["POST"])
def add_course():
    global course_id_counter
    data = request.get_json()
    name = data.get("name")
    credits = data.get("credits")

    if not name or not isinstance(credits, int) or credits <= 0:
        return jsonify({"error": "Invalid input"}), 400

    course = {
        "id": course_id_counter,
        "name": name,
        "credits": credits
    }
    courses.append(course)
    course_id_counter += 1
    return jsonify(course), 201


@courses_bp.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    global courses
    courses = [c for c in courses if c["id"] != course_id]
    return jsonify({"message": "Course deleted"})


@courses_bp.route("/api/courses/reset", methods=["DELETE"])
def reset_courses():
    global courses, course_id_counter
    courses.clear()
    course_id_counter = 1   # reset counter here
    return jsonify({"message": "Courses reset"})

