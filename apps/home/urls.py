# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from apps.home import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include,re_path  # add this
from django.conf.urls.static import static



urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("uploadFile/", views.uploadFile, name="uploadFile"),
    # path('modeling/',views.modeling,name='modeling'),
    path('model/',views.csvtomodel,name='model'),
    path("final/", views.final, name="final"),
    path("download/", views.downloadFile, name="downloadFile"),
  

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )