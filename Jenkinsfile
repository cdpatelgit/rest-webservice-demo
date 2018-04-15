pipeline{
    agent any

    stages{
        stage('Compile Stage'){
        steps{
            WithMaven(maven : 'Maven-3.5.0'){
                sh 'mvn clean compile'
             }
           }
        }

        stage('Deployment Stage'){
                steps{
                    WithMaven(maven : 'Maven-3.5.0'){
                        sh 'mvn deploy'
                     }
                   }
        }
    }
}