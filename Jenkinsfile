pipeline {
    agent any
    stages {
        stage('Stage 1') {
            steps {
                checkout scm
                echo 'Hello world!' 
                sh 'java version'
                sh 'ls -alh'
            }
        }
    }
}
