# Generated by Django 5.0.3 on 2024-05-01 01:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadedimage', models.ImageField(upload_to='C:\\Users\\CHK\\Desktop\\Final_django\\final_project\\_media')),
                ('processedimage', models.ImageField(upload_to='C:\\Users\\CHK\\Desktop\\Final_django\\final_project\\_media')),
                ('has_car', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'pybo_uploadedimage2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CarSalesPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('MNAME', models.TextField()),
                ('MYERAR', models.IntegerField()),
                ('MILEAGE', models.IntegerField()),
                ('COLOR', models.TextField()),
                ('TRANS', models.TextField()),
                ('F_TYPE', models.TextField()),
                ('DISP', models.IntegerField()),
                ('VTYPE', models.TextField()),
                ('VNUM', models.CharField(max_length=100)),
                ('CU_HIS', models.IntegerField()),
                ('MVD_HIS', models.FloatField()),
                ('AVD_HIS', models.FloatField()),
                ('FD_HIS', models.IntegerField()),
                ('VT_HIS', models.FloatField()),
                ('US_HIS', models.IntegerField()),
                ('PRICE', models.IntegerField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
                ('brand', models.TextField(null=True)),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image4', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image5', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image6', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image7', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('Image8', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('detected_thumbnail', models.ImageField(blank=True, null=True, upload_to='detected_results')),
                ('detected_image1', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image2', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image3', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image4', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image5', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image6', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image7', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('detected_image8', models.ImageField(blank=True, null=True, upload_to='detection_results')),
                ('buyers_count', models.IntegerField(default=0)),
                ('make_deal', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(related_name='buyer_car_sales_posts', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyerMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_price', models.IntegerField()),
                ('accepted', models.BooleanField(null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_messages', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_messages', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_messages', to='sales.carsalespost')),
            ],
            options={
                'db_table': 'BuyerMessages',
                'managed': True,
            },
        ),
    ]
