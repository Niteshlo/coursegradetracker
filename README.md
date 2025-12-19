# Course Grade Tracker - Backend

This is the backend service for the Course Grade Tracker application. It's a Flask-based REST API that handles course management, grade tracking, and analytics.

## Overview

The backend provides APIs for:
- **Courses Management**: Create, read, update, and delete courses
- **Grades Management**: Track and manage student grades
- **Analytics**: Generate grade analytics and statistics
- **Pages**: Serve static pages and content

## Project Structure

```
backend/
├── app.py              # Main Flask application factory
├── config.py           # Configuration settings (Dev, Prod)
├── requirements.txt    # Python dependencies
└── routes/
    ├── pages.py        # Page-related routes
    ├── courses.py      # Course management routes
    ├── grades.py       # Grade tracking routes
    └── analytics.py    # Analytics and statistics routes
```

## Key Files

### `app.py`
- Contains the Flask application factory function `create_app()`
- Registers all blueprints for different route modules
- Main entry point for running the application

### `config.py`
- Defines configuration classes for different environments
- `Config`: Base configuration
- `DevelopmentConfig`: Development environment settings (DEBUG=True)
- `ProductionConfig`: Production environment settings (DEBUG=False)

### Routes

#### `routes/pages.py`
Handles static page routes for the frontend.

#### `routes/courses.py`
Manages course-related operations:
- List all courses
- Create new course
- Update course details
- Delete course

#### `routes/grades.py`
Handles grade tracking and management:
- Record grades for students
- View grades
- Update grades
- Calculate course averages

#### `routes/analytics.py`
Provides analytics and reporting:
- Grade statistics
- Performance analysis
- Class analytics
- Export reports

## Installation & Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   - Copy `.env.example` to `.env` (in root directory)
   - Update environment variables as needed

3. **Run the Application**
   ```bash
   python app.py
   ```
   
   The application will start on `http://localhost:5000` by default (in debug mode).

## Running with Different Configurations

### Development Mode
```bash
export FLASK_ENV=development
python app.py
```

### Production Mode
```bash
export FLASK_ENV=production
python app.py
```

## Dependencies

See `requirements.txt` for a complete list of dependencies. Key packages include:
- **Flask**: Web framework
- **Flask-RESTful**: REST API extensions (if applicable)
- Additional dependencies as specified in requirements.txt

## API Endpoints

The application provides RESTful endpoints for:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home/dashboard page |
| GET | `/courses` | List all courses |
| POST | `/courses` | Create a new course |
| PUT | `/courses/<id>` | Update course |
| DELETE | `/courses/<id>` | Delete course |
| GET | `/grades` | View grades |
| POST | `/grades` | Record a grade |
| GET | `/analytics` | Get analytics data |

*(This is a template - adjust based on actual implementation)*

## Environment Variables

Configure these in your `.env` file:

```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
```

## Error Handling

The application includes standard HTTP error responses:
- `400 Bad Request`: Invalid input data
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server-side errors

## Development Notes

- The application uses Flask blueprints for modular route organization
- Each route module is independently registered with the app
- Configuration can be easily switched between environments
- The factory pattern allows for flexible app instantiation

## Testing

*(To be implemented)*

To run tests:
```bash
pytest
```

## Troubleshooting

- **Port Already in Use**: Change the port in `app.py` or kill the process using port 5000
- **Module Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **Configuration Issues**: Verify `.env` file is properly configured

## Contributing

When making changes to the backend:
1. Create a feature branch from `main`
2. Make your changes following the existing code structure
3. Test thoroughly
4. Submit a pull request

## License

[Add your license information here]

## Author

Nitesh Kumar
