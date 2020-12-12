# Generated by Django 3.1.2 on 2020-12-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0010_auto_20201209_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='tool',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='tool',
            name='town',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Town/village/locality'),
        ),
    ]