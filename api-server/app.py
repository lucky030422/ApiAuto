from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():

    data = request.json


    username = data.get("username")
    password = data.get("password")


    if username == "admin" and str(password) == "123456":

        return jsonify({

            "code":200,

            "msg":"登录成功",

            "data":{

                "token":"abc123456"

            }

        })


    else:

        return jsonify({

            "code":1001,

            "msg":"用户名或密码错误"

        })



@app.route("/user/info", methods=["GET"])
def user_info():


    token=request.headers.get(
        "Authorization"
    )


    if token=="Bearer abc123456":


        return jsonify({

            "code":200,

            "data":{

                "userId":10001,

                "username":"admin"

            }

        })


    return jsonify({

        "code":1002,

        "msg":"token无效"

    }),401



if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )