pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "alhobab/docker-flask-app"
        GIT_CREDENTIALS_ID = '796a33e1-c4be-4c8c-8438-f84217b7d65c'       // Jenkins-stored GitHub credentials
        DOCKERHUB_CREDENTIALS_ID = 'my-secret' // Docker Hub credentials in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    credentialsId: env.GIT_CREDENTIALS_ID, 
                    url: 'https://github.com/cybe44oot/docker-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Declare dockerImage with 'def' for proper scope
                    def dockerImage = docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                    // Save it for later stages
                    env.DOCKER_IMAGE_TAG = "${env.DOCKER_IMAGE}:${env.BUILD_ID}"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', env.DOCKERHUB_CREDENTIALS_ID) {
                        docker.image(env.DOCKER_IMAGE_TAG).push()
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh """
                docker rm -f docker-flask-app || true
                docker run -d --name docker-flask-app -p 5000:5000 ${env.DOCKER_IMAGE_TAG}
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded, deployed container: '${env.DOCKER_IMAGE_TAG}'"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
