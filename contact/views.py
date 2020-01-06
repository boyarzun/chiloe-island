# Django
from django.shortcuts import render
from django.core.mail import send_mail

# Forms
from contact.forms import ContactForm

def index(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(data = request.POST)

        if form.is_valid():

            send_mail(
                form.data['subject'],
                form.data['message'],
                form.data['email'],
                ['hola@chiloeisland.net'],
                fail_silently=False,
            )

            import pdb; pdb.set_trace()


    context = {
        "form": form
    }

    return render(request, "contact/index.html", context)