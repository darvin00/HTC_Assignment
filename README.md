# HTS_Assignment
## Overview of the Application:
- Purpose: This is a simple web application that provides a health check endpoint to verify if the application is running smoothly.
- Tech Stack: Technologies used Python/Flask, Jenkins for CI/CD, Docker for creating images and aws EC2 for deploying the web application
## Instructions to Run the Application Locally:
### Prerequisites:
- Python: 3.10.12
- Docker: 27.3.1 (build ce12230)
- Jenkins: 2.479.2
- Flask: 2.1.2
- Werkzeug: 2.0.3
- pytest: 7.1.2
- requests: 2.28.1
- Web Application: Running on port 8000
### Steps to Set Up Locally:
- Clone the repository: git clone https://github.com/darvin00/HTS_Assignment.git
- Install dependencies: pip install -r requirements.txt
- Run the application: python app.py 
- Access the application locally at http://54.149.140.148:8000.
- Test the /health endpoint by visiting http://54.149.140.148:8000/health.
## CI/CD Pipeline Setup Instructions:
- Commit and Push Changes and push to the GitHub repository triggering the CI/CD pipeline.
![image](https://github.com/user-attachments/assets/9e61c268-a38b-4b4b-a3b6-56210f6cff73)
--> git add .
--> git commit -m "updated commit"
--> git push origin main
![image](https://github.com/user-attachments/assets/ea7b8cdc-2f77-40c2-89b5-ab2a333daf30)
