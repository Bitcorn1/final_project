# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Create your models here.
class Result(models.Model):
    id1=models.CharField(max_length=1000)
    right_ans = models.CharField(max_length=1000)
    student_ans  = models.CharField(max_length=1000, null=True)
    similarity  = models.CharField(max_length=100)
    grammer_check  = models.CharField(max_length=100)
    keyword_sum  = models.CharField(max_length=100)
    score = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id1) +  "," + self.right_ans + "," + self.student_ans+ "," + str(self.similarity)+"," + str(self.grammer_check)+"," + str(self.keyword_sum)+"," + str(self.score)



class Document(models.Model):
    
    uploadedFile = models.FileField(upload_to="result/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.uploadedFile)



class final_result(models.Model):
    final_result=models.FileField(upload_to="final_result/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


