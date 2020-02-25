from django.contrib.auth import models
from django.db import migrations

Role_Manager = 'Manager'
Role_Developer = 'Developer'

Groups = (
    Role_Manager,
    Role_Developer
)


def add_groups(apps, schema_editor):
    for g in Groups:
        models.Group.objects.get_or_create(
            name=g
        )


def remove_groups(apps, schema_editor):
    qs = models.Group.objects.filter(name__in=Groups)
    qs.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_groups, remove_groups)
    ]
