from django.contrib import admin
from .models import Otp
# Register your models here.


class OtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'otp', 'email')


admin.site.register(Otp, OtpAdmin)
