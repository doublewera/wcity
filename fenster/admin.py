from django.contrib import admin

# Register your models here.

from .models import Fenster
from .models import Apt

admin.site.register(Fenster)
admin.site.register(Apt)

