"""Generate a clearly fictional sample resume dataset."""
import os
import random

random.seed(11)
os.makedirs("data/resumes", exist_ok=True)

pools = {
    "Machine Learning Engineer": ["python", "machine learning", "scikit-learn", "pandas", "numpy", "tensorflow", "pytorch", "deep learning", "sql", "git", "docker"],
    "Data Analyst": ["sql", "excel", "power bi", "tableau", "python", "pandas", "statistics", "data visualization"],
    "Web Developer": ["html", "css", "javascript", "react", "node.js", "mongodb", "git", "rest api"],
    "DevOps Engineer": ["docker", "kubernetes", "aws", "linux", "ci/cd", "terraform", "git", "python"],
    "Data Scientist": ["python", "statistics", "machine learning", "scikit-learn", "pandas", "matplotlib", "sql", "nlp", "deep learning"],
}
first = ["Aarav", "Ananya", "Rohan", "Priya", "Arjun", "Sneha", "Vikram", "Meera", "Rahul", "Isha", "Karan", "Neha", "Aditya", "Pooja", "Sourav", "Riya", "Debarati", "Amit", "Tanvi", "Soham"]
last = ["Sharma", "Das", "Mukherjee", "Patel", "Singh", "Banerjee", "Nair", "Gupta", "Reddy", "Chatterjee"]
colleges = ["Adamas University", "Jadavpur University", "NIT Durgapur", "IIT Kharagpur", "VIT Vellore", "Anna University"]
extra_pool = ["excel", "git", "linux", "statistics", "sql", "matplotlib", "html", "css"]

summaries = [
    "{role} with {years} years of practical experience delivering dependable, data-focused solutions.",
    "Results-oriented {role_lower} who enjoys turning complex requirements into clear, maintainable solutions.",
    "{role} with a track record of collaborating across teams and improving technical workflows.",
    "Curious and adaptable {role_lower} experienced in building projects from prototype through deployment.",
]

project_names = [
    "Operational analytics dashboard",
    "Automated reporting pipeline",
    "Customer insights platform",
    "Model deployment prototype",
    "Internal workflow automation",
]

for i in range(40):
    role = random.choice(list(pools))
    pool = pools[role]
    skill_count = random.randint(max(3, int(len(pool) * 0.5)), len(pool))
    skills = random.sample(pool, skill_count) + random.sample(extra_pool, random.randint(0, 2))
    skills = list(dict.fromkeys(skills))
    years = random.choice([0, 0, 1, 1, 2, 2, 3, 4, 5, 6])
    name = f"{random.choice(first)} {random.choice(last)}"
    summary = random.choice(summaries).format(
        role=role,
        role_lower=role.lower(),
        years=years,
    )
    primary, secondary = (skills + ["team collaboration"] * 2)[:2]
    project = random.choice(project_names)
    degree = random.choice([
        "B.Tech in Computer Science",
        "B.E. in Information Technology",
        "B.Sc. in Computer Science",
        "M.Sc. in Data Science",
    ])

    text = f"""{name}
{role}

PROFESSIONAL SUMMARY
{summary}

CORE SKILLS
{", ".join(skills)}

PROJECT EXPERIENCE
{project}
- Built and evaluated a {role.lower()} solution using {primary} and {secondary}.
- Worked with a small team to document requirements, test outcomes, and improve usability.
- Presented findings and implementation notes to technical and non-technical stakeholders.

WORK EXPERIENCE
{years} years of combined project and professional experience as a {role.lower()}.
- Developed repeatable processes and reusable components for technical assignments.
- Used {", ".join(skills[:3])} to support reporting, analysis, and delivery activities.

EDUCATION
{degree}, {random.choice(colleges)}
"""
    with open(f"data/resumes/resume_{i+1:02d}.txt", "w", encoding="utf-8") as f:
        f.write(text)

jd = """Job Title: Machine Learning Engineer

About the role
We are looking for a Machine Learning Engineer to build and deploy models that solve real business problems.

Required Skills:
Python, machine learning, scikit-learn, pandas, numpy, SQL, git, deep learning

Nice to have:
TensorFlow, PyTorch, Docker, AWS, NLP

Experience: 2+ years preferred
"""
with open("data/job_description.txt", "w", encoding="utf-8") as f:
    f.write(jd)
print("saved 40 resumes + job description")
