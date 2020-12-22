from django.db import migrations
from api.user.models import User


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = User(name='Sumit', email='sumit@milan.printers', is_staff=True, is_superuser=True,
                    phone='9876543210', gender="Male", address="17, Mayur Park Society")
        user.set_password('1234')
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
