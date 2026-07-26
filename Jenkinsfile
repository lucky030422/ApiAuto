pipeline {


    agent any


    stages {


        stage('拉取代码') {

            steps {

                echo "拉取代码"

            }

        }


        stage('安装依赖') {

            steps {

                bat '''
                pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
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