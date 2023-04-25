from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
