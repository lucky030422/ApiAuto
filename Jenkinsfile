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



    stages {



        stage('环境检查') {


            steps {


                bat """

                echo 当前环境:
                echo %TEST_ENV%


                python --version


                """


            }

        }




        stage('执行测试'){


            environment {


                TEST_ENV="${params.TEST_ENV}"


            }


            steps{


                bat """

                pytest -s --alluredir=allure-result


                """

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