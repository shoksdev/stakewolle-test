from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ReferralCode, CustomUser
from .serializers import CreateReferralCodeSerializer, GetReferralCodeSerializer, GetReferralsListSerializer


class CreateReferralCodeAPIView(CreateAPIView):
    """
    Создаём реферальный код и обрабатываем ошибку если у пользователя уже есть реферальный код,
    просим его удалить свой код
    """

    queryset = ReferralCode.objects.all()
    serializer_class = CreateReferralCodeSerializer
    permission_classes = [IsAuthenticated, ]

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
    """Удаляем реферальный код пользователя"""

    queryset = ReferralCode.objects.all()
    serializer_class = CreateReferralCodeSerializer
    permission_classes = [IsAuthenticated, ]


class RetrieveReferralCodeAPIView(RetrieveAPIView):
    """
    Выводим реферальный код по email адресу реферера, обрабатываем ошибки если у пользователя нет кода/нет пользователя
    """

    queryset = CustomUser.objects.all()
    serializer_class = GetReferralCodeSerializer
    permission_classes = [IsAuthenticated, ]
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
    """Выводим список всех рефералов по id реферера"""

    serializer_class = GetReferralsListSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        referrer_id = self.kwargs.get('referrer_id')
        referral_code = get_object_or_404(CustomUser, id=referrer_id).referral_code.referral_code_title
        return CustomUser.objects.filter(referrer_code=referral_code)
