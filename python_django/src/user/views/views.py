import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from python_django.config.response_code_msg import ERROR_REQUEST_METHOD
from python_django.config.response_code_msg import ERROR_PARAM
from python_django.config.response_code_msg import ERROR_DATA
from python_django.config.response_code_msg import SUCCESS

from ..services import services1


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
            env = request.POST.get["env"]
            data = services1.service1_select(env)
            if data:
                response = SUCCESS
                response["data"] = data
            else:
                raise ValueError
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
        # GET /user1/:id # 获取id用户的信息
        # POST /user1 # 创建新的用户（注册）
        # PUT /user1/:id # 更新id用户的信息
        # DELETE /user1/:id # 删除id用户（注销）
        if request.method == "GET":
            if not user_id:
                raise KeyError
            env = request.POST.get["env"]
            data = services1.service1_select(env)
            if data:
                response["data"] = data
            else:
                raise ValueError
        elif request.method == "POST":
            if not user_id:
                raise KeyError
            env = request.POST["env"]
            data = services1.service1_update(env)
            if data:
                response["data"] = data
            else:
                raise ValueError
        elif request.method == "PUT":
            if not user_id:
                raise KeyError
            env = request.POST["env"]
            data = services1.service1_insert(env)
            if data:
                response["data"] = data
            else:
                raise ValueError
        elif request.method == "DELETE":
            if not user_id:
                raise KeyError
            env = request.POST["env"]
            data = services1.service1_delete(env)
            if data:
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
