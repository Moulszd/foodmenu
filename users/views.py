from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages 
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# from .models import UserProfile  # Import your user profile model
from django.views.generic import DetailView





# Create your views here.



# Create a class-based view called Register that inherits from FormView.
class Register(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')  # Redirect to the main page after successful registration

    def form_valid(self, form):     # Override the form_valid method to handle form submission.
        user = form.save()         # Save the user created through the form.
        login(self.request, user)    # Log in the user.
        # Get the user's name
        user_name = user.get_full_name() or user.username

        # Create a success message that welcomes the user by their name
        success_message = f"Welcome, {user_name}! Your registration was successful."

        # Add the success message to the messages framework
        messages.success(self.request, success_message)
        return redirect(self.success_url)  # Redirect to the success URL (main page).
    


# @login_required  # Require login to access the profile page
# class ProfilePage(DetailView):
#     # model = UserProfile  # Set the model to your user profile model
#     template_name = 'users/profile.html'  # Create this template

#     # def get_object(self, queryset=None):
#     #     # Return the user profile for the currently logged-in user
#     #     return self.request.user.userprofile

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')