# app.py
from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    student_name = request.form['student_name']
    pdf_file = request.files['pdf_file']
    pdf_path = os.path.join(UPLOAD_FOLDER, f"{student_name}.pdf")
    pdf_file.save(pdf_path)
    return f"✅ Assignment submitted by {student_name}!"

@app.route('/grade', methods=['POST'])
def grade():
    student_name = request.form['student_name']
    feedback = request.form['feedback']
    q1 = request.form.get('question1', 0)
    q2 = request.form.get('question2', 0)
    q3 = request.form.get('question3', 0)
    total = int(q1) + int(q2) + int(q3)
    return f"📝 Grades submitted for {student_name}. Total: {total}/30. Feedback: {feedback}"

if __name__ == '__main__':
    app.run(debug=True)
