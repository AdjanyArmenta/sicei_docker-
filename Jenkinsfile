pipeline {
    agent any 
    stages{
        stage('First step'){
            steps{
                echo 'hola esta es una prueba'
            }
        }
        stage('Build'){
            steps{
                
                    sh 'docker build -t sicei-$GIT_BRANCH:1.0.0-$BUILD_NUMBER .'
            }
        }
    }
}
