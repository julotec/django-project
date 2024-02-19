from django.db import models
from django.contrib.auth.models import User



class Meta:
    constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    description = models.CharField(max_length=150, null=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f"{self.name}"


