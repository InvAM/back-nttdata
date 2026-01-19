from django.db import models

class Users(models.Model):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
        
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name if self.name else 'Unnamed User'