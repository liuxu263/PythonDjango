import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import QueryDict

from python_django.config.response_code_msg import ERROR_REQUEST_METHOD
from python_django.config.response_code_msg import ERROR_PARAM
from python_django.config.response_code_msg import ERROR_DATA
from python_django.config.response_code_msg import SUCCESS
from ..services import services1
from ..forms import forms1


# from ..services import services4


# Create your views here.

@csrf_exempt
def hello_world(request):
    return HttpResponse("hello world")


@csrf_exempt
def session(request):
    response = {}
    try:
        # GET /session # 获取会话信息
        # POST /session # 创建新的会话（登入）
        # PUT /session # 更新会话信息
        # DELETE /session # 销毁当前会话（登出）
        if request.method == "POST":
            return HttpResponse("post")
        if request.method == "GET":
            return HttpResponse("get")
        if request.method == "PUT":
            return HttpResponse("put")
        if request.method == "DELETE":
            return HttpResponse("delete")
        else:
            response = ERROR_REQUEST_METHOD
    except ValueError:
        response = ERROR_DATA
    except KeyError:
        response = ERROR_PARAM
    finally:
        return HttpResponse(json.dumps(response, ensure_ascii=False))


@csrf_exempt
def user(request, user_id):
    response = {}
    try:
        # GET /user/:id # 获取id用户的信息
        if request.method == "GET":
            env = request.GET["env"]
            forms1.is_empty({"env": env, "user_id": user_id})
            services1.services_is_user(env, user_id)
            data = services1.service1_get_user(env, user_id)
            if data:
                response = SUCCESS
                response["data"] = data
            else:
                raise ValueError
        # POST /user # 创建新的用户（注册）
        elif request.method == "POST":
            env = request.POST["env"]
            password = request.POST["password"]
            username = request.POST["username"]
            email = request.POST["email"]
            create_time = request.POST["create_time"]
            if not env or not user_id or not password or not username or not email or not create_time:
                raise KeyError
            data = services1.service1_create_user(env, user_id, password, username, email, create_time)
            if data:
                response = SUCCESS
                response["data"] = data
            else:
                raise ValueError
        # PUT /user/:id # 更新id用户的信息
        elif request.method == "PUT":
            put = QueryDict(request.body)
            env = put.get("env")
            password = put.get("password")
            username = put.get("username")
            email = put.get("email")
            create_time = put.get("create_time")
            if not env or not user_id or not password or not username or not email or not create_time:
                raise KeyError
            if user_id != services1.service1_get_user_id(env, user_id):
                raise KeyError
            data = services1.service1_update_user(env, user_id, password, username, email, create_time)
            if data:
                response = SUCCESS
                response["data"] = data
            else:
                raise ValueError
        # DELETE /user/:id # 删除id用户（注销）
        elif request.method == "DELETE":
            delete = QueryDict(request.body)
            env = delete.get("env")
            if not env or not user_id:
                raise KeyError
            if user_id != services1.service1_get_user_id(env, user_id):
                raise KeyError
            data = services1.service1_delete_user(env, user_id)
            if data:
                response = SUCCESS
                response["data"] = data
            else:
                raise ValueError
        else:
            response = ERROR_REQUEST_METHOD
    except ValueError:
        response = ERROR_DATA
    except KeyError:
        response = ERROR_PARAM
    finally:
        return HttpResponse(json.dumps(response, ensure_ascii=False))
