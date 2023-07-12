from django.http import HttpRequest


def get_ip(request:HttpRequest):
    remote_addr = request.META.get('REMOTE_ADDR')
    if remote_addr is not None  :
        user_ip = remote_addr
    else :
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    return user_ip