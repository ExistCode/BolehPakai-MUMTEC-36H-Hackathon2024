import re
from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the pre-trained model and vectorizer
model = joblib.load('model/KNN_model.pkl')
vectorizer = joblib.load('model/firmware_vectorizer.pkl')

# Load the dataset containing inefficient code, issue types, and optimized code
df = pd.read_csv('dummy.csv')

# Function to check if the input is valid code
def is_valid_code(snippet):
    # Regular expression to check for common code elements (basic validation)
    code_pattern = re.compile(r'[{}();=\[\]]|int|char|float|double|if|for|while|malloc|free|return')
    return bool(code_pattern.search(snippet))

def identify_and_optimize_code(snippet):
    # Validate if input is a code snippet
    if not is_valid_code(snippet):
        return "Invalid input: Only code snippets are accepted."

    # Split the input code into lines
    lines = snippet.split('\n')
    issues = []
    optimized_lines = []

    # Perform a line-by-line analysis to detect specific inefficiencies
    for idx, line in enumerate(lines):
        # Transform the line using the vectorizer for prediction
        line_vectorized = vectorizer.transform([line])
        line_prediction = model.predict(line_vectorized)[0]

        # Debugging: Print the prediction for each line
        print(f"Line {idx + 1}: '{line.strip()}' - Predicted issue type: {line_prediction}")

        # Retrieve the corresponding optimized code from the dataset
        matching_rows = df[df['issue_type'] == line_prediction]

        if not matching_rows.empty:
            line_optimized_row = matching_rows.sample(1)

            # Extract all relevant information from the row
            line_optimized_info = {
                'issue_type': line_optimized_row['issue_type'].values[0],
                'issue_description': line_optimized_row['issue_description'].values[0],
                'suggestion': line_optimized_row['suggestion'].values[0],
                'optimized_code': line_optimized_row['optimized_code'].values[0],
                'complexity': line_optimized_row['complexity'].values[0],
                'runtime_estimate': line_optimized_row['runtime_estimate'].values[0],
                'memory_estimate': line_optimized_row['memory_estimate'].values[0],
                'hardware_constraints': line_optimized_row['hardware_constraints'].values[0],
                'safety_security_impact': line_optimized_row['safety_security_impact'].values[0],
                'implementation_notes': line_optimized_row['implementation_notes'].values[0],
                'estimated_performance_gain': line_optimized_row['estimated_performance_gain'].values[0],
                'difficulty_level': line_optimized_row['difficulty_level'].values[0]
            }

            # Record the issue and optimization
            issues.append((idx + 1, line_optimized_info, line))
            optimized_lines.append(f"// Line {idx + 1}: Optimized\n{line_optimized_info['optimized_code']}")
        else:
            # If no inefficiency is detected, keep the line as is
            optimized_lines.append(line)

    # Generate output information
    num_issues = len(issues)
    optimized_code = '\n'.join(optimized_lines)

    return {
        'num_issues': num_issues,
        'issues': issues,
        'optimized_code': optimized_code
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == "POST":
        input_code = request.form['code_snippet']
        result = identify_and_optimize_code(input_code)
        print(result)
        return render_template('test-home-screen.html', result=result)
    
    return render_template('test-home-screen.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# # Example code snippet input
# input_code = input("Enter the code snippet to optimize:\n")

# # Analyze the input code
# result = identify_and_optimize_code(input_code)

# # Output the results
# if isinstance(result, str):
#     print(result)  # This will print the error message for invalid input
# else:
#     print(f"Number of issues found: {result['num_issues']}")
#     for issue in result['issues']:
#         line, info, original_line = issue
#         print(f"Issue at line {line}:")
#         print(f"  - Original Code: {original_line.strip()}")
#         print(f"  - Issue Type: {info['issue_type']}")
#         print(f"  - Description: {info['issue_description']}")
#         print(f"  - Suggestion: {info['suggestion']}")
#         print(f"  - Complexity: {info['complexity']}")
#         print(f"  - Runtime Estimate: {info['runtime_estimate']}")
#         print(f"  - Memory Estimate: {info['memory_estimate']}")
#         print(f"  - Hardware Constraints: {info['hardware_constraints']}")
#         print(f"  - Safety/Security Impact: {info['safety_security_impact']}")
#         print(f"  - Implementation Notes: {info['implementation_notes']}")
#         print(f"  - Estimated Performance Gain: {info['estimated_performance_gain']}")
#         print(f"  - Difficulty Level: {info['difficulty_level']}")

#     print("\nOptimized Code:\n")
#     print(result['optimized_code'])