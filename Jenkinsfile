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
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | podman login docker.io -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'podman build . -t docker.io/surote/py-test-jenkins:0.1'
            }
        }
        stage('Stage push') {
            steps {
                sh 'podman push docker.io/surote/py-test-jenkins:0.1'
            }
        }
    }
}
