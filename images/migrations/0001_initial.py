# Generated by Django 3.2 on 2023-01-31 16:25

from django.db import migrations, models
import django_extensions.db.fields
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=16, prefix='image_', primary_key=True, serialize=False)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('thickness', models.IntegerField()),
                ('useless_length', models.IntegerField()),
                ('useless_width', models.IntegerField()),
                ('path', models.FileField(upload_to='')),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ('-created',),
            },
        ),
    ]
