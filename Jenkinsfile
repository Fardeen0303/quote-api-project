pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Fardeen0303/quote-api-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t quote-api .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 quote-api'
            }
        }

    }
}
