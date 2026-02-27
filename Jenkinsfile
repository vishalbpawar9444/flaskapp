pipeline {

    agent any

    environment {

        AWS_REGION = "ap-northeast-2"
        ECR_REGISTRY = "410003306855.dkr.ecr.ap-northeast-2.amazonaws.com"
        ECR_REPO = "project"
        IMAGE_TAG = "latest"
        IMAGE_NAME = "${ECR_REGISTRY}/${ECR_REPO}:${IMAGE_TAG}"

    }

    stages {

        stage('Clone Code') {

            steps {
                git branch: 'main',
                url: 'https://github.com/vishalbpawar9444/flaskapp.git'
            }

        }

        stage('Build Docker Image') {

            steps {
                sh 'docker build -t project:${IMAGE_TAG} .'
            }

        }

        stage('Login to ECR') {

            steps {
                sh '''
                aws ecr get-login-password --region ${AWS_REGION} | \
                docker login --username AWS --password-stdin ${ECR_REGISTRY}
                '''
            }

        }

        stage('Tag Image') {

            steps {
                sh 'docker tag project:${IMAGE_TAG} ${IMAGE_NAME}'
            }

        }

        stage('Push Image to ECR') {

            steps {
                sh 'docker push ${IMAGE_NAME}'
            }

        }

        stage('Deploy MySQL to EKS') {

            steps {
                sh '''
                kubectl apply -f k8s/mysql-deployment.yaml
                kubectl apply -f k8s/mysql-service.yaml

                kubectl rollout status deployment/mysql
                '''
            }

        }

        stage('Deploy Flask to EKS') {

            steps {
                sh '''
                kubectl set image deployment/flaskapp frontend=${IMAGE_NAME} || true

                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                kubectl rollout status deployment/flaskapp
                '''
            }

        }

        stage('Verify Deployment') {

            steps {
                sh '''
                kubectl get pods
                kubectl get svc
                '''
            }

        }

    }

    post {

        success {
            echo 'Flask + MySQL Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }

    }

}
