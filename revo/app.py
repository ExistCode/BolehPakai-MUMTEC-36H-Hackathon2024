from openai import OpenAI
import os
import re
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def remove_language_markers(text):
    # Remove code block language markers such as ```python``` or ```javascript```
    cleaned_text = re.sub(r'```[a-zA-Z]+\n', '', text)
    return cleaned_text

def mask_sensitive_data(text):
    # Mask potential sensitive data in the code snippet
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)
    text = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP_ADDRESS]', text)
    text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE_NUMBER]', text)
    text = re.sub(r'https?://\S+', '[URL]', text)
    return text

def analyze_code_with_openai(code_snippet):
    try:
        client = OpenAI(api_key='open-ai')

        # Mask the code snippet before sending
        masked_code = mask_sensitive_data(code_snippet)

        # OpenAI API call
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=500,
            messages=[
                {"role": "system",
                 "content": "You are an AI assistant that identifies inefficiencies in code and provides detailed analysis. Output each result using the following format strictly:\n- Inefficient code: [code]\n- Issue type: [issue]\n- Description: [description]\n- Suggestion: [suggestion]\n- Optimized code: [optimized code]\n- Complexity: [complexity]\n- Runtime estimate: [runtime]\n- Memory estimate: [memory]\n- Hardware constraints: [constraints]\n- Safety/security impact: [impact]\n- Implementation notes: [notes]\n- Estimated performance gain: [gain]\n- Difficulty level: [difficulty]. If a field is not applicable, simply write 'N/A'."},
                {"role": "user",
                 "content": f"Analyze the following code snippet and identify any inefficiencies. Provide the analysis using the format specified:\n\nCode snippet:\n{masked_code}"}
            ],
        )

        # Extract the content from the response
        analysis_result = completion.choices[0].message.content
        print(analysis_result)

        # Clean the text before processing
        analysis_result = remove_language_markers(analysis_result)

        # Continue with the rest of your code processing
        result_dict = {}
        pattern = r'-(.*?)\:\s(.*?)(?=\n-\s|$)'  # Modified pattern
        matches = re.findall(pattern, analysis_result, re.DOTALL)

        for match in matches:
            key = match[0].strip().lower().replace(' ', '_')
            value = match[1].strip()
            result_dict[key] = value

        return result_dict

    except Exception as e:
        return {"error": f"Error while processing with OpenAI: {str(e)}"}
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        input_code = request.form['code_snippet']
        result = analyze_code_with_openai(input_code)
    
        return render_template('home-screen.html', result=result)
    return render_template('home-screen.html')

if __name__ == '__main__':
    app.run(debug=True)
