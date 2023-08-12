from turtle import title
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import contactForm
from enquiry.models import Enquiry
from django.core.mail import EmailMultiAlternatives, send_mail
import datetime
from webservice.models import WebService
from projects.models import Projects
from sociallink.models import SocialLink

def contactUs(request):
    fn = contactForm()
    data = {
        'total': '',
        'form': fn,
    }
    if request.method == 'GET':
        output = request.GET.get('output')
        data = {
            'total': '',
            'form': fn,
        }
    return render(request, "contactus.html", data)

def saveEnquiry(request):
    fn = contactForm()
    data = {
        'total': '',
        'form':fn
    }

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        en = Enquiry(fname=fname,lname=lname,email=email,phone=phone,message=message)
        en.save()

        subject = "New Enquiry Submitted"
        froms = 'arijit.wizkraft@gmail.com'
        msg = 'This is a enquiry email from <b>Django website using EmailAlternatives</b>.<br><h3>Name:</h3> '+fname+'<br><h3>Email:</h3> '+email+'<br><h3>Phone:</h3> '+phone+'<br><h3>Message:</h3> '+message+'<br>'
        to = 'arijitsamaddar21@gmail.com'
        msgs = EmailMultiAlternatives(subject,msg,email,[to])
        msgs.content_subtype='html'
        msgs.send()

    return render(request,"contactus.html", data)

def homPage(request):
    fn = contactForm()
    today = datetime.date.today()
    year = today.year

    #Order by Ascending and Limit using list Slicing method of Python
    # serviceData = WebService.objects.all().order_by('service_title')[:3]
    serviceData = WebService.objects.all().order_by('service_title')

    projectData = Projects.objects.all()

    footerData = SocialLink.objects.all()

    data = {
        'title':'Home',
        'form': fn,
        'year': year,
        'serviceData' : serviceData,
        'projectData' : projectData,
        'footerData' : footerData
    }
    return render(request, "index.html", data)