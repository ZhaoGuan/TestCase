from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from to_yaml.models import Attributes, Elements, TypeAttribute, Recording
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@require_http_methods(["GET", "OPTIONS"])
def test(request):
    return JsonResponse({"code": 20000})


@require_http_methods(["POST", "OPTIONS"])
def add_attribute(request):
    request_json = json.loads(request.body)
    info = request_json["info"]
    if len(Attributes.objects.filter(info=info)) > 0:
        return JsonResponse({"code": 50000, "message": "已经存在该属性"})
    else:
        attribute = Attributes.objects.create(info=info)
    return JsonResponse({"code": 20000})


@require_http_methods(["GET", "OPTIONS"])
def get_attributes(request):
    data = []
    for object in Attributes.objects.all():
        data.append({"id": object.id, "info": object.info})
    return JsonResponse({"code": 20000, "data": data})


@require_http_methods(["GET", "OPTIONS"])
def del_attributes(request):
    info = request.GET.get("info")
    if "info" is None:
        return JsonResponse({"code": 50000, "message": "缺少参数info"})
    del_info = Attributes.objects.filter(info=info)
    del_info.delete()
    return JsonResponse({"code": 20000})


@require_http_methods(["POST", "OPTIONS"])
def create_element(request):
    name = json.loads(request.body)["name"]
    attribute_list = json.loads(request.body)["attribute_list"]
    attribute_ids = [i["id"] for i in attribute_list]
    if len(Elements.objects.filter(name=name)) > 0:
        return JsonResponse({"code": 50000, "message": "已经存在该元素"})
    else:
        element = Elements.objects.create(name=name)
        element_id = element.id
        for attribute_id in attribute_ids:
            TypeAttribute.objects.create(element_id=element_id, attribute_id=attribute_id)
    return JsonResponse({"code": 20000})


@require_http_methods(["GET", "OPTIONS"])
def get_elements_info(request):
    data = []
    elements = Elements.objects.all()
    for element in elements:
        element_id = element.id
        element_name = element.name
        temp_attribute = []
        for i in TypeAttribute.objects.filter(element_id=element_id):
            attribute = Attributes.objects.get(id=i.attribute_id)
            temp_attribute.append({"info": attribute.info})
        data.append({"id": element_id, "name": element_name, "attribute_list": temp_attribute})
    return JsonResponse({"code": 20000, "data": data})


@require_http_methods(["GET", "OPTIONS"])
def del_element(request):
    info = request.GET.get("id")
    if "info" is None:
        return JsonResponse({"code": 50000, "message": "缺少参数id"})
    del_info = Elements.objects.filter(id=info)
    del_info.delete()
    return JsonResponse({"code": 20000})


@require_http_methods(["POST", "OPTIONS"])
def recording(request):
    request_json = json.loads(request.body)
    test_case = request_json["pathName"]
    executor = request_json["executor"]
    result = request_json["result"]
    message = request_json["message"]
    if executor == "":
        return JsonResponse({"code": 50000, "msg": "未正确填写执行用户名称！"})
    Recording.objects.create(test_case=test_case, executor=executor, result=result, message=message)
    return JsonResponse({"code": 20000})
