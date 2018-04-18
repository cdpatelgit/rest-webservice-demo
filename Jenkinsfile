pipeline{
	agent any

	stages{
		stage('Compile Stage'){
			steps{
					sh 'mvn  -s settings.xml clean compile'
			}
		}

		stage('Test Stage'){
			steps{
					sh 'mvn -s settings.xml test'
			}
		}
	}
}