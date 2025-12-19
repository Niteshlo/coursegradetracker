# Course Grade Tracker

A modern, web-based dashboard to track courses, assignments, grades, and calculate GPA.  
Built with **Python Flask** backend and a futuristic frontend design.

---

## 🌟 Features

- ✅ Add, edit, and delete courses with credit hours
- ✅ Add assignments/exams with grades per course
- ✅ Automatic **credit-weighted GPA calculation**
- ✅ View **summary analytics**: total credits, grades, GPA
- ✅ Assignments overview grouped by course
- ✅ Clear navigation between Dashboard, Courses, Grades, Assignments, and Summary
- ✅ Futuristic, modern UI with gradients, glassmorphism, and interactive buttons
- ✅ RESTful API endpoints for grade management
- ✅ Analytics and reporting capabilities

---

## 📋 Project Structure

```
course-grade-tracker/
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── README.md                  # Main project documentation
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
│
├── backend/                   # Flask backend application
│   ├── app.py                # Main Flask application factory
│   ├── config.py             # Configuration (Dev, Prod)
│   ├── requirements.txt       # Backend dependencies
│   ├── README.md             # Backend documentation
│   └── routes/               # API route blueprints
│       ├── pages.py          # Static page routes
│       ├── courses.py        # Course management routes
│       ├── grades.py         # Grade tracking routes
│       └── analytics.py      # Analytics routes
│
└── frontend/                  # Frontend application
    ├── static/               # Static assets
    │   ├── css/
    │   │   └── style.css     # Main stylesheet
    │   └── js/
    │       └── main.js       # Main JavaScript
    └── templates/            # HTML templates
        ├── index.html        # Dashboard/Home
        ├── courses.html      # Courses page
        ├── grades.html       # Grades page
        ├── assignments.html  # Assignments page
        └── summary.html      # Summary/Analytics page
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/Niteshlo/coursegradetracker.git
cd coursegradetracker
```

2. **Create and activate virtual environment**:
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**:
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your settings
# Update database URL, secret key, etc.
```

5. **Run the application**:
```bash
cd backend
python app.py
```

The application will start on `http://localhost:5000`

---

## 🏗️ Architecture

### Backend (Flask)
- **Framework**: Flask microframework
- **Structure**: Modular blueprint-based architecture
- **Routes**:
  - `/` - Dashboard/home page
  - `/courses` - Course management (CRUD operations)
  - `/grades` - Grade tracking and management
  - `/analytics` - Analytics and statistics

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Works on desktop and mobile devices
- **UI Framework**: Custom CSS with modern design patterns
- **Features**: 
  - Glassmorphism effects
  - Gradient backgrounds
  - Interactive buttons and forms
  - Real-time updates

---

## 📚 Detailed Documentation

- [Backend Documentation](backend/README.md) - Complete backend setup and API reference
- [Frontend Documentation](frontend/) - Frontend structure and styling guide

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
```

### Development vs Production
- **Development**: `FLASK_ENV=development` (Debug mode enabled)
- **Production**: `FLASK_ENV=production` (Debug mode disabled)

---

## 🐳 Docker Deployment

Build and run using Docker:

```bash
# Build the image
docker build -t course-grade-tracker .

# Run the container
docker run -p 5000:5000 course-grade-tracker
```

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home/dashboard |
| GET | `/courses` | List all courses |
| POST | `/courses` | Create a new course |
| PUT | `/courses/<id>` | Update course |
| DELETE | `/courses/<id>` | Delete course |
| GET | `/grades` | View grades |
| POST | `/grades` | Record a grade |
| GET | `/analytics` | Get analytics data |

---

## 🔒 Security

- Secret key configuration for session management
- Environment-based configuration
- Separate development and production settings
- Input validation on all routes

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find and kill process using port 5000
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Module Import Errors
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Verify virtual environment is activated
which python  # Linux/Mac - should show venv path
where python  # Windows - should show venv path
```

### Configuration Issues
- Verify `.env` file exists and is properly configured
- Check `FLASK_ENV` is set correctly
- Ensure `SECRET_KEY` is defined

---

## 📝 Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Test thoroughly
4. Commit with meaningful messages: `git commit -m "Add feature description"`
5. Push to your branch: `git push origin feature/your-feature`
6. Create a pull request

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:
- Fork the repository
- Create a feature branch
- Make your changes
- Test your changes
- Submit a pull request with a clear description

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Nitesh Kumar**

---

## 🙏 Acknowledgments

- Flask framework and community
- Contributors and testers
- All those who provided feedback and suggestions

---

## 📞 Support

For issues, questions, or suggestions, please:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include steps to reproduce if reporting a bug

---

**Last Updated**: December 2025
