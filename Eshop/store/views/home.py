from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from django.views import View



class Index(View):

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1

        request.session['cart']=cart
        return redirect('homepage')


    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
            
        products = None

        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_category_id(category_id)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, "index.html", data)



