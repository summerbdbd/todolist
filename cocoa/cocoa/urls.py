from django.contrib import admin
from django.urls import path
#from home.views import home_view, var_view, nums_view
from home.views import home_view

from todo.views import todo_view, todo_inprogress_view, delete_todo, complete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = "home"),
    #path('var/',var_view),
    #path('nums/', nums_view),
    path("todos/", todo_view, name="todos"),
    path("todos/in_progress", todo_inprogress_view, name= "in_progress"),
    path('todos/<pk>/delete', delete_todo, name = "todo_del"),
    path('todos/<pk>/complete', complete_todo, name = "todo_complete"),
    ]
