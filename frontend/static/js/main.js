// --- Courses ---
async function loadCourses() {
    const res = await fetch("/api/courses");
    const courses = await res.json();
    const list = document.getElementById("course-list");
    const select = document.getElementById("course-select");
    if(list) list.innerHTML = "";
    if(select) select.innerHTML = "";

    courses.forEach(c => {
        if(list) list.innerHTML += `<li>${c.id}. ${c.name} (${c.credits} credits)
            <button onclick="deleteCourse(${c.id})">Delete</button></li>`;
        if(select) select.innerHTML += `<option value="${c.id}">${c.name}</option>`;
    });
}

async function addCourse() {
    const name = document.getElementById("course-name").value;
    const credits = parseInt(document.getElementById("course-credits").value);
    await fetch("/api/courses", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({name, credits})
    });
    loadCourses();
}

async function deleteCourse(id) {
    await fetch(`/api/courses/${id}`, {method:"DELETE"});
    loadCourses();
}

async function resetCourses() {
    await fetch("/api/courses/reset",{method:"DELETE"});
    loadCourses();
}

// --- Grades ---
async function loadGrades() {
    const res = await fetch("/api/grades");
    const grades = await res.json();
    const list = document.getElementById("grade-list");
    list.innerHTML = "";

    grades.forEach((g, index) => {
        list.innerHTML += `<li>${g.course} - ${g.assignment}: ${g.grade} 
        <button onclick="deleteGrade(${index})">Delete</button></li>`;
    });

    if(grades.length === 0) {
        list.innerHTML = "<li>No grades added yet.</li>";
    }
}


async function addGrade() {
    const courseSelect = document.getElementById("course-select");
    const assignmentInput = document.getElementById("assignment-name");
    const gradeSelect = document.getElementById("grade-select");

    const course_id = parseInt(courseSelect.value);
    const assignment = assignmentInput.value.trim();
    const grade = gradeSelect.value;

    if (!assignment) {
        alert("Please enter assignment/exam name");
        return;
    }

    const res = await fetch("/api/grades", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({course_id, assignment, grade})
    });

    const data = await res.json();
    if (res.ok) {
        assignmentInput.value = "";   // clear input after adding
        loadGrades();
    } else {
        alert(data.error || "Error adding grade");
    }
}


async function deleteGrade(index) {
    await fetch(`/api/grades/${index}`, {method:"DELETE"});
    loadGrades();
}

async function resetGrades() {
    await fetch("/api/grades/reset",{method:"DELETE"});
    loadGrades();
}

// --- Summary ---
async function loadStats() {
    const gpaRes = await fetch("/api/gpa");
    const gpaData = await gpaRes.json();
    document.getElementById("gpa").innerText = `GPA: ${gpaData.gpa}`;

    const statsRes = await fetch("/api/stats");
    const statsData = await statsRes.json();
    document.getElementById("stats").innerText = `Total Grades: ${statsData.total_grades}, Total Credits: ${statsData.total_credits}`;
}
