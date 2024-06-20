# Generated by Django 4.2.11 on 2024-06-18 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='recipes/%Y/%m/%d')),
                ('description', models.TextField(verbose_name='Description')),
                ('ingredients', models.TextField(verbose_name='Ingredients')),
                ('preparation', models.TextField(verbose_name='Preparation')),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
