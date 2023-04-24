from django.urls import path
from accounts.views import user_login, logout_view

# logout_view, signup_view

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", logout_view, name="logout"),
    # path("signup/", signup_view, name="signup"),
]
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                )
                login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
