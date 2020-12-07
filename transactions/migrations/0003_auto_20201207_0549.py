# Generated by Django 3.1.2 on 2020-12-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20201206_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='cost',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='selling_time',
            field=models.DateTimeField(null=True, verbose_name='When transaction is made'),
        ),
    ]