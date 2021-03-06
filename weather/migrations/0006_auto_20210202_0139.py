# Generated by Django 3.1.5 on 2021-02-02 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_auto_20210202_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='fellsLike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weather.feels'),
        ),
        migrations.AddField(
            model_name='weather',
            name='weatherTemp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weather.temp'),
        ),
    ]
