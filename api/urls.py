
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'accounts',views.AccountViewSet)

urlpatterns = router
