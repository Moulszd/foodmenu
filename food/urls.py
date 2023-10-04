from . import views
from django.urls import path


app_name = 'food' # it help django to differentialte urls between apps

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:item_id>/', views.FoodDetail.as_view(), name='detail'),
    path('add', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:id>/', views.UpdateItem.as_view(), name='update_item'),
    path('delete/<int:id>/', views.DeleteItem.as_view(), name='delete_item'),
]
