# Generated by Django 5.0.3 on 2024-04-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_carsalespost_image5_carsalespost_image6_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage2',
            name='processedimage',
            field=models.ImageField(upload_to='C:\\ITStudy\\12_Project\\main\\final_project\\_media'),
        ),
        migrations.AlterField(
            model_name='uploadedimage2',
            name='uploadedimage',
            field=models.ImageField(upload_to='C:\\ITStudy\\12_Project\\main\\final_project\\_media'),
        ),
    ]