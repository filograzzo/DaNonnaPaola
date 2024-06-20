from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# - Modello per avere anche la bio e l'immagine profilo nel profilo
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    friends = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)


# - Modello per la creazione di una ricetta
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('ANTIPASTI', 'Antipasti'),
        ('PRIMI', 'Primi'),
        ('SECONDI', 'Secondi'),
        ('DOLCI', 'Dolci')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recipes_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='recipes/%Y/%m/%d')
    description = models.TextField("Description")
    ingredients = models.TextField("Ingredients")
    preparation = models.TextField("Preparation")
    preparation_time = models.IntegerField("Preparation Time (minutes)", default=0)
    created = models.DateField(auto_now_add=True, db_index=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_recipes', blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='PRIMI')
    objects = models.Manager()

    def __str__(self):
        return self.title
