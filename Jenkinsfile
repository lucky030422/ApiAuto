pipeline {

    // 使用Jenkins节点执行
    agent any


    environment {

        // Allure结果目录
        ALLURE_RESULT = "allure-result"

    }


    stages {


        /*
         * 第一阶段
         * 环境检查
         */
        stage('环境检查') {

            steps {

                bat '''
                echo Jenkins Start

                python --version

                pip --version

                git --version

                '''

            }

        }



        /*
         * 第二阶段
         * 安装Python依赖
         */
        stage('安装依赖') {

            steps {

                bat '''

                echo Install dependency

                python -m pip install -r requirements.txt ^
                -i https://pypi.tuna.tsinghua.edu.cn/simple ^
                --timeout 60


                '''

            }

        }



        /*
         * 第三阶段
         * 执行接口自动化测试
         */
        stage('执行测试') {

            steps {

                bat '''

                echo Run pytest


                pytest -s ^
                --alluredir=%ALLURE_RESULT%


                '''

            }

        }



        /*
         * 第四阶段
         * 查看测试结果
         */
        stage('测试结果') {

            steps {

                bat '''

                dir %ALLURE_RESULT%

                '''

            }

        }


    }



    /*
     * 无论成功失败都执行
     */
    post {


        always {


            echo "Generate Allure Report"


            allure(

                includeProperties: false,

                results: [

                    [

                        path: 'allure-result'

                    ]

                ]

            )


        }



        success {

            echo "接口自动化测试成功"

        }



        failure {

            echo "接口自动化测试失败"

        }


    }


}