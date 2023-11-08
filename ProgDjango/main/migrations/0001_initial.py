# Generated by Django 4.2.6 on 2023-11-01 13:49

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('anons', models.CharField(max_length=250, verbose_name='анонс')),
                ('text', models.TextField(verbose_name='статья')),
                ('time', models.DateTimeField(verbose_name='время публикации')),
                ('picture', models.FileField(null=True, upload_to=main.models.Articales.file_path)),
            ],
        ),
    ]
