from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
from .forms import contact_book


def contacts(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Phone = request.POST['phone']
        Email = request.POST['email']
        Address = request.POST['address']
        contactbook = Contacts(name=Name, phone=Phone, email=Email, address=Address)
        contactbook.save()
        messages.success(request, 'New contact added.')
    cont_list = Contacts.objects.all()
    return render(request, 'contact_list/contact_list.html', {'cont_list': cont_list})


def delete_contact(request, name):
    if request.method == 'POST':
        contact_name = Contacts.objects.get(name=name)
        contact_name.delete()
        return redirect('/contacts')



def update_contact(request, name):
    if request.method == 'POST':
        contact_name = Contacts.objects.get(name=name)
        temp = contact_book(request.POST, instance=contact_name)
        if temp.is_valid():
            temp.save()

    return render(request, 'contact_list/update_contact.html', {'name':name})

