

from ninja import Router


router = Router(tags=["Customers"])

@router.get('/')
def index(request):
    '''
    Index page api for customers...
    '''
    return {"message":"Customer API interface"}
