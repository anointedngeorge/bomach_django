from ninja import Router


router = Router(tags=["Drivers"])

@router.get('/')
def index(request):
    '''
        Index page api for drivers...
    '''
    return {"message":"Drivers API interface"}
