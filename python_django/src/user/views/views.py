import json

from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpRequest
from django.http import HttpResponse


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
    except ValueError:
        pass
    except Exception as e:
        print(e)
    finally:
        # return HttpResponse(json.dumps(response))
        pass


@csrf_exempt
def user(request, user_id):
    response = {}
    print(user_id)
    try:
        # GET /user/:id # 获取id用户的信息
        # POST /user # 创建新的用户（注册）
        # PUT /user/:id # 更新id用户的信息
        # DELETE /user/:id # 删除id用户（注销）
        if request.method == "POST":
            return HttpResponse("post")
        if request.method == "GET":
            return HttpResponse("get")
        if request.method == "PUT":
            return HttpResponse("put")
        if request.method == "DELETE":
            return HttpResponse("delete")
    except ValueError:
        pass
    except Exception as e:
        print(e)
    finally:
        # return HttpResponse(json.dumps(response))

        pass
