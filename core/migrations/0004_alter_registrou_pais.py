

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrou',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais'),
        ),
    ]
