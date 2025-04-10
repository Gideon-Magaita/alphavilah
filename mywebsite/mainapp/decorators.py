from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='admins').exists():
                return redirect('admin_home')
            else:
                return view_func(request,*args, **kwargs)
        else: 
            return view_func(request,*args, **kwargs)
    return wrapper_func   

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
               group = request.user.groups.all()[0].name

            if group in allowed_roles:
               return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')   
        return wrapper_func
    return decorator 

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login page if not authenticated

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'admins':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to access this page.", status=403)  

        return HttpResponse("You are not authorized to access this page.", status=403)  

    return wrapper_func      

