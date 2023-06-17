from django import forms

from .models import *

class imageUploadingForm(forms.Form): 
    #WSDL = forms.FileField(label="Upload WSDL", help_text="Upload multiple WSDL using the 'Ctrl", widget=forms.ClearableFileInput(attrs={'multiple': True}))
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control", 'value':"Mubashir Iqbal"}) ) 
    CHOICES = [(200, "200 x 200"), (400, "400 x 400"), (600, "600 x 600")]
    choice_field = forms.CharField(label="Choose the image size", widget=forms.Select(attrs={'class': "form-control"}, choices=CHOICES ))
    image4openCV = forms.FileField(label="Upload Images", help_text="Upload multiple images using the 'Ctrl'", max_length=250,  widget=forms.TextInput(attrs={'class': "form-control", 'multiple': "True", 'type': "file",                                                            'accept': "image/*"}))



class contactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}) )
    #email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': "form-control"}) )
    #phone = forms.CharField(label='Phone', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}) )
    
    CHOICES = [(1, "200 x 300"), (2, "400 x 500"), (3, "600 x 700")]
    choice_field = forms.CharField(label="Choose the image size", widget=forms.Select(attrs={'class': "form-control"}, choices=CHOICES ))
    
    image = forms.FileField(label="Image for openCV", max_length=250, widget=forms.TextInput(attrs={'class': "form-control", 'type': "file", 'accept': "image/*"}))
    #message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': "form-control"}), max_length=1000)
    

