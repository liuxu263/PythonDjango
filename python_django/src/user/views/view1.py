# coding:utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PythonDjango.python_django.config.response_code_msg import NOT_POST_METHOD_ERROR, INPUT_PARAM_EMPTY, \
    INPUT_PARAM_MISS, SUCCESS
from PythonDjango.app01.services.services import service1
import json


@csrf_exempt
def test1(request):
    res = {}
    try:
        if request.POST:
            key1 = request["key1"]
            if key1 != "":
                data = service1()
                if data:
                    res = SUCCESS
                    res["data"] = data
            else:
                raise ValueError
        else:
            res = NOT_POST_METHOD_ERROR
    except ValueError:
        res = INPUT_PARAM_EMPTY
    except KeyError:
        res = INPUT_PARAM_MISS
    finally:
        return HttpResponse(json.dumps(res, ensure_ascii=False))
