from django.urls import path

from .views import CreateReferralCodeAPIView, DestroyReferralCodeAPIView

urlpatterns = [
    path('create/referral/code/', CreateReferralCodeAPIView.as_view(), name='create_referral_code'),
    path('delete/referral/code/<int:pk>/', DestroyReferralCodeAPIView.as_view(), name='delete_referral_code'),

]
