from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .other_functions import calc_excel


class ExcelFile(models.Model):
    initial_file = models.FileField()
    file_name = models.CharField(max_length=120, default='')
    date_upload = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=120, default='loaded')
    results = models.CharField(max_length=120, default='')


@receiver(post_save, sender=ExcelFile)
def update_spouse(sender, instance, **kwargs):
    post_save_functions(instance.initial_file, instance.id)


def post_save_functions(file, id: int):
    obj = ExcelFile.objects.filter(pk=id)
    obj.update(
        status='is_being_processed',
        file_name=file.name,
    )
    results, time = calc_excel(file)
    obj.update(
        status='processed',
        results=results,
        date_processed=time,
    )
