# Academic Performance Tracker

A modern, web-based dashboard to track courses, assignments, grades, and calculate GPA.  
Built with **Python Flask** and a futuristic frontend design.

---

## 🌟 Features

- Add, edit, and delete courses with credit hours
- Add assignments/exams with grades per course
- Automatic **credit-weighted GPA calculation**
- View **summary analytics**: total credits, grades, GPA
- Assignments overview grouped by course
- Clear navigation between Dashboard, Courses, Grades, Assignments, and Summary
- Futuristic, modern UI with gradients, glassmorphism, and interactive buttons

---

## 🗂 Project Structure

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── routes/
│ ├── pages.py
│ ├── courses.py
│ ├── grades.py
│ └── analytics.py
│
├── templates/
│ ├── index.html
│ ├── courses.html
│ ├── grades.html
│ ├── assignments.html
│ └── summary.html
│
└── static/
└── css/
└── style.css



---

## ⚙️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/academic-performance-tracker.git
cd academic-performance-tracker

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt


python app.py
