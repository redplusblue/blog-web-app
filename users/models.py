from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')
    bio = models.TextField(max_length=3000, default="Hello! I'm a user of the blog.")
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # Old Image resize using Pillow 
    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)

    #    img = Image.open(self.image.path)
        
    #    if img.height > 300 or img.width > 300:
    #        output_size = (300, 300)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)

