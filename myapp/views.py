from django.shortcuts import render
from .models import Task
import pandas as pd
import os

def dashboard(request):
    tasks = Task.objects.all()
    csv_file = os.path.join(
        os.path.dirname(__file__),
        "students.csv"
    )
    df = pd.read_csv(csv_file)
    # Convert DataFrame to list
    students = df.to_dict("records")
    total_students = len(df)
    average_marks = round(
        df["marks"].mean(),
        2
    )
    highest_marks = df["marks"].max()
    context = {
        # Previous information
        "name": "Addan",
        "course": "BSCS",
        "time": "1st Semester",
        # Tasks from database
        "tasks": tasks,
        # CSV students
        "students": students,
        # Pandas results
        "total_students": total_students,
        "average_marks": average_marks,
        "highest_marks": highest_marks,
    }
    return render(
        request,
        "myapp/dashboard.html",
        context
    )