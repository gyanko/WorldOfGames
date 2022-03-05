pipeline {
  agent any
  environment {
      IMAGEPATH = "gyanko/world-of-games:${BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') {
      steps {
        echo 'Cloning git repo..'
        sh 'printenv | sort'
        git 'https://github.com/gyanko/WorldOfGames'
      }
    }
    stage('Build') {
      steps {
          echo 'Building container image...'
          sh 'docker-compose build'
      }
    }
    stage('Run') {
      steps {
          echo 'Running the container image...'
          echo 'Making a dummy score file'
          sh 'echo \'{ "gil" : 80}\' > dummy_scores.txt'
          sh 'docker-compose down && docker-compose up -d'
          sh 'docker-compose cp dummy_scores.txt score-server:scores.txt'
      }
    }

    stage('Test') {
      steps {
          echo 'testing the score server...'
          sh 'pip3 install -r requirements.txt'
          sh 'python3 tests/e2e.py http://localhost:8777'
      }
    }
    stage('Finalize') {
        steps {
          echo 'Uploading artifact...'
          sh 'docker-compose push'
          sh 'docker-compose down --rmi all'
    }
  }
}
}