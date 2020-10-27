from django import forms
from django.core import validators
from main_app.models import User

class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'Input an even number', 'email']
    
    def clean(self):
        form_data = self.cleaned_data
        if form_data['Input an even number'] % 2 != 0:
            raise forms.ValidationError('That is not an even number, please try again')
        
