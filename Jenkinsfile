// ============================================================
// Jenkins Pipeline
// Python接口自动化测试 CI/CD
//
// 流程:
//
// 1. 拉取GitHub代码
// 2. 检查测试环境
// 3. 安装Python依赖
// 4. 执行pytest自动化测试
// 5. 生成Allure测试报告
// 6. 邮件通知测试结果
//
// ============================================================


pipeline {


    // Jenkins执行节点
    agent any


    environment {

        // Allure结果目录
        ALLURE_RESULT = "allure-result"


        // Allure报告目录
        ALLURE_REPORT = "allure-report"


        // Python命令
        PYTHON = "python"

    }



    stages {


        // ====================================================
        // 1. 拉取代码
        // ====================================================

        stage('拉取代码') {

            steps {

                echo "========== 拉取代码成功 =========="

            }

        }



        // ====================================================
        // 2. 环境检查
        // ====================================================

        stage('环境检查') {

            steps {

                bat '''

                echo Jenkins Start


                python --version


                pip --version


                git --version


                echo Environment Check Success


                '''

            }

        }



        // ====================================================
        // 3. 安装依赖
        // ====================================================

        stage('安装依赖') {


            steps {


                bat '''

                echo Install dependency


                python -m pip install -r requirements.txt ^
                -i https://pypi.tuna.tsinghua.edu.cn/simple ^
                --timeout 60


                echo Install Success


                '''


            }


        }




        // ====================================================
        // 4. 执行接口自动化测试
        // ====================================================

        stage('执行测试') {


            steps {


                bat '''

                echo Run API Test


                pytest -s ^
                --alluredir=%ALLURE_RESULT%


                '''


            }


        }




        // ====================================================
        // 5. 测试结果
        // ====================================================

        stage('测试结果') {


            steps {


                script {


                    echo "测试执行完成"


                }


            }


        }



    }




    // ====================================================
    // 后置处理
    // ====================================================


    post {


        // -----------------------------------------
        // 无论成功失败都生成Allure报告
        // -----------------------------------------

        always {


            echo "Generate Allure Report"



            allure(


                includeProperties: false,


                results: [


                    [


                        path: "${ALLURE_RESULT}"


                    ]


                ]

            )



        }



        // -----------------------------------------
        // 测试成功邮件
        // -----------------------------------------


        success {



            emailext(


                subject:
                "✅ 接口自动化测试成功 - ${JOB_NAME} #${BUILD_NUMBER}",



                body:


                """

                <h2>接口自动化测试成功</h2>


                <hr>


                <p>
                项目:
                ${JOB_NAME}
                </p>


                <p>
                构建编号:
                ${BUILD_NUMBER}
                </p>


                <p>
                执行状态:
                SUCCESS
                </p>



                <p>
                Allure报告:
                <a href="${BUILD_URL}">
                点击查看
                </a>
                </p>



                """,



                mimeType: 'text/html',


                to:
                "lucky2071167255@gmail.com"



            )


        }





        // -----------------------------------------
        // 测试失败邮件
        // -----------------------------------------


        failure {



            emailext(


                subject:
                "❌ 接口自动化测试失败 - ${JOB_NAME} #${BUILD_NUMBER}",



                body:


                """

                <h2>
                接口自动化测试失败
                </h2>


                <hr>


                <p>
                项目:
                ${JOB_NAME}
                </p>


                <p>
                构建编号:
                ${BUILD_NUMBER}
                </p>


                <p>
                执行状态:
                FAILURE
                </p>



                <p>
                控制台日志:
                <a href="${BUILD_URL}console">
                查看日志
                </a>
                </p>



                """,



                mimeType: 'text/html',


                to:
                "lucky2071167255@gmail.com"



            )


        }



    }



}
