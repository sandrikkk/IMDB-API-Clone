# Generated by Django 4.0.4 on 2022-05-27 10:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_alter_watchlist_options_watchlist_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField(max_length=200, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='watchlist_app.watchlist')),
            ],
        ),
    ]
