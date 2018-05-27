from django.db import models

from .utils import code_generator, create_shortcode
# Create your models here.

class Client(models.Model):
    full_name = models.CharField(max_length=40,)
    email = models.EmailField()
    skype_telegram = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    comments = models.CharField(max_length=400, default="no comments")
    shortcode = models.CharField(max_length=9, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Client, self).save(*args, **kwargs)

