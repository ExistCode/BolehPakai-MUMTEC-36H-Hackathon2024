from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('Unique_Code_Optimization_Dataset__5000_Records_.csv')

# Normalize suggestions in the dataset
data['suggestion'] = data['suggestion'].str.strip().str.lower()

# Group by 'suggestion' and keep the first entry for each unique suggestion
data_unique = data.groupby('suggestion').first().reset_index()

# Create the dictionary mapping each suggestion to its corresponding details
suggestion_details = data_unique.set_index('suggestion').to_dict(orient='index')

# Load the trained model and vectorizer
with open('model/optimizer_model.pkl', 'rb') as file:
    model, vectorizer = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        # Get the code snippet from the form input
        user_code_lines = request.form['code_snippet'].splitlines()
        user_code_snippet = "\n".join(user_code_lines)

        # Transform the input code snippet using the vectorizer
        user_code_vect = vectorizer.transform([user_code_snippet])

        # Use the model to get the suggestion and normalize it
        suggestion = model.predict(user_code_vect)[0].strip().lower()

        # Retrieve additional details based on the suggestion
        details = suggestion_details.get(suggestion, {
            "issue_type": "Unknown",
            "issue_description": "No description available.",
            "optimized_code": "No optimized code available.",
            "impact": "Impact not available.",
            "complexity": "Not specified",
            "runtime_estimate": "Not specified",
            "memory_estimate": "Not specified",
            "alternative_approaches": "Not available",
            "required_libraries": "Not specified",
            "hardware_constraints": "Not specified",
            "context_module": "Not specified",
            "safety_security_impact": "Not specified",
            "edge_cases": "Not specified",
            "implementation_notes": "No notes available.",
            "estimated_performance_gain": "Not specified",
            "difficulty_level": "Not specified",
            "test_cases": "Not specified"
        })

        # Render the result to the HTML template and pass the data
        return render_template('home-screen.html', details=details, suggestion=suggestion)

    return render_template('home-screen.html')

if __name__ == '__main__':
    app.run(debug=True)
