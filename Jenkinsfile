pipeline {

    agent any


    stages {


        stage('环境检查') {

            steps {

                bat '''
                echo Jenkins Start

                python --version

                git --version

                '''

            }

        }
        stage('执行测试') {

    steps {

        bat '''

        pytest -s --alluredir=allure-result

        '''

    }

}
        post {

            always {

                allure(
                    includeProperties:false,
                    results:[
                        [
                            path:'allure-result'
                        ]
                    ]
                )

            }

        }
    }

}