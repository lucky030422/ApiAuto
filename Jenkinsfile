pipeline {


    agent any


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


            step{


                bat '''

                echo Start Docker Environment

                docker-compose up -d

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
                --alluredir=%ALLURE_RESULT%



                '''


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

                docker compose down

                '''
            }



        success{


            emailext(

                subject:
                "✅测试成功 ${JOB_NAME} #${BUILD_NUMBER}",


                body:
                """

                项目:
                ${JOB_NAME}


                环境:
                ${TEST_ENV}


                状态:
                SUCCESS


                Allure:
                ${BUILD_URL}


                """,


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

                项目:
                ${JOB_NAME}


                环境:
                ${TEST_ENV}


                状态:
                FAILURE


                日志:
                ${BUILD_URL}console


                """,


                to:
                "lucky2071167255@gmail.com"


            )


        }



    }


}
