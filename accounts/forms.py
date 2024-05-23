from django import forms
from .models import Account



class RegistrationForm(forms.ModelForm):  # because we are using model forms we need to import the model
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }))

    class Meta:  # this is the meta class that will be used to specify the model and the fields that we want to use
        model = Account  # this is the model that we want to use
        fields = ['first_name', 'last_name', 'email','username',
                  'password']  # these are the fields that we want to use

    def __init__(self, *args,
                 **kwargs):  # this is the init method that will be used to add placeholders and classes to the fields
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        # Labels
        # self.fields['first_name'].label = 'First Name'
        # self.fields['last_name'].label = 'Last Name'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
       

    def clean(self):  # this is the clean method that will be used to check if the password and the confirm password are the same
        cleaned_data = super(RegistrationForm, self).clean()  # this line means that we are getting the data from the form
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
       

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email Address', 'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', 'class': 'form-control'
    }))
    remember_me = forms.BooleanField(label="Remember Me", required=False, initial=False, widget=forms.CheckboxInput(
        attrs={'name': 'remember_me','id': 'remember_me','class': 'form-check-input'}
    ))
        