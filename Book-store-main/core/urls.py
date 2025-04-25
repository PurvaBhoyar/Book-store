from django.urls import path
from . import views
from .views import AdminDashboardView, BookListView, BookCreateView
urlpatterns = [
 
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
 
     path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/books/', views.BookListView.as_view(), name='admin_book_list'),
    path('admin/books/add/', views.BookCreateView.as_view(), name='admin_book_add'),
    path('admin/books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='admin_book_edit'),
    path('admin/books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='admin_book_delete'),
    
  
    path('', views.StoreBookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.StoreBookDetailView.as_view(), name='book_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<int:book_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:book_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),

      path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/books/', BookListView.as_view(), name='admin_book_list'),
    path('admin/books/add/', BookCreateView.as_view(), name='admin_book_add'),
]
