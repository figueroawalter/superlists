# Generated by Django 2.1.7 on 2019-04-02 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
            preserve_default=False,
        ),
    ]
