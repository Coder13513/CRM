# Generated by Django 3.0.4 on 2020-05-08 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('ServiceLevelAgreement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sla',
            name='customer_name',
            field=models.ManyToManyField(to='authentication.Customer'),
        ),
        migrations.AddField(
            model_name='sla',
            name='responsible_person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='authentication.EmployeeProfile'),
        ),
        migrations.AddField(
            model_name='history',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Customer'),
        ),
    ]
