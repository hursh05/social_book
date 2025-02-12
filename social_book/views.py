# social_book/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book  # Assuming your Book model is defined
from .forms import BookUploadForm  # Form for uploading books

@login_required
def my_books(request):
    # Fetch the books uploaded by the logged-in user
    books = Book.objects.filter(user=request.user)

    # Check if any books exist
    if books.exists():
        return render(request, 'my_books.html', {'books': books})
    else:
        return redirect('upload_books')  # Redirect to upload_books if no books

@login_required
def upload_books(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded book and associate it with the logged-in user
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('my_books')  # Redirect to "My Books" after successful upload
    else:
        form = BookUploadForm()

    return render(request, 'upload_books.html', {'form': form})
