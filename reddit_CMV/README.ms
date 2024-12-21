# Reddit CMV Dataset: Pro-Vegan Arguments Analysis

This repository contains a filtered subset of the Reddit Change My View (CMV) dataset. The data focuses on threads where the original post (OP) expressed **anti-vegan** or **anti-animal rights/welfare** views. The dataset is curated to identify and analyze **pro-vegan arguments** that successfully persuaded the OP, as indicated by awarded deltas (Δ).

## Dataset Description

The dataset is stored as a CSV file with the following columns:

- **thread_title**: The title of the Reddit thread.
- **author**: The username of the comment author.
- **delta**: Indicates whether the comment received a delta (1 for yes, 0 for no).
- **text**: The content of the comment.

### Example Rows

| thread_title                                     | author         | delta | text                                              |
|-------------------------------------------------|---------------|-------|--------------------------------------------------|
| "Why I think veganism is unnecessary"           | proVeganUser  | 1     | "Actually, studies show that plant-based diets..." |
| "Animals don’t feel pain the way humans do"     | anotherUser   | 0     | "I disagree, but I understand where you're coming from..." |

## Goals of the Dataset

This dataset is designed for researchers, data scientists, and advocates who want to:

- Analyze effective pro-vegan arguments.
- Study the persuasive techniques used in successful comments.
- Examine patterns in anti-vegan rhetoric and the responses they elicit.
- Train or fine-tune machine learning models on argumentation and persuasion.
