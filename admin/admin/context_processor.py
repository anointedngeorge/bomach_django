from authuser.models import *
from operations.models import *
from realestate.models import *


def contextProcessor(request):
    return {
       'branches': Branch.objects.all(),
       'tasks':OperationTask.objects.all(),
       'estates':RealEstate.objects.all(),
       'plots':RealEstatePlot.objects.all(),
       'sites':OperationSite.objects.all(),
       'projects':OperationProject.objects.all()
    }