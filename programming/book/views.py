from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

@login_required
def index(request):
    data = Book.objects.all()
    return render(request,"book/index.html",{"data":data})

@login_required
def add(request):
    if request.POST:
        form =BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
        else :
            return HttpResponseRedirect("")
    else:
        form = BookForm()
        return render(request,"book/add.html",{"form":form})

@login_required
def edit(request,id):
    if request.POST:
        if request.POST:
            data = Book.objects.get(id=id)
            form = BookForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect("book")
            else :
                return HttpResponseRedirect("")
    else :
            data = Book.objects.get(id=id)
            form = BookForm(instance=data)
            return render(request, "book/edit.html", {"form": form})

@login_required
def view(request,id):
    data = Book.objects.get(id=id)
    return render(request,"book/view.html",{"data":data})

@login_required
def delete(request,id):
    item = Book.objects.get(id=id)
    item.delete()
    return redirect("/book")