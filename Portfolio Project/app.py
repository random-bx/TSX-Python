import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)

PROFILE_DATA = {
    "name": "Biswajit Das",
    "tagline": "Passionate Developer | Tech Enthusiast | Lifelong Learner",
    "bio": "Hi! I'm a passionate developer with a keen interest in Python and AI."
           "I love building creative and efficient solutions to complex problems."
           "This portfolio showcases some of the projects I've worked on and the skills I've developed."
           "From innovative web applications to optimized algorithms, each project reflects my dedication to learning, problem-solving, and delivering quality work."
           "Feel free to explore and reach out if you'd like to connect!",
    "email": "biswajit.das.63716@gmail.com",
    "linkedin": "https://www.linkedin.com/in/biswajitdas17/",
    "github": "https://github.com/random-bx",
    "profile_picture": "images/profile.jpg"
}

SKILLS = [
    {"name": "Python", "level": 90},
    {"name": "Java", "level": 100},
    {"name": "Flask", "level": 85},
    {"name": "HTML5", "level": 95},
    {"name": "CSS3", "level": 80},
    {"name": "JavaScript", "level": 70},
    {"name": "Git & GitHub", "level": 85}
]

PROJECTS_DATA = [
    {
        "id": "project-1",
        "title": "Awesome Project Alpha",
        "description": "A brief description of Project Alpha, highlighting its key features and the problems it solves. Built with Python and Flask.",
        "image": "images/project1.jpg",
        "link": "#",
        "technologies": ["Python", "Flask", "HTML", "CSS"]
    },
    {
        "id": "project-2",
        "title": "Innovative Solution Beta",
        "description": "Details about Solution Beta. This project focused on data analysis and visualization using modern tools.",
        "image": "images/project2.jpg",
        "link": "#",
        "technologies": ["Python", "Pandas", "Matplotlib"]
    },
    {
        "id": "project-3",
        "title": "Portfolio Website (This one!)",
        "description": "This very portfolio, built to showcase my skills in web development using Flask and dynamic content generation.",
        "image": "images/portfolio_ss.png",
        "link": "#",
        "technologies": ["Python", "Flask", "HTML", "CSS", "Jinja2"]
    }
]

@app.route('/')
def home():
    return render_template('index.html', profile=PROFILE_DATA, skills=SKILLS)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS_DATA, profile=PROFILE_DATA)

@app.context_processor
def inject_current_year():
    """Makes the current year available to all templates."""
    return {'_current_year': datetime.datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)
