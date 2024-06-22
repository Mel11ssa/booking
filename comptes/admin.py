from django.contrib import admin

# Register your models here.
from .models import Transporteur
from .models import Chauffeur

# Register your models here.
admin.site.register(Transporteur)
admin.site.register(Chauffeur)