# Generated by Django 5.0.3 on 2024-04-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_carsalespost_detected_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsalespost',
            name='detected_image1',
            field=models.ImageField(blank=True, null=True, upload_to='detection_results'),
        ),
        migrations.AlterField(
            model_name='carsalespost',
            name='detected_image2',
            field=models.ImageField(blank=True, null=True, upload_to='detection_results'),
        ),
        migrations.AlterField(
            model_name='carsalespost',
            name='detected_image3',
            field=models.ImageField(blank=True, null=True, upload_to='detection_results'),
        ),
        migrations.AlterField(
            model_name='carsalespost',
            name='detected_image4',
            field=models.ImageField(blank=True, null=True, upload_to='detection_results'),
        ),
        migrations.AlterField(
            model_name='carsalespost',
            name='detected_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='detected_results'),
        ),
    ]
