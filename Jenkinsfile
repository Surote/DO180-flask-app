pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('dockerhub')
      ROX_API_TOKEN = credentials('acs')
    }
    stages {
        stage('Stage checkout') {
            steps {
                checkout scm
                echo 'Hello world! DEV' + env.BRANCH_NAME 
                sh 'echo $BRANCH_NAME'
                sh 'ls -alh'
            }
        }
        stage('Stage build') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | podman login docker.io -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'podman build . -t docker.io/surote/py-test-jenkins:0.1-$BRANCH_NAME'
            }
        }
        stage('Stage push') {
            steps {
                sh 'podman push docker.io/surote/py-test-jenkins:0.1-$BRANCH_NAME'
            }
        }
        stage('Stage scan') {
            steps {
                sh 'podman run -e ROX_API_TOKEN=$ROX_API_TOKEN  -it registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel8:4.0.0 -e https://central-stackrox.apps.cluster-4v75k.4v75k.sandbox2150.opentlc.com:443 image scan --image docker.io/surote/py-test-jenkins:0.1-$BRANCH_NAME'
            }
        }
    }
}
