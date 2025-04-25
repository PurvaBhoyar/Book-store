from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, User
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords don't match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Registration successful")
        return redirect('book_list')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('book_list')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('book_list')

# Admin Views
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    login_url = '/login/'
    permission_denied_message = "You don't have permission to access this page"
    
    def test_func(self):
        return self.request.user.is_admin
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(self.login_url)
        raise PermissionDenied(self.permission_denied_message)
class BookListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Book
    template_name = 'admin/book_list.html'
    context_object_name = 'books'

class BookCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover_image', 'stock']
    template_name = 'admin/book_form.html'
    success_url = reverse_lazy('admin_book_list')

    def form_valid(self, form):
        messages.success(self.request, "Book added successfully")
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover_image', 'stock']
    template_name = 'admin/book_form.html'
    success_url = reverse_lazy('admin_book_list')

    def form_valid(self, form):
        messages.success(self.request, "Book updated successfully")
        return super().form_valid(form)

class BookDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('admin_book_list')
    template_name = 'admin/book_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Book deleted successfully")
        return super().delete(request, *args, **kwargs)

# Store Views
class StoreBookListView(ListView):
    model = Book
    template_name = 'store/book_list.html'
    context_object_name = 'books'

class StoreBookDetailView(DetailView):
    model = Book
    template_name = 'store/book_detail.html'
    context_object_name = 'book'

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = Book.objects.filter(id__in=cart.keys())
        cart_items = []
        total = 0
        
        for book in books:
            quantity = cart[str(book.id)]
            item_total = book.price * quantity
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'total': item_total
            })
            total += item_total
            
        context = {
            'cart_items': cart_items,
            'total': total
        }
        return render(request, 'store/cart.html', context)

class AddToCartView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        cart = request.session.get('cart', {})
        
        if str(book.id) in cart:
            cart[str(book.id)] += 1
        else:
            cart[str(book.id)] = 1
            
        request.session['cart'] = cart
        messages.success(request, f"{book.title} added to cart")
        return redirect('book_detail', pk=book.id)

class RemoveFromCartView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        cart = request.session.get('cart', {})
        
        if str(book.id) in cart:
            if cart[str(book.id)] > 1:
                cart[str(book.id)] -= 1
            else:
                del cart[str(book.id)]
                
        request.session['cart'] = cart
        messages.success(request, f"{book.title} removed from cart")
        return redirect('cart')
