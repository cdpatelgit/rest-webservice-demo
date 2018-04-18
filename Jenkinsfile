pipeline{
	agent any

	stages{
		stage('Compile Stage'){
			steps{
				WithMaven(mavenSettingsConfig: 'MyGlobalSettings', mavenInstallation: 'M3', jdk: 'jdk1.8'){
					sh 'mvn  -s settings.xml clean compile'
				}
			}
		}

		stage('Test Stage'){
			steps{
				WithMaven(mavenSettingsConfig: 'MyGlobalSettings', mavenInstallation: 'M3', jdk: 'jdk1.8'){
					sh 'mvn test'
				}
			}
		}
	}
}