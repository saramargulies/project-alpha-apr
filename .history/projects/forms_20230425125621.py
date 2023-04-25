from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.TextInput
