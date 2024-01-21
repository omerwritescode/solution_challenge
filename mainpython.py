from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for job listings
jobs = [
    {"title": "Software Engineer", "skills": ["Python", "JavaScript", "Web Development"]},
    {"title": "Data Scientist", "skills": ["Python", "Machine Learning", "Statistics"]},
    {"title": "Graphic Designer", "skills": ["Adobe Creative Suite", "UI/UX Design"]}
]

@app.route('/')
def index():
    return render_template('index.html', jobs=jobs)

@app.route('/match', methods=['POST'])
def match():
    user_skills = request.form.get('skills').split(',')
    
    matched_jobs = []
    for job in jobs:
        if all(skill in user_skills for skill in job['skills']):
            matched_jobs.append(job)

    return render_template('match_result.html', user_skills=user_skills, matched_jobs=matched_jobs)

if __name__ == '__main__':
    app.run(debug=True)