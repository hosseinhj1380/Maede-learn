import user_agents.parsers
from django.views import View
from django.views.generic import  ListView,CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from .models import Cart
from .models import Course


class AddToCartView(CreateView):
    @login_required
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        cart = Cart.objects.create(user=request.user, course=course)
        cart.save()
        return redirect('cart')

class CartView(ListView):
    model = Cart
    template_name = 'cart.html'

    def get_queryset(self):
        # email_user=Cart.objects.filter(user__email='hossein@hossein.com').first()
        # user_id=Cart.objects.id
        cart_items = Cart.objects.filter(user__email='hossein@hossein.com')
        return cart_items

class RemoveFromCartView(View):
    @login_required
    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(Cart, pk=kwargs['pk'])
        cart_item.delete()
        return redirect('cart')
