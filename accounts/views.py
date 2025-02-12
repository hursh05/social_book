from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView
from django_filters.views import FilterView
from .models import CustomUser
import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import BookUploadForm
from .models import UploadedFile


# Define a filter class for CustomUser model
class CustomUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            'username': ['icontains'],  # Allow searching by username (contains)
        }

# View for listing authors and sellers
class AuthorsAndSellersView(LoginRequiredMixin, FilterView, ListView):
    model = CustomUser
    template_name = 'users/authors_and_sellers.html'
    context_object_name = 'users'
    filterset_class = CustomUserFilter

    def get_queryset(self):
        return CustomUser.objects.filter(public_visibility=True)

# The Login view for authenticating users
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user with provided credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('home')  # Redirect to homepage after successful login
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('users:login')  # Redirect back to login page if credentials are invalid

    return render(request, 'users/login.html')  # Render the login page on GET request


# View to upload books
def upload_books(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:upload_books')  # Redirect back to the upload page after saving
    else:
        form = BookUploadForm()
    return render(request, 'users/upload_books.html', {'form': form})
