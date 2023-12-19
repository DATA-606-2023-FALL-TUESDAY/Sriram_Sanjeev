from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('UserLogin', views.UserLogin, name="UserLogin"),
	       path('UserLoginAction', views.UserLoginAction, name="UserLoginAction"),	   
	       path('Predict', views.Predict, name="Predict"),
	       path('PredictAction', views.PredictAction, name="PredictAction"),	
	       path('Aboutus', views.Aboutus, name="Aboutus"),	       
]
