from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .utils import code_list

from .forms import CheckForm, ClientForm
from .models import Client


# Create your views here.

def client(request):

    model = Client.objects.all()
    form = ClientForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # for key, value in form.cleaned_data.items():
        #     print(key, value)
        form.save()
        form_full_name = form.cleaned_data.get('full_name')
        form_email = form.cleaned_data.get('email')
        form_skype_telegram = form.cleaned_data.get('skype_telegram')
        shortcode = ''.join([str(i) for i in Client.objects.values_list('shortcode').last()])
        subject = "You've been registred in FIB Lottery!"
        contact_message = "" % ( )
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email, from_email]
        some_html_message = """
        <h3>Hello, %s!!!</h3>
        <h4>You became a participant of the FIB lottery</h4>
        <h4>Your unique ID is: <u>%s</u></h4>
        <p>Contact info:</p>
        <p>Email: %s</p>
        <p>Skype/Telegram: %s</p>
        <p>Contact Us: %s</p>
		""" %(form_full_name, shortcode, form_email, form_skype_telegram, from_email)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            html_message=some_html_message,
            fail_silently=True
        )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    check_form = CheckForm(request.POST or None)
    check_text = 'Проверьте результат.'
    context = {
        'check_form': check_form,
        'model': model,
        'form': form,
        'code_list': code_list,
        'check_text': check_text
    }

    if request.method == 'POST' and check_form.is_valid():
        messages.error(request, "<h5>К сожалению вы не выиграли. Попробуйте участвовать в следующем розыгрыше!</h5>", extra_tags='html_safe')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return render(request, 'index.html', context)