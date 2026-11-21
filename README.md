# AI Resume Screening System

**Future Interns — Machine Learning Track, Task 3**

This project demonstrates an end-to-end machine learning workflow for screening resumes. It reads candidate profiles, extracts technical skills, compares each profile with a job description, ranks candidates, and identifies missing skills.

## Project contents

| Path | Description |
|---|---|
| `resume_screening.ipynb` | Complete data-processing, ranking, visualization, and evaluation workflow |
| `data/resumes/` | 40 fictional resume examples in text format |
| `data/job_description.txt` | Sample Machine Learning Engineer role |
| `data/generate_data.py` | Rebuilds the fictional resume dataset |
| `outputs/ranked_candidates.csv` | Ranked candidates with scores and skill gaps |
| `outputs/01_top_candidates.png` | Top-candidate score chart |
| `outputs/02_skill_availability.png` | Candidate skill-frequency chart |

## Screening method

1. Clean and normalize resume text while preserving technical terms such as `c++`, `node.js`, and `ci/cd`.
2. Extract skills using a curated dictionary and word-boundary matching.
3. Parse required skills, preferred skills, and minimum experience from the job description.
4. Calculate an experience score and TF-IDF text similarity.
5. Combine scores to rank candidates and produce missing-skill lists.

The final score combines 60% skill match, 25% TF-IDF cosine similarity, and 15% experience fit. Skill match itself gives 75% weight to required skills and 25% to preferred skills.

## Dataset

The resumes are fictional and were generated only for demonstration. They do not represent real people or employment records. The generator creates varied summaries, project descriptions, education details, and experience levels.

Replace `data/resumes/` and `data/job_description.txt` with your own approved resumes and role description to run the system on a new candidate set.

> This system is a screening aid, not an automated hiring decision maker. Human review is essential, and real-world use should include bias and fairness checks.

## Setup and run

```bash
pip install -r requirements.txt
jupyter notebook resume_screening.ipynb
```

To regenerate the fictional dataset:

```bash
python data/generate_data.py
```

## Technologies

Python, Pandas, NumPy, Scikit-learn, TF-IDF, cosine similarity, Matplotlib, and regular expressions.
