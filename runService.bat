@ECHO OFF

set JAVA_HOME="C:\Program Files\Java\jdk1.8.0_131"

%JAVA_HOME%\bin\java -jar -Dserver.port=8889  C:\WFDIPAL\MyLearning\TutorialExampleWorkspace\rest-webservice-demo\target\rest-webservice-demo-0.0.1-SNAPSHOT.jar
echo App stared

::-Dspring.config.location=%app_config_location%\application-dev.yaml
:: Add below to command line in case of JRebel debugging
::-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=4001 -jar -agentpath:c:\private\apps\jrebel\lib\jrebel64.dll



