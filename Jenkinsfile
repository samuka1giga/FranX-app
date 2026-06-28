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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Prueba de ejecucion') {
            steps {
                sh 'python -c "from app import app; print(app)"'
            }
        }
    }
}
