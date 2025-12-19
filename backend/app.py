from flask import Flask


def create_app():
    app = Flask(__name__)

    from routes.pages import pages_bp
    from routes.courses import courses_bp
    from routes.grades import grades_bp
    from routes.analytics import analytics_bp

    app.register_blueprint(pages_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(grades_bp)
    app.register_blueprint(analytics_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
