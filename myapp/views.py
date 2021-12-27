from types import prepare_class
from django.shortcuts import redirect, render, resolve_url
from .forms import signupForm,postForm
from .models import signupMaster
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import requests
import json
import random

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")

                '''#Send Mail
                mail_sub="Account Creation Confirmation!"
                mail_msg="Hello User, \nThis is system genrated mail!\nYour account has been created successfully with us!\nHappy Coding\nThanks & Regards\n+91 9724799469 | sanketchauhanios@gmail.com"
                mail_from=settings.EMAIL_HOST_USER
                #mail_to=['sarvendalsania@gmail.com','akarshagrawal7@gmail.com','prathamsorathiya5555@gmail.com']
                mail_to=request.POST["username"]
                send_mail(mail_sub,mail_msg,mail_from,[mail_to])'''


                return redirect('home')
            else:
                print(newuser.errors)
        elif request.POST.get("signin")=="signin":

            usernm=request.POST["username"]
            passwrd=request.POST["password"]

            name=signupMaster.objects.get(username=usernm)
            print("Username:",name.firstname)
            print("UserID:",name.id)
            
            user=signupMaster.objects.filter(username=usernm,password=passwrd)
            otp=random.randint(1111,9999)
            if user:
                print("Successfully! Signin!")
                request.session["user"]=name.firstname
                userid=request.session["userid"]=name.id
                print(name)
                print(userid)

                '''#Send SMS
                # mention url
                url = "https://www.fast2sms.com/dev/bulk"

                # create a dictionary
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS',
                    
                    # Put your message here!
                    'message': f'Hello User, Your account has been login! \nYour OTP is {otp}',
                    
                    'language': 'english',
                    'route': 'p',
                    
                    # You can send sms to multiple numbers
                    # separated by comma.
                    'numbers': ''	
                }

                # create a dictionary
                headers = {
                    'authorization': 'SVMgZDu1bGawWACq4QBrKTJUl9vFct2fHOoXhep36ExyzNjLd8aJWhDwxnzyCoSlc87smBM2R3Y9KtEu',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }

                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                #load json data from source
                returned_msg = json.loads(response.text)

                # print the send message
                print(returned_msg['message'])'''

                return redirect("home")
    else:
        newuser=signupForm()
    return render(request,'index.html')


def home(request):
    user=request.session.get("user")
    if request.method=='POST':
        mypost=postForm(request.POST,request.FILES)
        if mypost.is_valid():
            mypost.save()
            print("Your post has been uploaded!")
        else:
            print(mypost.errors)
    else:
        mypost=postForm()
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect("/")

def updateprofile(request):
    user=request.session.get("user")
    userid=request.session.get("userid")
    print(f"This userid={userid}")
    stid=signupMaster.objects.get(id=userid)
    if request.method=='POST':
        updateform=signupForm(request.POST)
        if updateform.is_valid():
            updateform=signupForm(request.POST,instance=stid)
            updateform.save()
            print("Your profile has been updated!")
            return redirect('updateprofile')
        else:
            print(updateform.errors)
    else:
        updateform=signupForm()
    return render(request,'updateprofile.html',{'user':user,'userdata':signupMaster.objects.get(id=userid)})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    