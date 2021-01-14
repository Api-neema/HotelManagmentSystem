from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

#importing all viweos to riseter to router
from fees.api.views      import conductedFeesApi
from members.api.views   import UsersApi
from hotel_app.api.views import hotelApi
from service.api.views   import servicesApi
from payment.api.views   import PaymentApi
from room.api.views      import roomApi
from review.api.views    import reviewApi
from feedback.api.views  import feedbackApi
from booking.api.views   import bookingApi
from sightseeing.api.views   import queryApi


router = routers.SimpleRouter()
router.register(r'fee'      , conductedFeesApi)
router.register(r'user'     , UsersApi )
router.register(r'hotel'    , hotelApi)
router.register(r'services' , servicesApi)
router.register(r'card'     , PaymentApi )
router.register(r'room'     , roomApi)
router.register(r'reviews'  , reviewApi)
router.register(r'feedback' , feedbackApi)
router.register(r'book'     , bookingApi)
router.register(r'sightseeing'     , queryApi)

# router.register(r'test'      , testApi , basename='conductedFees')




urlpatterns = [
    path('appadmin/', admin.site.urls),

    # api
    path('api/', include(router.urls)),
]
