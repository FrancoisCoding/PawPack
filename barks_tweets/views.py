from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Bark


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


def bark_detail_view(request, bark_id, *args, **kwargs):
    """
    REST API VIEW
    """
    data = {
        "id": bark_id,
    }
    status = 200
    try:
        obj = Bark.objects.get(id=bark_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
