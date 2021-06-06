from .models import AstroRegister
from django.forms import ModelForm, TextInput


class AstroRegisterForm(ModelForm):
    class Meta:
        model = AstroRegister
        fields = ["name", "mail"]
        widgets = {
            "name": TextInput(attrs={
                'placeholder':'your name'
            }),
            "mail": TextInput(attrs={
                'placeholder': 'your mail'
            }),
        }




