from authuser.models import *


def contextProcessor(request):
    return {
       'branches': Branch.objects.all(),
    }