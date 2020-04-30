from django.shortcuts import render, redirect
from .models import Todo
from .forms import AddForm
#from .forms import CompleteForm
# Create your views here.

def todo_view(request):
    if request.method == 'POST': # 리퀘스트가 포스트면?!
        form = AddForm(request.POST) # AddForm의 인스턴스 생성
        if form.is_valid(): #Form 의 형식이 유효한지 확인
            form.save() # Form 저장 후 DB에 저장   => 할일 추가하기!!



    todos = Todo.objects.all()
    form = AddForm()
    data = {
        "todos" : todos,
        "forms" : form,
    }
    return render(request, "todo_list.html", data)

def todo_inprogress_view(request):

    if request.method == 'POST': 
        form = AddForm(request.POST) 
        if form.is_valid():
            form.save()

    todos = Todo.objects.all()
    data = {
        "todos" : todos,
    }
    return render(request, "todo_inprogress.html", data)



def delete_todo(request,pk): # pk는(프라임키) 각 DB튜플의 고유번호
    target = Todo.objects.get(pk=pk)
    #Model 에서 삭제하려는 튜플 불러오기
    target.delete() # 해당 튜플을 제거
    return redirect("todos") # 다시 다른 링크를 타라! name = "todos"

def complete_todo(request,pk): 
    target = Todo.objects.get(pk=pk)
    target.delete() 
    return redirect("in_progress") 
