# Book Recommender System Using Machine Learning | Collaborative Filtering

## Overview
A recommendation system helps users discover books they might like without manually searching. This project uses **collaborative filtering**, a popular technique that suggests books based on user preferences and similar readers' choices.

## Types of Recommendation Systems
1. **Content-Based:** Suggests books based on attributes like genre or author. Example: If a user reads sci-fi books, the system recommends more sci-fi.
2. **Collaborative-Based:** Finds similarities between users. If User A and User B both liked Book X, and User B also liked Book Y, the system suggests Book Y to User A.
3. **Hybrid:** Combines both approaches for better accuracy.

## About the Project
This **Streamlit** web app recommends books based on user interests. It uses **Nearest Neighbors** algorithm to find similar books efficiently.

### Workflow:
1. Load book data.
2. Define the number of neighbors (`k`).
3. Compute distances between books using **Euclidean distance**.
4. Sort and return top `k` similar books.

## Dataset
Dataset: https://www.kaggle.com/datasets/saurabhbagchi/books-dataset

## How to Run
### Steps:
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/DipaliKhatua/Book-Recommendation-System-ML
2.  Install Dependencies:
pip install -r requirements.txt

3.  Run the Application:
streamlit run app.py

@ Author
Dipali Khatua

Aspiring Data Scientist

Connect: https://www.linkedin.com/in/dipalikhatua/
