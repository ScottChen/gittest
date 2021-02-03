pipeline {
  agent any
  stages {
    stage('say-hi') {
      steps {
        sh 'echo "hi nihau"'
      }
    }

    stage('add-text') {
      steps {
        writeFile(file: '1.txt', text: 'testtest', encoding: 'utf-8')
      }
    }

  }
}