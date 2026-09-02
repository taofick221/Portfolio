from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactInfo
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thanks! Your message has been sent.")
        return redirect("contact")
    return render(request, "contact/contact.html", {"form": form, "contact_info": ContactInfo.objects.first()})
