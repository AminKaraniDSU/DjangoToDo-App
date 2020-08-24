from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST, None)
        if form.is_valid():
            form.save()
            allItem = List.objects.all
            messages.success(request,("Item has been aded to list"))
            # return redirect(request, 'home.html', {'all_item': allItem})
            return redirect('home')
    else:
        allItem = List.objects.all
        return render(request, 'home.html',{'all_item':allItem})
def about(request):
    myname = 'Amin'
    return render(request, 'about.html', {'name':myname})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item has been delete from the list"))
    return redirect('home')

def Uncrouss(request,list_id):
    item = List.objects.get(pk=list_id)
    item.complete = False
    item.save()
    messages.success(request,("Item has been Uncrouss"))
    return redirect('home')

def Croussoff(request,list_id):
    item = List.objects.get(pk=list_id)
    print(item)
    item.complete = True
    item.save()
    messages.success(request,("Item has been Crossed off"))
    return redirect('home')

def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST, None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item has been Edited"))
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


