# Generated by Django 4.1.1 on 2022-10-21 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0003_alter_ad_name_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('items', models.ManyToManyField(to='ads.ad')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Подборка объявлений',
                'verbose_name_plural': 'Подборки объявлений',
            },
        ),
    ]
