# Django
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse

# Forms
from contact.forms import ContactForm
from settings.models import Setting

def index(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(data = request.POST)

        if form.is_valid():

            setting = Setting.objects.get(pk=1)

            email = EmailMessage(
                subject = form.data['subject'],
                body = form.data['message'],
                from_email = setting.email,
                to = [setting.email],
                reply_to = [form.data['email']]
            )
            try:
                email.send()
                message_response = 'Mensaje enviado! Te contactaremos lo más pronto posible ;)'
                type_respose = 'success'

            except ValueError:
                message_response = 'Oops! Algo salio mal, intentalo más tarde :P'
                type_respose = 'danger'


            return JsonResponse({
                'message': message_response,
                'type': type_respose
            })

    context = {
        "form": form
    }

    return render(request, "contact/index.html", context)