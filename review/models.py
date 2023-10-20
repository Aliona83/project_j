from django.db import models
from django.contrib.auth.models import User
from jewelleries.models import Jewellery

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField(default=0)
    
def __str__(self):
    return self.user.username
