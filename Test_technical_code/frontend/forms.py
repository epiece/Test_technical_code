from django import forms

class InputForm(forms.Form):

    InputAngka = forms.IntegerField(
        help_text = "Enter Number"
    )