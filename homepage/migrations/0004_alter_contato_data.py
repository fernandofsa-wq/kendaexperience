# Generated by Django 4.1.2 on 2022-10-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_contato_alter_dataevento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
