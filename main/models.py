from django.db import models

# Create your models here.


class Project(models.Model):
    """Fase 2 / A2 (notes C2).

    Nama field di bawah = ASUMSI kita, tidak ada di notes.
    # VERIFY: kalau spec kuis menyebut nama/field lain, spec kuis menang.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='projects')
    starred_by = models.ManyToManyField('auth.User', related_name='starred_projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name