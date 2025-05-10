from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from django.db.models import Avg
from django.contrib import messages
from .models import *

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        if password != conpassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered.")
            return render(request, 'signup.html')

        User.objects.create(name=name, email=email, contact=contact, password=password)
        messages.success(request, "User registered successfully!")

        return render(request, 'signup.html', {'show_alert': True})

    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            if user.password == password:
                request.session['email'] = user.email
                return render(request, 'signin.html', {'show_alert': True})
            else:
                messages.error(request, "Invalid email or password. Please try again.")
        except User.DoesNotExist:
            messages.warning(request, "User Does Not Exist.")

    return render(request, 'signin.html')

def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out. Visit again!")
    return render(request, 'profile.html', {'show_alert': True})

def index(request):
    dis= Book.objects.all()
    return render(request,"index.html",{'Book':dis})

def profile(request):
    if 'email' in request.session:
        email = request.session['email']
        user = get_object_or_404(User, email=email)

        if request.method == 'POST':
            
            user.city = request.POST.get('city', user.city)
            user.state = request.POST.get('state', user.state)
            user.pincode = request.POST.get('pincode', user.pincode)
            user.country = request.POST.get('country', user.country)
            user.contact = request.POST.get('contact', user.contact)
            user.save()
            messages.success(request, "Profile updated successfully!")
            
            if 'profile_image' in request.FILES:
                user.profile_image = request.FILES['profile_image']

            user.save()
            messages.success(request, "Profile updated successfully!")

            return redirect('profile')

        return render(request, 'profile.html', {'user': user})

    return redirect('signin')

def thankyou(request):
    if 'email' in request.session:
        
        return render(request, 'thankyou.html')
    
    messages.info(request, "Login First!")
    return redirect('signin')

def manage_book(request):
    if 'email' not in request.session:
        messages.info(request, "Login First!")
        return redirect('signin')
    dis= Book.objects.all()
    return render(request,"manage_book.html",{'Book':dis})

def add_book(request):
    if 'email' not in request.session:
        messages.info(request, "Login First!")
        return redirect('signin')

    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        book_price = request.POST.get('book_price')
        book_image = request.FILES.get('book_image')

        if not book_name or not book_author or not book_price or not book_image:
            messages.error(request, "All fields are required!")
            return render(request, 'add_book.html')

        try:
            Book.objects.create(
                book_name=book_name,
                book_author=book_author,
                book_price=book_price,
                book_image=book_image
            )
            
            messages.success(request, "Book added successfully!")
            return redirect('manage_book')
        except Exception as e:
            messages.error(request, f"Error adding book: {e}")
            return render(request, 'add_book.html')

    return render(request, 'add_book.html')

def delete(request,id):
    delt = get_object_or_404(Book, id=id)
    delt.delete()
    return redirect('manage_book')

def edit(request, id):
    updt = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        updt.book_name = request.POST['book_name']
        updt.book_author = request.POST['book_author']
        updt.book_price = request.POST['book_price']
        updt.book_image = request.FILES['book_image']
        updt.save()
        return redirect('manage_book')
    
    return render(request, 'add_book.html', {'action': 'update', 'Book': updt})
def add_review(request, id):
    if 'email' not in request.session:
        messages.info(request, "Login First!")
        return redirect('signin')

    email = request.session['email']
    user = get_object_or_404(User, email=email)
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book_name=book.book_name)

    if request.method == 'POST':
        book_name = request.POST['book_name']
        user_name = request.POST['user_name']
        user_profile = request.POST['user_profile']
        review_title = request.POST['review_title']
        review_description = request.POST['review_description']
        rating = request.POST['rating']

        try:
            Review.objects.create(
                book_name=book_name,
                user_name=user_name,
                user_profile=user_profile,
                review_title=review_title,
                review_description=review_description,
                rating=rating
            )
            messages.success(request, "Review added successfully!")
        except IntegrityError:
            messages.error(request, "A review from this user already exists.")
        return redirect('add_review', id=id)
    
    return render(request, 'add_review.html', {'book': book, 'user': user, 'reviews': reviews, 'star_range': range(1, 6)})