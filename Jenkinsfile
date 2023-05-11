pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Stage checkout') {
            steps {
                checkout scm
                echo 'Hello world!' 
                sh 'java -version'
                sh 'ls -alh'
            }
        }
        stage('Stage build') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | podman login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'podman build . -t surote/py-test-jenkins:0.1'
            }
        }
    }
}
