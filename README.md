# AI-Powered Static Code Analyzer

## Overview
A Python-based code analysis tool that combines static code analysis and machine learning to identify potential security vulnerabilities, code smells, and programming anti-patterns.

## Features
- Detects potential encryption key exposure.
- Identifies possible SQL injection and XSS vulnerabilities.
- Detects code smells and anti-patterns.
- Uses machine learning to classify potentially vulnerable code.
- Supports CI/CD pipeline integration checks.
- Generates automated analysis reports.

## Technologies Used
- Python 3
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Regular Expressions

## Installation

```bash
pip install pandas scikit-learn
```

## Project Files

```text
StaticCodeAnalyzer/
├── main.py
├── labeled_data.csv
├── input.txt
├── generate_data.py
└── analysis_report.txt
```

## Run the Project

```bash
python main.py
```

## Machine Learning
The project uses TF-IDF for text feature extraction and Logistic Regression for classifying source code. Model performance is evaluated using training and testing accuracy.

## Output
- Security vulnerability detection results.
- Code quality warnings.
- Machine learning predictions.
- Generated `analysis_report.txt`.
