pipeline {
    agent any
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
                sh 'podman build . -t surote/py-test:0.1'
            }
        }
    }
}
