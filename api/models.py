from django.db import models
import string
import random

def GenerateUniqueCode():
  length = 6

  while True:
    code = ''.join(random.choices(string.ascii_uppercase, k=length))
    if Room.objects.filter(code=code).count() == 0:
      break

  return code
# Create your models here.
class Room(models.Model):
  roomCode = models.CharField(max_length=10, default="", unique=True)
  host = models.CharField(max_length=50, unique=True)
  guestCanPause = models.BooleanField(null=False, default=False)
  votesToSkip = models.IntegerField(null=False, default=1)
  createdAt = models.DateTimeField(auto_now_add=True)

