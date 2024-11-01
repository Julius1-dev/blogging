from django import forms
from .models import User

class Login_form(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class Signup_form(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

        def save(self, commit=True):
            user = super(signup_form, self).save(commit=False)
            user.username = self.cleaned_data['username']
            if commit:
                user.save()
            return user

    

