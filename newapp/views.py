from django.shortcuts import render,redirect
from newapp.models import signup,hm
from.import forms
from.forms import signupform
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    if request.method == "POST":
         kname = request.POST.get("name")
         kemail = request.POST.get("email")
         kcontact = request.POST.get("contact")
         kdestination = request.POST.get("destination")
         data = hm(name=kname, email=kemail, contactt = kcontact, destination = kdestination)
         data.save()
        #  messages.success(request, "Thanks for contacting us. We will get back to you soon!")

        #  return redirect('/#surveyForm')
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def guide(request):
    return render(request,"guide.html")
def destination(request):
    return render(request,"destination.html")
def contact(request):
        context = {}
        if request.method == "POST":
             
             address = "pandeyketan111@gmail.com"
             fname = request.POST.get('name')
             femail = request.POST.get('email')
             fsub = request.POST.get('subject')
             fmessage = request.POST.get('message')
             fmessage = "HI "+ fname + " " + femail + " " + fmessage 
             query = signup(name=fname, emailid=femail, subject=fsub, messages = fmessage)
             query.save()
             messages.success(request, "Thanks for contacting us. We will get back to you soon!")
             if address and fsub and fmessage:
                try:
                    send_mail(fsub, fmessage, settings.EMAIL_HOST_USER, [address])
                    context['result'] = 'Email sent successfully'
                except Exception as e:
                    context['result'] = f'Error sending email: {e}'
             else:
                    context['result'] = 'All fields are required'

                    return redirect('/contact/')

        return render(request,'contact.html',context)
# def mcontact(request):
#     if request.method == "POST":
#         fname = request.POST.get('name')
#         femail = request.POST.get('email')
#        # fphoneno = request.POST.get('num')

        
        
#         query = signup(name=fname, emailid=femail)
#         query.save()
#         messages.success(request, "Thanks for contacting us. We will get back to you soon!")

#         return redirect('/contact/')

#     return render(request, 'contact.html')

# def contact(request):
#     if request.method == "POST":
#         name = request.POST('name')
#         email = request.POST('emailid')
#         contact = request.POST('contact')
#         ed = signup(name=name,emailid=email,contact=contact)
#         ed.save()
#         messages.success(request, "Thanks for contacting us. We will get back to you soon!")
#         return redirect('/contact/')
#     return render(request,'contact.html')
 
# def signupme(request):
#     if request.method == "POST":
#         name = request.POST('name')
#         emailid = request.POST('email')
#         contact = request.POST('contact')
#         ed = signup(name=name,email=emailid,contact=contact)
#         ed.save()
#         messages.success(request, "Thanks for contacting us. We will get back to you soon!")
#         return redirect('index.html')
#     return render(request,'index.html')
 
