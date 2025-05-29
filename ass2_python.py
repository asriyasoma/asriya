university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

print("Q1: Student Names and Majors")
for student_id, student_info in university_data.items():
    print(f"{student_info['name']} - {student_info['major']}")

print("\nQ2: Average score per course per student")
for student_id, student_info in university_data.items():
    print(f"\nStudent: {student_info['name']}")
    for course, scores in student_info["courses"].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: Average = {avg:.2f}")

print("\nQ3: Students with >90 in final of Python101")
for student_id, student_info in university_data.items():
    courses = student_info["courses"]
    if "Python101" in courses and courses["Python101"]["final"] > 90:
        print(f"{student_info['name']} scored {courses['Python101']['final']} in final")

print("\nQ4: Adding AI101 to student S101")
ai_course = {"midterm": 89, "final": 94, "project": 91}
university_data["S101"]["courses"]["AI101"] = ai_course
print(f"AI101 added for {university_data['S101']['name']}")


print("\nQ5: Average for each course across all students")
from collections import defaultdict

course_totals = defaultdict(lambda: {"midterm": 0, "final": 0, "project": 0, "count": 0})

for student_info in university_data.values():
    for course, scores in student_info["courses"].items():
        for assessment, score in scores.items():
            course_totals[course][assessment] += score
        course_totals[course]["count"] += 1

for course, totals in course_totals.items():
    count = totals["count"]
    avg_midterm = totals["midterm"] / count
    avg_final = totals["final"] / count
    avg_project = totals["project"] / count
    overall_avg = (avg_midterm + avg_final + avg_project) / 3
    print(f"{course}: Average = {overall_avg:.2f}")