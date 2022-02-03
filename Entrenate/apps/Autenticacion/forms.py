from django import forms

class login_form(forms.Form):
    email = forms.EmailField(
            max_length=100,
            label='Email',
            widget=forms.EmailInput(
                attrs={'class':'form-control', 'placeholder':'Email'}
                )
            )
    password = forms.CharField(
            max_length=100,
            label='Password',
            widget=forms.PasswordInput(
                attrs={'class':'form-control', 'placeholder':'Password'}
                )
            )
