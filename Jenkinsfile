pipeline {


    agent any
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    parameters {


        choice(

            name:'TEST_ENV',

            choices:[
                'dev',
                'test',
                'prod'
            ],

            description:'选择测试环境'

        )

    }



    environment {


        ALLURE_RESULT="allure-result"


        ALLURE_REPORT="allure-report"


        PYTHON="python"


        TEST_ENV="${params.TEST_ENV}"


    }



    stages {



        stage('环境检查'){


            steps{


                bat '''

                python --version

                echo 当前环境:

                echo %TEST_ENV%

                docker --version

                docker ps

                '''


            }

        }

        stage('启动测试环境'){


            steps{


                bat '''

                echo Start Docker Environment

                docker-compose up -d

                ping 127.0.0.1 -n 6 > nul

                echo Docker Started

                '''
            }
        }

        stage('安装依赖'){


            steps{


                bat '''

                python -m pip install -r requirements.txt ^
                -i https://pypi.tuna.tsinghua.edu.cn/simple


                '''


            }

        }



        stage('执行测试'){


            steps{


                bat '''


                echo Run Test


                echo Environment:

                echo %TEST_ENV%



                pytest -s ^
                --clean-alluredir ^
                --reruns 2 ^
                --alluredir=%ALLURE_RESULT% ^
                --junitxml=test-results.xml 



                '''


            }


        }
        stage('发布测试结果'){
            steps{
                junit 'test-results.xml'
            }
        }



    }



    post{


        always{


            echo 'Generate Allure Report'


            allure(

                includeProperties:false,

                results:[

                    [

                        path:"${ALLURE_RESULT}"

                    ]

                ]

            )


            echo 'Stop Docker Environment'

                bat '''

                docker-compose down

                '''
            }



        success{


            emailext(

                subject:
                "✅测试成功 ${JOB_NAME} #${BUILD_NUMBER}",

                body:

                """

                <h2>接口自动化测试报告</h2>


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
                测试环境:
                ${TEST_ENV}
                </p>


                <p>
                执行结果:
                SUCCESS
                </p>


                <p>
                测试报告:
                <a href="${BUILD_URL}allure">
                查看Allure报告
                </a>
                </p>


                <p>
                Jenkins地址:
                <a href="${BUILD_URL}">
                查看构建详情
                </a>
                </p>


                """,
                mimeType:
                'text/html',

                to:
                "lucky2071167255@gmail.com"


            )

        }




        failure{


            emailext(

                subject:
                "❌测试失败 ${JOB_NAME} #${BUILD_NUMBER}",

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
                测试环境:
                ${TEST_ENV}
                </p>


                <p>
                状态:
                FAILURE
                </p>


                <p>
                日志:
                <a href="${BUILD_URL}console">
                查看控制台
                </a>
                </p>


                """,


                mimeType:'text/html',


                to:
                "lucky2071167255@gmail.com"


            )


        }



    }


}
