from flask import Flask
import os


def create_app():
    # Set template and static folder paths
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/static'))
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

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
