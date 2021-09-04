from django.shortcuts import render, redirect
from django.contrib.auth.hashers import  make_password, check_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')

        value = {

            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email

        }

        # validation

        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)

        error_message = self.customer_validation(customer)

        # saving

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:

            data = {

                'error': error_message,
                'values': value
            }

            return render(request, 'signup.html', data)

    def customer_validation(self, customer):
        error_message  =None;
        if(not customer.first_name):
            error_message = "First Name required !!"
        elif len(customer.first_name) < 3:
            error_messag  ="First Name should consist of minimum 3 characters"
        elif not customer.last_name:
            error_message = "Last Name required !!"
        elif len(customer.last_name) < 3:
            error_message = "Last Name should consist of minimum 3 characters"
        elif not customer.phone:
            error_message = "Phone Number required !!"
        elif len(customer.phone) < 11:
            error_message = "Phone Number should consist of minimum 11 characters"
        elif len(customer.phone) > 14:
            error_message = "Phone Number should consist of maximum 14 characters"
        elif len(customer.email) < 5:
            error_message = "Email should consist of minimum 3 characters"
        elif(not customer.password):
            error_message = "Password required !!"
        elif len(customer.password) < 5:
            error_message = "Password should consist of minimum 5 characters"
        elif customer.isExists():
            error_messag  ="Email is already Registered"


        return error_message;

        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # validation
        error_message = None
        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)

        error_message = customer_validation(customer)

        # saving

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:

            data = {

                'error': error_message,
                'values': value
            }

            return render(request, 'signup.html', data)

