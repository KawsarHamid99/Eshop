from django.shortcuts import redirect

def Auth_middleware(get_response):
    def middleware(request):
        print("Middle--------------------------")
        returnUrl=""
        print(request.META['PATH_INFO'])
        if not request.session.get('customer_id'):
            redirect('login')   

        response=get_response(request)
        return response 
    return middleware
