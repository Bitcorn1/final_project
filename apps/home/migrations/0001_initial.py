# Generated by Django 3.2.13 on 2022-09-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='uploads/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=1000)),
                ('right_ans', models.CharField(max_length=1000)),
                ('student_ans', models.CharField(max_length=1000, null=True)),
                ('similarity', models.CharField(max_length=100)),
                ('grammer_check', models.CharField(max_length=100)),
                ('keyword_sum', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='right_ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans1', models.FileField(upload_to='uploads/', verbose_name='첨부 파일1')),
            ],
        ),
        migrations.CreateModel(
            name='student_ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans2', models.FileField(upload_to='uploads/', verbose_name='첨부 파일2')),
            ],
        ),
    ]