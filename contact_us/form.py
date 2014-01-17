


from django import forms

class ContactUsForm(forms.Form):
    name=forms.CharField()
    contact_no=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea())




print ContactUsForm()
