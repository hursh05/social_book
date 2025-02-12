from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django import forms
from .models import UploadedFile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'public_visibility', 'birth_year', 'address']

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class BookUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['book_file', 'title', 'description', 'visibility', 'cost', 'published_year']
    
    book_file = forms.FileField(label="Upload Book (PDF/JPEG)", widget=forms.ClearableFileInput(attrs={'accept': '.pdf, .jpeg'}))
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    visibility = forms.BooleanField(initial=True, required=False)
    cost = forms.DecimalField(max_digits=10, decimal_places=2)
    published_year = forms.IntegerField()
