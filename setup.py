from setuptools import setup, find_packages

setup(
    name="experiment-days",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gemini-python",
        "sydney-py",
        "scikit-learn",
        "shap",
        "ruff",
    ],
    python_requires=">=3.11",
)