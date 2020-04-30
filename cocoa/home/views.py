#home/views.py
from django.shortcuts import render
from django.http import HttpResponse

#def home_view(request):
#    return HttpResponse("<p>Hello World!</p>")
def home_view(request):
     return render(request, "index.html", {})



# def var_view(request) :
#     num = 10
#     return render(request, "var.html", {"num":num})
# def nums_view(request):
#     nums = [1, 2, 3, 4 ,5]
#     return render(request, "nums.html", {"nums":nums})

# def even_num_view(request):
#     nums = [1, 2, 3, 4, 5]
#     return render(request, "nums.html", {"nums":nums})
    