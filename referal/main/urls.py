from django.urls import path

from .views import CreateReferralCodeAPIView, DestroyReferralCodeAPIView, RetrieveReferralCodeAPIView, \
    ReferralsListAPIView

urlpatterns = [
    path('create/referral/code/', CreateReferralCodeAPIView.as_view(), name='create_referral_code'),
    path('delete/referral/code/<int:pk>/', DestroyReferralCodeAPIView.as_view(), name='delete_referral_code'),
    path('get/referral/code/<str:email>/', RetrieveReferralCodeAPIView.as_view(), name='retrieve_referral_code'),
    path('get/referrals/list/<int:referer_id>/', ReferralsListAPIView.as_view(), name='get_referrals_list'),

]
