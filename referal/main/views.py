from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response

from .models import ReferralCode, CustomUser
from .serializers import CreateReferralCodeSerializer, GetReferralCodeSerializer, GetReferralsListSerializer


class CreateReferralCodeAPIView(CreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = CreateReferralCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.validated_data['user'] = request.user
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            error_message = 'У вас уже есть код реферера, удалите свой перед созданием нового!'
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)


class DestroyReferralCodeAPIView(DestroyAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = CreateReferralCodeSerializer


class RetrieveReferralCodeAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetReferralCodeSerializer
    lookup_field = 'email'

    def retrieve(self, request, *args, **kwargs):
        email = kwargs.get('email')
        try:
            user = self.queryset.get(email=email)
            serializer = self.get_serializer(user)
            referral_code = serializer.data.get('referral_code', None)
            if referral_code is None:
                return Response({'error': 'У этого пользователя нет реферального кода'},
                                status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Пользователь с таким адресом электронной почты не найден'},
                            status=status.HTTP_404_NOT_FOUND)


class ReferralsListAPIView(ListAPIView):
    serializer_class = GetReferralsListSerializer

    def get_queryset(self):
        referer_id = self.kwargs.get('referer_id')
        print(referer_id)
        referral_code = get_object_or_404(CustomUser, id=referer_id).referral_code.referral_code_title
        return CustomUser.objects.filter(reference_code=referral_code)
