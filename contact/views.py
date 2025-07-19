from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def message_list_view(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'message_list.html', {'messages': messages})