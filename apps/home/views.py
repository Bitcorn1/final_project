# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from final import get_similarity, sbert_final
from django.shortcuts import render, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
import csv
import os
from django.conf import settings
from . import models
import pandas as pd
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
import numpy
import time

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def csvtomodel(request):
    path='C:/Users/Admin/Desktop/django1/final_score_q1.csv'
    file=open(path)
    reader = csv.reader(file)
    print('-----',reader)
    list=[]
    for row in reader:
        list.append(Result( id1=row[0],
                            right_ans=row[1],
                            student_ans=row[2],
                            similarity=row[3],
                            grammer_check=row[4],
                            keyword_sum=row[5],
                            score=row[6]

        ))
    Result.objects.bulk_create(list)
    return HttpResponse('creat modell ~~')

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
       
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            
            uploadedFile=uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "home/auto.html", context={
        "files": documents
    })



def final(request):
    
    # print(Document.objects.latest('id'))
    document = Document.objects.values_list()
    # print(document)
    print(list(document)[-1])
    print(list(document)[-1][1])
    a=list(document)[-1][1]
    b=list(document)[-2][1]
    # document_list = []
    # for item in document:
    #     asdf = str(document.)
    #     document_list.append(asdf)
    # print(document_list[-1])    
    # time.sleep(777)
    df_right_answers = pd.read_csv('media/' + b,index_col=0)
    q_pd = pd.read_csv('media/'+a,index_col=0)
    sbert_final(df_right_answers, q_pd)
    
    
    context = {'query_set': 'query_set'}
    html_template = loader.get_template('home/result.html')

    return HttpResponse(html_template.render(context, request))


def downloadFile(request):
    # path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, 'final_score_q1.csv')
    
    print(file_path)
    # C:\Users\Admin\Desktop\django-datta-able-master_html\django-datta-able-master\media\final_score_q1.csv
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '알 수 없는 오류가 발행하였습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")

   
