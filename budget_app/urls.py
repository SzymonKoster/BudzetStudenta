from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(),name='login'),
    path('app',views.index,name='index'),
    path('add_item',views.add_item,name='add item'),
    path('remove_item',views.remove_item,name='remove item'),
    path('edit_item',views.edit_item,name='edit item'),
    
    path('entertainment',views.entertainment_view,name="entertainment"),
    path('add_entertainment',views.add_entertainment,name='add entertainment'),
    path('remove_entertainment',views.remove_entertainment,name='remove entertainment'),
    path('edit_entertainment',views.edit_entertainment,name='edit entertainment'),

    path('study',views.study_view,name="study"),
    path('add_study',views.add_study,name='add study'),
    path('remove_study',views.remove_study,name='remove study'),
    path('edit_study',views.edit_study,name='edit study'),

    path('travel',views.travel_view,name="travel"),
    path('add_travel',views.add_travel,name='add travel'),
    path('remove_travel',views.remove_travel,name='remove travel'),
    path('edit_travel',views.edit_travel,name='edit travel'),

    path('savings',views.savings_view,name="savings"),
    path('add_savings',views.add_savings,name='add savings'),
    path('remove_savings',views.remove_savings,name='remove savings'),
    path('edit_savings',views.edit_savings,name='edit savings'),

    path('accounts/',include('django.contrib.auth.urls')),
    path('logout',views.logout_view,name='logout'),
    path('sign_up',views.sign_up,name="sign up"),
]