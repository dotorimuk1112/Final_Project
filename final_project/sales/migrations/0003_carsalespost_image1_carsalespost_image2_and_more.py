# Generated by Django 5.0.3 on 2024-04-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_uploadedimage2'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsalespost',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images'),
        ),
        migrations.AddField(
            model_name='carsalespost',
            name='Image2',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images'),
        ),
        migrations.AddField(
            model_name='carsalespost',
            name='Image3',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images'),
        ),
        migrations.AddField(
            model_name='carsalespost',
            name='Image4',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images'),
        ),
        migrations.AddField(
            model_name='carsalespost',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images'),
        ),
        migrations.AlterField(
            model_name='uploadedimage2',
            name='processedimage',
            field=models.ImageField(upload_to='C:\\Users\\CHK\\Desktop\\django_migration\\ourcar_Django\\final_project\\_media'),
        ),
        migrations.AlterField(
            model_name='uploadedimage2',
            name='uploadedimage',
            field=models.ImageField(upload_to='C:\\Users\\CHK\\Desktop\\django_migration\\ourcar_Django\\final_project\\_media'),
        ),
    ]