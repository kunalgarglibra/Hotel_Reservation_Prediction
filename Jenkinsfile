pipeline{
    agent any


    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/kunalgarglibra/Hotel_Reservation_Prediction.git']])
                }
            }
        }
    }
        
}