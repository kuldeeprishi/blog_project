from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput
    email=forms.EmailField()
    first_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)



    
    
    
    
    

