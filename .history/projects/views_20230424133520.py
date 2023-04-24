from django.shortcuts import render


def show_projects(request):
    account = Account.objects.filter(owner=request.user)
    context = {"account": account}
    return render(request, "receipts/accounts.html", context)