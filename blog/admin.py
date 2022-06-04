from django.contrib import admin
from .models import Post

# Registering Post model to show it on Django admin page
admin.site.register(Post)
