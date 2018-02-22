pipeline {
    agent any
    triggers {
        cron('@weekly')
    }
    stages {
        stage('Extract') {
            steps {
                echo 'Download Report..'
                sh '''
                    wget -q -O wngsr.txt http://ir.eia.gov/ngs/wngsr.txt
                    cat wngsr.txt
                '''
            }
        }
        stage('Transform') {
            steps {
                echo 'Transforming data'
                sh '''
                    grep Total wngsr.txt | awk '{print $3}' | head -1 | sed 's/,//' | tee data.txt
                '''
            }
        }
        stage('Load') {
            steps {
                echo 'Loading data into the database...'
            }
        }
        
    }
    post {
        always {
            archiveArtifacts artifacts: 'data.txt', fingerprint: true
        }
    }
}
