pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/darvin00/HTS_Assignment.git'
            }
        }
        stage('List Files') {
            steps {
                sh 'ls -R'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                # Use Bash explicitly
                bash -c "
                # Install python3-venv and python3-pip (necessary for virtual environment creation)
                sudo -S apt-get update
                sudo -S apt-get install -y python3-venv python3-pip
                
                # Create a virtual environment
                python3 -m venv venv
                source venv/bin/activate
                
                # Upgrade pip and install dependencies
                pip install --upgrade pip
                pip install --upgrade werkzeug requests pytest
                pip install --upgrade Flask
                pip install -r pytests/requirements.txt
                pip install pytest
                "
                '''
            }
        }
        stage('Pull Docker Image') {
            steps {
                script {
                    // Pull the Docker image from Docker Hub 
                    sh 'docker pull xave01/hts_assignment:applatest'
                }
            }
        }
        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }
        stage('Run Docker Image') {
            steps {
                script {
                    // Run the pulled Docker image in detached mode
                    sh 'docker run -d --name hts-assignment-container xave01/hts_assignment:applatest'
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                # Run tests inside Bash to ensure virtualenv works
                bash -c "
                source venv/bin/activate
                pytest pytests/
                "
                '''
            }
        }
    }
}
