from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255)
    size = models.PositiveSmallIntegerField()
    projector_available = models.BooleanField(default=False)


class ReservationStatus(models.Model):
    date = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='reservations')  # 'room_id' in database
    comment = models.TextField()

    class Meta:
        unique_together = ('date', 'room_id')
