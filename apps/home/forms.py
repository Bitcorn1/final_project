from django import forms
from .models import right_ans
from .models import student_ans
from django.forms import ModelForm



class right_ansForm(forms.ModelForm):
    upload = forms.FileField(label='첨부 파일1', required=False, 
          widget=forms.FileInput(attrs={'class': 'form'}))
    
    class Meta:
        model = right_ans
        exclude = ['attached']

class student_ansForm(forms.ModelForm):
    upload = forms.FileField(label='첨부 파일2', required=False, 
          widget=forms.FileInput(attrs={'class': 'form'}))
    
    class Meta:
        model = student_ans
        exclude = ['attached']



class FileUploadForm(ModelForm):
    class Meta:
        model = right_ans
        fields = ['ans1']