from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	 print(args, kwargs),
	 print(request.user),
	# return HttpResponse("<h1>Hello World<h1>")
	 return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	 print(args, kwargs),
	 print(request.user),
	# return HttpResponse("<h1>Contact Page<h1>")
	 return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	 print(args, kwargs)
	 print(request.user)
	 my_context = {
              "my_text": "This is about us",
              "my_number": 1234,
              "my_list": [1232, 1123, 1213, 121323]
	 }
	 return render(request, "about.html", my_context)