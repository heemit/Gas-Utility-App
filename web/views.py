from django.contrib.auth            import get_user_model
from django.shortcuts               import render, redirect, get_object_or_404
from django.contrib.auth            import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers    import make_password
from django.contrib.auth.models     import AnonymousUser
from django.contrib                 import messages
from .models                        import ServiceRequest

# Use get_user_model() to get the custom User model
User = get_user_model()

# User Registration
def user_register(request):
    if request.method == "POST":
        username    = request.POST["username"]
        email       = request.POST["email"]
        password    = request.POST["password"]
        first_name  = request.POST["first_name"]
        last_name   = request.POST["last_name"]
        phone       = request.POST["phone"]
        address     = request.POST["address"]
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')  # Redirect back to register page

        # Create the user
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            password=make_password(password)  # Hash password before saving
        )

        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')  # Redirect to the login page

    return render(request, 'web/register.html')

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'web/login.html')

# User Logout
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')  # Redirect to login page after logout

# Frontend views
def index(request):
    return render(request, 'web/index.html')

def dashboard(request):
    if isinstance(request.user, AnonymousUser):
        return redirect('login')

    # Get all service requests for the logged-in user
    service_requests = ServiceRequest.objects.filter(user=request.user)

    return render(request, 'web/dashboard.html', {'service_requests': service_requests})

def login_page(request):
    return render(request, 'web/login.html')

def register_page(request):
    return render(request, 'web/register.html')

@login_required
def create_request_page(request):
    if request.method == "POST":
        # Get form data from the POST request
        request_type    = request.POST.get("request_type")
        description     = request.POST.get("description")
        attachment      = request.FILES.get("attachment")

        # Check if the request_type and description are provided
        if not request_type or not description:
            messages.error(request, "Both request type and description are required.")
            return redirect('create_request')

        # Create a new ServiceRequest
        service_request = ServiceRequest.objects.create(
            user=request.user,
            request_type=request_type,
            description=description,
            attachment=attachment,
            status='pending',  # Default status
        )

        # Save the request to the database
        service_request.save()

        messages.success(request, "Service request created successfully!")
        return redirect('dashboard')  # Redirect to the dashboard

    return render(request, 'web/create_request.html')

@login_required
def track_request_page(request, id):
    # Fetch the service request based on the ID
    service_request = get_object_or_404(ServiceRequest, id=id)

    return render(request, 'web/track_request.html', {'service_request': service_request})

@login_required
def account_info(request):
    if request.method == "POST":
        # Fetch the current user
        user = request.user

        # Get the updated fields from the POST request
        first_name  = request.POST.get('first_name')
        last_name   = request.POST.get('last_name')
        phone       = request.POST.get('phone')
        email       = request.POST.get('email')
        address     = request.POST.get('address')
        username    = request.POST.get('username')
        password    = request.POST.get('password')

        # Update the user's details
        user.first_name = first_name
        user.last_name  = last_name
        user.phone      = phone
        user.email      = email
        user.address    = address
        user.username   = username

        # Only update password if it's provided
        if password:
            user.set_password(password)  # Use set_password to hash the password

        user.save()

        messages.success(request, "Account information updated successfully.")
        return redirect('account_info')

    return render(request, 'web/account_info.html', {"user": request.user})