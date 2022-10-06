# Generated by Django 3.2.13 on 2022-09-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_document_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='final_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_result', models.FileField(upload_to='final_result/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='right_ans',
        ),
        migrations.DeleteModel(
            name='student_ans',
        ),
    ]
