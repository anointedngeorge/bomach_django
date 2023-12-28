
from ninja import Router


router = Router(tags=["Admins"])

@router.get('/')
def index(request):
    '''
    Authentication API...
    '''
    return {"message":"Admin API interface"}
