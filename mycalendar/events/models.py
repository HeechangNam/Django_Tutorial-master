from django.db import models


# Create your models here.

class Event(models.Model):
    day = models.DateField('Day of the event', help_text='Day of event')
    start_time = models.TimeField("Starting time", help_text='Starting time')
    end_time = models.TimeField("Final time", help_text='Final time')
    notes = models.TextField("Textual Notes", help_text="Textual Notes", blank=True, null=True)

    class Meta:
        verbose_name = "Scheduling"
        verbose_name_plural = "Scheduling"
