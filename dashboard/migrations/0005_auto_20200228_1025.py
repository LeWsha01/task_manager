# Generated by Django 3.0.3 on 2020-02-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200228_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
