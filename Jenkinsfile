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

        stage('Test Stage'){
                steps{
                    WithMaven(maven : 'Maven-3.5.0'){
                        sh 'mvn test'
                     }
                   }
        }
    }
}