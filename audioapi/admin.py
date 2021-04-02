from django.contrib import admin
from .models import Song
from .models import Podcast
from .models import Audiobook
# Register your models here.
admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Audiobook)



