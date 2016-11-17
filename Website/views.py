from django.shortcuts import render
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


def lab_info(request):
    return render(request, 'Website/lab_info.html')


def home(request):
    return render(request, 'Website/Test.html')


def lab_members(request):
    return render(request, 'Website/lab_members.html')


def lab_publications(request):
    return render(request, 'Website/lab_publications.html')


def contact_form(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            your_message = request.POST.get('your_message', '')
            template = get_template('Website/contact_form.html')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'your_message': your_message,
            })

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission", content, "Burke Lab" + '', ['scottymiller9@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact_form')

        #https://hellowebapp.com/news/tutorial-setting-up-a-contact-form-with-django/

    return render(request, 'Website/contact_form.html', {'form': form_class, })
