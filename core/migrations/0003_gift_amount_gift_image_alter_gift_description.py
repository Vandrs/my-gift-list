# Generated by Django 4.1 on 2022-09-08 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_event_options_alter_event_event_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='Valor'),
        ),
        migrations.AddField(
            model_name='gift',
            name='image',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Descrição'),
        ),
    ]
