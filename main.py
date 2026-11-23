import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# read source code from file
def read_source_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()

class StaticCodeAnalyzer:
    # Compiled regular expressions for efficiency
    ENCRYPTION_KEY_PATTERN = re.compile(r'ENCRYPTION_KEY\s*=\s*["\']([^"\']+)["\']')
    SQL_INJECTION_PATTERN = re.compile(r'execute\s*\(\s*"(?:SELECT|INSERT|UPDATE|DELETE).*?"\s*\)')
    XSS_PATTERN = re.compile(r'print\s*\(\s*"([^"]*?)"\s*\)')

    # Regular expressions for code smells and anti-patterns
    CODE_SMELL_PATTERNS = [
        re.compile(r'\bif\s+1==1:'),  
        re.compile(r'\bfor (\w+) in (\w+):'),  
        re.compile(r'\bwhile True:'),  
        re.compile(r'\btry:'),  
        re.compile(r'\bexcept (\w+):'),
    ]
    ANTI_PATTERN_PATTERNS = [
        re.compile(r'\bprint\s*\(.*?\)'),  
        re.compile(r'\blogging\s*\.\s*debug\s*\(.*?\)'),  
        re.compile(r'\bassert\s+.*?'),  
        re.compile(r'\bimport\s+.*?'),  
        re.compile(r'\bglobal\s+.*?'),
    ]

    def __init__(self, source_code):
        self.source_code = source_code

    def detect_security_vulnerabilities(self):
        # Encryption key weakness detection
        encryption_keys = self.ENCRYPTION_KEY_PATTERN.findall(self.source_code)
        if encryption_keys:
            print("Potential encryption key found:", encryption_keys)
            print("Suggestion: Consider using secure encryption methods.")

        # SQL injection detection
        sql_injections = self.SQL_INJECTION_PATTERN.findall(self.source_code)
        if sql_injections:
            print("Potential SQL injection found:", sql_injections)
            print("Suggestion: Use parameterized queries to prevent SQL injection.")

        # XSS vulnerability detection
        xss_vulnerabilities = self.XSS_PATTERN.findall(self.source_code)
        if xss_vulnerabilities:
            print("Potential XSS vulnerability found:", xss_vulnerabilities)
            print("Suggestion: Perform output encoding to prevent XSS attacks.")

    def detect_code_smells(self):
        # detect code smells
        for pattern in self.CODE_SMELL_PATTERNS:
            if pattern.search(self.source_code):
                print("Code smell detected:", pattern.pattern)
                print("Suggestion: Refactor code for better readability.")

    def detect_anti_patterns(self):
        # detect anti-patterns
        for pattern in self.ANTI_PATTERN_PATTERNS:
            if pattern.search(self.source_code):
                print("Anti-pattern detected:", pattern.pattern)
                print("Suggestion: Avoid using anti-patterns for better code quality.")

    def integrate_with_ci_cd(self):
        # Integration with CI/CD pipelines
        if os.environ.get('CI') == 'true' or os.environ.get('CD') == 'true':
            print("Integration with CI/CD pipeline detected. Performing static code analysis...")

            # Perform static code analysis during CI/CD process
            self.detect_security_vulnerabilities()
            self.detect_code_smells()
            self.detect_anti_patterns()

            print("Static code analysis completed.")
        else:
            print("CI/CD integration not detected.")
            print("Suggestion: Integrate with CI/CD pipelines for automated analysis.")

    def generate_report(self, report_format='txt'):
        # Generating analysis report
        report_content = []

        # Append static code analysis header
        report_content.append("Static Code Analysis Report:\n")
        report_content.append("----------------------------\n")
        report_content.append("Source Code:\n")
        report_content.append(self.source_code)
        report_content.append("\n\n")

        # Append CI/CD integration status
        report_content.append("Integration with CI/CD Pipelines:\n")
        report_content.append("Integration with CI/CD pipeline detected." if os.environ.get('CI') == 'true' or os.environ.get('CD') == 'true' else "CI/CD integration not detected.")
        report_content.append("\n\n")

        # Perform static code analysis and append findings to the report
        findings = []

        # Detect security vulnerabilities
        encryption_keys = self.ENCRYPTION_KEY_PATTERN.findall(self.source_code)
        if encryption_keys:
            findings.append("Potential encryption key found: " + str(encryption_keys))
            findings.append("Suggestion: Consider using secure encryption methods.")

        sql_injections = self.SQL_INJECTION_PATTERN.findall(self.source_code)
        if sql_injections:
            findings.append("Potential SQL injection found: " + str(sql_injections))
            findings.append("Suggestion: Use parameterized queries to prevent SQL injection.")

        xss_vulnerabilities = self.XSS_PATTERN.findall(self.source_code)
        if xss_vulnerabilities:
            findings.append("Potential XSS vulnerability found: " + str(xss_vulnerabilities))
            findings.append("Suggestion: Perform output encoding to prevent XSS attacks.")

        # Detect code smells
        for pattern in self.CODE_SMELL_PATTERNS:
            if pattern.search(self.source_code):
                findings.append("Code smell detected: " + pattern.pattern)
                findings.append("Suggestion: Refactor code for better readability.")

        # Detect anti-patterns
        for pattern in self.ANTI_PATTERN_PATTERNS:
            if pattern.search(self.source_code):
                findings.append("Anti-pattern detected: " + pattern.pattern)
                findings.append("Suggestion: Avoid using anti-patterns for better code quality.")

        if not findings:
            findings.append("No security vulnerabilities, code smells, or anti-patterns detected.")

        report_content.extend(findings)

        # Write report content to file
        with open('analysis_report.txt', 'w') as file:
            file.write('\n'.join(report_content))

class MachineLearningAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.classifier = LogisticRegression()

    def train_model(self, labeled_data):
        # Preparing data
        code_snippets = labeled_data['code_snippet']
        labels = labeled_data['label']

        # Vectorizing code snippets
        X = self.vectorizer.fit_transform(code_snippets)

        # Splitting data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

        # Training the classifier
        self.classifier.fit(X_train, y_train)

        # Evaluating the model
        y_pred_train = self.classifier.predict(X_train)
        train_accuracy = accuracy_score(y_train, y_pred_train)
        print("Training Accuracy:", train_accuracy)

        y_pred_test = self.classifier.predict(X_test)
        test_accuracy = accuracy_score(y_test, y_pred_test)
        print("Testing Accuracy:", test_accuracy)

    def predict(self):
        # Vectorize the source code
        code_vector = self.vectorizer.transform([self.source_code])

        # Predict using the trained model
        prediction = self.classifier.predict(code_vector)

        # Print prediction
        if prediction[0] == 1:
            print("The code contains a security vulnerability.")
        else:
            print("The code is secure.")

# Main function
def main():
    # Read labeled data
    labeled_data = pd.read_csv('labeled_data.csv')  

    # Initialize MachineLearningAnalyzer and perform training
    ml_analyzer = MachineLearningAnalyzer(None)  
    ml_analyzer.train_model(labeled_data)

    
    source_code = read_source_code('input.txt')

    # Perform static code analysis
    analyzer = StaticCodeAnalyzer(source_code)
    analyzer.integrate_with_ci_cd()
    analyzer.generate_report()  

    # Predict using machine learning model
    ml_analyzer.source_code = source_code
    ml_analyzer.predict()

if __name__ == "__main__":
    main()
