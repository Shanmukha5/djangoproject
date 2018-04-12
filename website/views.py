from django.shortcuts import render, HttpResponse
from .forms import ContactForm

def base(request):
	return render(request,'base.html')

def about(request):
	return render(request,'about.html')


def services(request):
	return render(request,'services.html')

def products(request):
	return render(request,'products.html')

def blog(request):
	return render(request,'blog.html')

def hiring(request):
	return render(request,'hiring.html')



def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'base.html',{'form':form})
		else:
			form = ContactForm()
	return render(request,'contact.html',{'form':form})



