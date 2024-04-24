pipeline {
    agent any 
    stages{
        stage('Stop containers'){
            steps{
                echo 'hola esta es una prueba'
                sh 'docker ps -a | grep sicei | awk \'{print $1}\' | xargs docker stop'
            }
        }
        stage('Build'){
            steps{
                
                sh 'docker build -t sicei-$GIT_BRANCH:1.0.0-$BUILD_NUMBER .'
            }
        }
        stage('Deploy'){
            steps{

                sh 'docker run -d -p 8000:8000 --name sicei-${BUILD_NUMBER} sicei-$GIT_BRANCH:1.0.0-$BUILD_NUMBER'
            }

        }
    }
}
