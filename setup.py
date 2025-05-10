from setuptools import setup

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define package metadata
REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Dipali-Khatua" 
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy', 'pandas', 'scikit-learn']

setup(
    name="books_recommendation_system", 
    version="0.0.1",
    author="Dipali-Khatua",
    description="A package for a Book Recommender System using collaborative filtering and clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/DipaliKhatua/Book-Recommendation-System-ML",
    packages=[""], 
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
