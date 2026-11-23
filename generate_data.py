import pandas as pd
import numpy as np

# random code snippets
def generate_code_snippets(num_samples=100):
    code_snippets = []
    for _ in range(num_samples):
        code_length = np.random.randint(5, 20)  # Random length between 5 and 20
        code = ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), code_length))
        code_snippets.append(code)
    return code_snippets

# andom labels (0 or 1)
def generate_labels(num_samples=100):
    return np.random.randint(0, 2, size=num_samples)

# Create labeled data
def create_labeled_data(num_samples=100):
    code_snippets = generate_code_snippets(num_samples)
    labels = generate_labels(num_samples)
    labeled_data = pd.DataFrame({'code_snippet': code_snippets, 'label': labels})
    return labeled_data

# create labeled data and save it to CSV
def main():
    labeled_data = create_labeled_data(num_samples=1000)  
    labeled_data.to_csv('labeled_data.csv', index=False)
    print("Labeled data saved to labeled_data.csv")

if __name__ == "__main__":
    main()
