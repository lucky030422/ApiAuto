pipeline {

    agent any


    stages {


        stage('测试环境') {

            steps {

                bat '''
                echo Jenkins测试开始

                whoami

                cd

                python --version

                echo Jenkins测试结束
                '''

            }

        }


    }

}