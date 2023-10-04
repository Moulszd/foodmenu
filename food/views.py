from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.



class IndexClassView(ListView): 

    # Import the necessary modules:
        # from django.views.generic import ListView
        # from .models import YourModel  # Import your model

    model = Item       # Specify the model to use
    template_name ='food/index.html'   # Specify the HTML template to use
    context_object_name ='item_list'    # Specify the context variable name for the object list


# -----------------------------------------------------------------------------------


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'item_id'  # Set the URL parameter name to 'item_id' to match the URL pattern.
 


# -----------------------------------------------------------------------------------


# Create a class-based view called CreateItem that inherits from CreateView.
class CreateItem(LoginRequiredMixin, CreateView):
    model = Item

    # Specify the form class to be used for creating new items.
    form_class = ItemForm

    # Define the HTML template to be used for rendering the form.
    template_name = 'food/item-form.html'

    # Set the success_url to redirect to the main page (index.html) after successful form submission.
    success_url = reverse_lazy('food:index')

    # Override the form_valid method to set the user_name field to the currently logged-in user.
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            # Set the user_name field to the currently logged-in user.
            form.instance.user_name = self.request.user

            # Call the parent class's form_valid method to proceed with form submission.
            return super().form_valid(form)
        else:
                # Redirect to the login page if the user is not authenticated
                return self.handle_no_permission()
        
    def handle_no_permission(self):
        # Redirect to the login page
        return redirect('users:login')
    

# -----------------------------------------------------------------------------------



# Create a class-based view called UpdateItem that inherits from UpdateView.
class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'
    # Set the name of the context variable that will hold the item object in the template
    context_object_name = 'item'
    success_url = reverse_lazy('food:index')

    # Override the get_object method to fetch the item to be updated.
    def get_object(self, queryset=None):

        # Get the item based on the 'id' URL parameter.
        return Item.objects.get(id=self.kwargs['id'])
    
    def handle_no_permission(self):
        # Redirect to the login page
        return redirect('users:login')
    
    
# -----------------------------------------------------------------------------------

# Create a class-based view called DeleteItem that inherits from DeleteView.
class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'food/item_confirm_delete.html'  # Specify the confirmation template
    # Set the name of the context variable that will hold the item object in the template
    context_object_name = 'item'
    success_url = reverse_lazy('food:index')  # Redirect to the main page after deletion

    def get_queryset(self):
    # Filter the queryset to ensure that only items owned by the current user can be deleted.
    # You might want to adjust this logic based on your specific requirements.
        return Item.objects.filter(user_name=self.request.user)

    def get_object(self, queryset=None):
        # Get the Item object to be deleted based on the URL parameter (id)
        return Item.objects.get(id=self.kwargs['id'])
    
    def handle_no_permission(self):
        # Redirect to the login page
        return redirect('users:login')