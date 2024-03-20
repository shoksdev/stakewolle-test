from django.contrib import admin

from .models import CustomUser, ReferralCode


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Регистрируем модель пользователя в админ-панели"""

    list_display = ('username', 'email', 'referrer_code')
    search_fields = ('referrer_code',)


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    """Регистрируем модель реферального кода в админ-панели"""

    list_display = ('user', 'referral_code_title', 'referral_code_due_date')
