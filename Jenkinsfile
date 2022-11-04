pipeline {
    agent { any { image 'python:3.10.7-alpine' } }
    stages {
        stage('check') {
            steps {
                sh 'python --version'
            }
        }
    
        stage('Build') {
            steps {
                sh "docker build . -t test:0.1"
            }
        }
    }
}