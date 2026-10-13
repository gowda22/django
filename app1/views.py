from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request, 'app1/base.html')


def about(request):
    return render(request, 'app1/about.html')


def contact(request):
    print("Request method:", request.method)

    if request.method == "POST":
        name = request.POST.get("username")
        print("Entered name:", name)

    return render(request, "app1/contact.html")



from django.shortcuts import render
from .forms import ContactForm


# from validation

def myfrom(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            print("Name:", name)
            print("Email:", email)
            print("Age:", age)
            print("Form submitted successfully")

    else:
        form = ContactForm()

    return render(request, 'app1/form.html', {'form': form})
