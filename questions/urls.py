from django.urls import path

from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),    
    path('add/', views.QuestionCreateView.as_view(), name='add'),    
    path('<int:pk>/add/', views.AnswerCreateView.as_view(), name='addAnswer'), 
    path('search/', views.SearchView.as_view()) 
]