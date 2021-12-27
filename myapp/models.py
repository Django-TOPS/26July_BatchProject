from django.db import models

# Create your models here.


class signupMaster(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField(max_length=6)


class uploadPost(models.Model):
    title=models.CharField(max_length=200)
    cate=models.CharField(max_length=50)
    myfile=models.FileField(upload_to='MyFiles')
    comments=models.TextField()