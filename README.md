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
###Trigger the Pipeline:
- **Code Push to Repository**--> When you push your changes to the repository git push origin main GitHub detects the change.
- **Webhook Notification**--> The repository sends a webhook notification to the specified URL which in this case is your CI/CD server **(e.g., Jenkins)**.
- The webhook contains information about the push event, such as the branch, commit details, etc.
- **Webhook Handler on CI/CD Server**--> Jenkins is configured to listen for incoming webhooks
- When it receives the webhook from GitHub it processes the event and triggers the corresponding pipeline job.
- **Pipeline Execution:**--> The CI/CD server Jenkins executes the pipeline steps such as Clone Repository, List Files, Install Dependencies, Pull Docker Image, List Docker Images, Run Docker Image, Run Tests as defined in the Jenkins job configuration.
- **Monitor Results:** --> The results of the pipeline execution (success or failure) will be logged, and it can be check and the status will be in our CI/CD tool's interface.
### Webhook:
![image](https://github.com/user-attachments/assets/ea7b8cdc-2f77-40c2-89b5-ab2a333daf30)

## Access the Deployed Application:
### Live URL:
- After deployment the application will be available at the following URL: http://54.149.140.148:8000
- Verify the Deployment:To verify the deployment visit the /health endpoint of the application. --> http://54.149.140.148:8000/health
- A successful response (HTTP 200) indicates the application is deployed and functioning correctly.
## Screenshots:

