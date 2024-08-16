pipeline {
    agent any

    stages {
        stage('Clonar código') {
            steps {
                git 'https://github.com/DonaldLemus/Prueba_Jenkins/tree/main'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                script {
                    // Instalar dependencias, si las hay (por ejemplo, con pip)
                    // sh 'pip install -r requirements.txt' 
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas unitarias
                    sh 'python3 -m unittest discover -s .'
                }
            }
        }
    }
}
