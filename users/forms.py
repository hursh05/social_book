# users/forms.py
from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'public_visibility', 'age', 'birth_year', 'address']
    
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

from django import forms
from .models import UploadedFile  # Ensure this points to the correct model for file upload

from django import forms
from .models import UploadedFile  # Ensure this points to the correct model for file upload

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile  # Make sure this points to your actual file model
        fields = ['title', 'description', 'file', 'visibility', 'cost', 'year_published']  # Adjust according to your model fields

    # Optionally, you can customize the form fields if needed
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(required=True)
    visibility = forms.BooleanField(initial=True)  # Default to True
    cost = forms.DecimalField(max_digits=10, decimal_places=2)
    year_published = forms.IntegerField(required=True)
