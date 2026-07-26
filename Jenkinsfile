// ============================================================
// Jenkins Pipeline 配置（Declarative Pipeline）
// 接口自动化测试 CI/CD 流程
// 流程：拉取代码 → 安装依赖 → 执行测试 → 生成 Allure 报告
// ============================================================

pipeline {

    // 在任何可用的 agent 上运行
    agent any

    stages {

        // Stage 1: 从 Git 仓库拉取最新代码
        stage('拉取代码') {
            steps {
                echo "拉取代码"
            }
        }

        // Stage 2: 安装 Python 项目依赖
        stage('安装依赖') {
            steps {
                bat '''
                python --version
                python -m pip --version
                python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
                '''
            }
        }

        // Stage 3: 执行 pytest 测试并生成 Allure 结果数据
        stage('执行测试') {
            steps {
                bat '''
                pytest -s --alluredir=allure-result
                '''
            }
        }
    }

    post {

        // 无论构建结果如何，始终生成并发布 Allure 报告
        always {

            allure(
                includeProperties: false,
                results: [
                    [
                        path: 'allure-result'
                    ]
                ]
            )

        }
    }
}
