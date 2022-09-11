from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01.static.utils.sendMsg import send


# Create your views here.
@csrf_exempt
def notice(request):
    if request.method == "GET":
        return render(request, 'notice.html')
    print(request.POST.get("map_id"))
    print(request.POST.get("p_x"))
    print(request.POST.get("p_y"))
    print(request.POST.get("start_time"))
    print(request.POST.get("finish_time"))
    map_id = request.POST.get("map_id")
    p_x = request.POST.get("p_x")
    p_y = request.POST.get("p_y")
    start_time = request.POST.get("start_time")
    finish_time = request.POST.get("finish_time")
    send(map_id, p_x, p_y, start_time, finish_time)
    return HttpResponse("success")
