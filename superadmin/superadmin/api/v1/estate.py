
from ninja import Router
from realestate.models import *

router = Router(tags=["Estates"])


@router.get('get-estates')
def estates(request):
    req =  request.META
    url_scheme = req.get('wsgi.url_scheme')
    HTTP_HOST =  req.get('HTTP_HOST')
    
    container = []
    realestates = RealEstate.objects.all()
    for x in realestates:
        http_url =  f"{url_scheme}://{HTTP_HOST}{x.banner.url}"
        data = {
            'id':x.id,
            'name':x.name,
            'content':x.content,
            'total_amount':x.total_amount,
            'banner':http_url
        }
        container.append(data)
    return {"data":container}
