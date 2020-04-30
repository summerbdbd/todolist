from django import forms
from .models import Todo
#이 모델에 맞는 폼을 만들거라서

class AddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task',) #문장만듬, 네모만든다 생각하시면 됨!
