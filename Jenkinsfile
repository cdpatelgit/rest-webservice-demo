node {

    stage 'Checkout'
    checkout scm

    withEnv(["PATH=${env.PATH}:${tool 'M3'}/bin:${tool 'jdk1.8'}/bin", "JAVA_HOME=${tool 'jdk1.8'}", "MAVEN_HOME=${tool 'M3'}"]) {

        echo "JAVA_HOME=${env.JAVA_HOME}"
        echo "MAVEN_HOME=${env.MAVEN_HOME}"
        echo "PATH=${env.PATH}"

        wrap([$class: 'ConfigFileBuildWrapper', managedFiles: [
                [fileId: 'MyGlobalSettings', variable: 'MAVEN_SETTINGS']
        ]]) {
            stage 'Compile Stage'
            sh 'mvn -DskipTests -Dmaven.test.skip=true -s $MAVEN_SETTINGS clean compile'

            stage 'Test Stage'
            sh 'mvn -s $MAVEN_SETTINGS test'
        }
    }
}