from django.urls import path
from .views import ind,addFlavor,update_ing,customer_feedback,list_all
urlpatterns = [
    path('',ind,name='ind'),
    path('addflavor/',addFlavor,name='addflavor'),
    path('update_ing/',update_ing,name='update_ing'),
    path('cust_FB/',customer_feedback,name='Customer_Feedback'),
    path('list_all/', list_all, name='list_all'),
]