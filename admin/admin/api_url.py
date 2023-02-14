# loading api ninja
from ninja import NinjaAPI

from admin.api.v1.api_admin import router as router1
from admin.api.v1.api_customer import router as router2
from admin.api.v1.api_driver import router as router3
from admin.api.v1.api_upload_images import router as router4

from django.contrib.admin.views.decorators import staff_member_required


# docs_decorator=staff_member_required

api = NinjaAPI()
api.add_router(f"images/", router4)
# api.add_router(f"customer/", router2)
# api.add_router(f"driver/", router3)