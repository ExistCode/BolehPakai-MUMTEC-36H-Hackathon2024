# Western Digital x MUMTEC-36H-Hackathon 2024-
# Boleh Pakai – MUMTEC Hackathon 2024 Submission

## Project Title: Revo

### Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Features](#features)
6. [Architecture](#architecture)

(feel free to add any content or sections)

---

### Project Overview
The "Revo" project is an AI-powered tool designed to assist firmware developers in optimizing their code for embedded systems. It aims to simplify the development process by providing real-time analysis and tailored suggestions for improving code efficiency, memory usage, and runtime performance.

In the context of embedded systems development, optimizing code for speed, memory, and power consumption is crucial. "Revo" addresses these challenges by analyzing code snippets, identifying common inefficiencies, and recommending best practices. This not only accelerates the development process but also helps developers produce high-quality, optimized code.

- **Problem Statement**: Embedded Systems Development Challenges:
Embedded system developers often face significant challenges in optimizing their code for performance, memory usage, and power efficiency. This task is further complicated by:

  - Limited Resources: Embedded systems operate on hardware with constrained computational power, memory, and storage.
  - Time-Consuming Debugging: Identifying inefficiencies and bottlenecks in the code often requires manual inspection, which is both time-consuming and prone to errors.
  - Lack of Standardized Best Practices: Developers may not always be aware of the best practices for optimizing embedded code, leading to suboptimal performance and increased development time.
  These challenges result in extended development cycles, inefficient code, and potential failures in critical applications like IoT devices, automotive systems, and industrial automation.

- **Proposed Solution**: Revo – AI-Powered Code Optimization Assistant
To address these challenges, Revo offers an AI-driven tool that assists developers by providing real-time analysis and suggestions for code optimization. This tool is designed specifically for embedded system development, with a focus on reducing inefficiencies and improving code quality.

Key Features and Benefits:
- AI-Powered Code Analysis: Uses a trained machine learning model to analyze the provided code snippet and identify common inefficiencies, such as redundant calculations, blocking delays, and memory-intensive operations.
- Tailored Optimization Suggestions: Generates context-aware optimization tips, including best practices for embedded system development. This guidance helps developers refine their code for better performance, reduced memory usage, and energy efficiency.
- Detailed Reporting: Produces a comprehensive analysis report outlining the detected issues, optimized code snippets, potential impact, complexity, and alternative approaches. This empowers developers with actionable insights for immediate improvements.
- Ease of Use: Features a simple, user-friendly interface where developers can paste their code and receive instant feedback. This streamlines the debugging and optimization process, saving valuable development time.
- Non-blocking Processing: The backend is designed to handle multiple code submissions without interrupting ongoing analyses, ensuring a smooth user experience.

Benefits to Developers:
- Achieve faster development cycles with immediate feedback on code optimizations.
- Improve the efficiency and performance of their embedded systems.
- Reduce power consumption and memory usage, which are critical factors in embedded devices.

In summary, "Revo" offers a comprehensive solution to the complexities of embedded system development, empowering developers to produce high-quality, optimized code efficiently.

---

### Technologies Used

- Python 3.7
- HTML
- Tailwind CSS
- Flask
- TensorFlow
- Figma
- Scikit-Learn

---

### Installation and Setup
Clone the Repository:
git clone [https://github.com/your-username/boleh-pakai.git](https://github.com/ExistCode/BolehPakai-MUMTEC-36H-Hackathon2024.git)

Navigate to the Project Directory:
cd revo

Install all the dependancies:
pip install -r requirements.txt

Set Up a Virtual Environment:
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

Set Up the Static Folder:
Ensure all assets like images are placed in the static/assets/images/ directory.

Run the Flask Application:
python app.py
The app should now be running on http://127.0.0.1:5000/.

--- 

### Usage
After setting up the application, you can use "Revo" to analyze and optimize code:

Open the Application:
Go to http://127.0.0.1:5000/ in your web browser.

Paste Code for Analysis:
Use the text editor on the left side to paste your code snippet.

Analyze the Code:
Click the "Analyze Code" button to submit the code for processing.

View Suggestions:
The application will display detailed suggestions, including optimization tips, estimated performance gains, and alternative approaches.

--- 

### Features
"Revo" provides the following key features to enhance the developer's coding experience:

Code Analysis: Processes code snippets to identify areas of improvement, such as memory usage, runtime inefficiencies, and best practices.
AI-Powered Suggestions: Utilizes a trained machine learning model to suggest code optimizations tailored to embedded systems.
Detailed Reports: Provides comprehensive information, including:
Issue Type: Categorization of the detected issue (e.g., Memory Inefficiency).
Optimized Code: A suggested code snippet that improves upon the provided code.
Potential Impact: Details the effect of the suggested change on performance.
Non-blocking Analysis: The app can accept new code submissions while processing ongoing analyses, thanks to efficient backend handling.
User-Friendly Interface: Designed using Tailwind CSS for an intuitive and responsive frontend.

--- 

### Architecture
![architectural-diagram drawio](https://github.com/user-attachments/assets/374ed45a-a4a6-4892-88e0-8377fed74825)

--- 

