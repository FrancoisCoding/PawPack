import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .forms import BarkForm
from .models import Bark


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def bark_create_view(request, *args, **kwargs):
    form = BarkForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BarkForm()
    return render(request, 'components/form.html', context={"form": form})


def bark_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    """
    qs = Bark.objects.all()
    barks_list = [{"id": x.id, "content": x.content,
                   "likes": random.randint(0, 122)} for x in qs]
    data = {
        "isUser": False,
        "response": barks_list
    }
    return JsonResponse(data)


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
