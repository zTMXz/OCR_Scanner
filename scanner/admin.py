from idlelib.history import History

from django.contrib import admin
from .models import Scanner, ScanHistory

# Register your models here.
admin.site.register(Scanner)
admin.site.register(ScanHistory)