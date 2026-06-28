pipeline {
    agent any
    stages {
        stage('Clonar') {
            steps {
                checkout scm
            }
        }
        stage('Instalar dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Prueba de ejecucion') {
            steps {
                sh 'python3 -c "from app import app; print(app)"'
            }
        }
    }
}
