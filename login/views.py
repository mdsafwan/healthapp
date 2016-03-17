from django.shortcuts import render
from twilio.rest import TwilioRestClient
from django.http.response import HttpResponse, HttpResponseRedirect,\
    JsonResponse
from login.models import patient_details, doc_prescription, doctor_details
import datetime
import urllib, simplejson, json

# Your Account Sid and Auth Token from twilio.com/user/account
def sendsms(request):
    account_sid = "ACb7185c76aece47e1ccddd493d0acf03e"
    auth_token  = "7adcea2bf12f828d3d34d1828a4baf25"
    client = TwilioRestClient(account_sid, auth_token)
    
    message = client.messages.create(
        body="",
        to="+917259702969",
        from_="+17162613345",
        media_url="https://www.google.co.in/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    print message.sid       
    call = client.calls.create(to="+917259702969",  # Any phone number
                           from_="+17162613345", # Must be a valid Twilio number
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    print call.sid
    return HttpResponse('sent!')

def login_doctor(request):
    if request.POST:
        name = request.POST.get('username')
        password = request.POST.get('password')
        x = doctor_details.objects.filter(Name=name,
                                       Password=password).last()
        if x is None:
            return HttpResponseRedirect('/login_doctor/')
        else:
            return HttpResponseRedirect('/dashboard/?U=D')
         
        
    return render(request, "doc-login.html", {})

def login_patient(request):
    if request.POST:
        name = request.POST.get('username')
        password = request.POST.get('password')
        x = patient_details.objects.filter(Name=name,
                                       Password=password).last()
        if x is None:
            return HttpResponseRedirect('/login_patient/')
        else:
            return HttpResponseRedirect('/dashboard/?U=P')
        
    return render(request, "patient-login.html", {})

def register(request):
    if request.POST:
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_again = request.POST.get('password-again')
        option = request.POST.get('option', None)
        if option == '1':
            patient_details.objects.create(Name = name,
                                           Email = email,
                                           Password = password)
        if option == '2':
            doctor_details.objects.create(Name = name,
                                           Email = email,
                                           Password = password)
    return render(request, "user-register.html", {})

def prescription(request):
    if request.POST:
        name = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        date = request.POST.get('date')
        date = datetime.datetime.now()
        number = request.POST.get('number')
        diagnosis = request.POST.get('diag')
        remedies = request.POST.get('remedies')
#         print date
#         return HttpResponse("hello")
#         print remedies
#         return HttpResponse("ji")
        doc_prescription.objects.create(Name = name,
                                        Age = age,
                                        Email = email,
                                        Number = number,
                                        Date = date,
                                        Diagnosis = diagnosis,
                                        Remedies = remedies,
                                        )
        x = patient_details.objects.filter(Email=email).last()
        
        account_sid = "ACb7185c76aece47e1ccddd493d0acf03e"
        auth_token  = "7adcea2bf12f828d3d34d1828a4baf25"
        client = TwilioRestClient(account_sid, auth_token)
        
        d = "\nPATIENT NAME: " + name + "\nDIAGNOSIS: " + diagnosis
        r = "\nREMEDIES: " + remedies
        m = d + r
        message = client.messages.create(
            body= m,
            to="+917259702969",
            from_="+17162613345",
            media_url="https://www.google.co.in/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
        print message.sid
        
        return HttpResponseRedirect('/dashboard/?U=D') 
    return render(request, "prescrip.html", {})

def dashboard(request):
    if request.GET:
        user = request.GET.get('U')
        url = "https://content.guardianapis.com/search?q=%28disease%20OR%20virus%20OR%20epidemic%29%20&api-key=test"
#     url = url + '.json'

        response = urllib.urlopen(url)
        interm = json.load(response)
    #     print interm["response"]["results"][0]
    
        list1 = []
        list2 = []
        x = interm["response"]["results"]
        for y in x:
            for z in y:
                if z=="webTitle":
                    list1.append(y[z])
                if z=="webUrl":
                    list2.append(y[z])
    #     print list
    #     print type(x)
    #     return HttpResponse("hi")
        list = zip(list1, list2)
        
        if user == 'P':
            return render(request, "dashboard.html", {'user': user,
                                                      'abc' : list})
        else:
            return render(request, "dashboard.html", {'user': user,
                                                      'abc' : list})
    else:
        return HttpResponseRedirect('/login_patient/')
    
def panic(request):
    return render(request, "panic.html", {})

def sendpanic(request):
    account_sid = "ACb7185c76aece47e1ccddd493d0acf03e"
    auth_token  = "7adcea2bf12f828d3d34d1828a4baf25"
    client = TwilioRestClient(account_sid, auth_token)
    
    message = client.messages.create(
        body="YOUR FRIEND NEEDS URGENT HELP!",
        to="+917259702969",
        from_="+17162613345",
        media_url="https://www.google.co.in/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    print message.sid
    return HttpResponseRedirect('/dashboard/?U=P')

def newsfeed(request):
    url = "https://content.guardianapis.com/search?q=%28disease%20OR%20virus%20OR%20epidemic%29%20&api-key=test"
#     url = url + '.json'

    response = urllib.urlopen(url)
    interm = json.load(response)
#     print interm["response"]["results"][0]

    list1 = []
    list2 = []
    x = interm["response"]["results"]
    for y in x:
        for z in y:
            if z=="webTitle":
                list1.append(y[z])
            if z=="webUrl":
                list2.append(y[z])
#     print list
#     print type(x)
#     return HttpResponse("hi")
    list = zip(list1, list2)
    return render(request, "newsfeed.html", {'abc': list})