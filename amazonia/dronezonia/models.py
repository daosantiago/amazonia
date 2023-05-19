from django.db import models


class Path(models.Model):
    path = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self) -> str:
        return self.path
