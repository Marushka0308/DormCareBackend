from django.contrib import admin
from .models import User
from .models import Complaints
from .models import Announcements

# The dot refers to the same directory - in .models
admin.site.register(User)
admin.site.register(Complaints)
admin.site.register(Announcements)