from django.db import models


class About(models.Model):
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Information (Last updated on {self.updated_on})"