# Generated by Django 4.2.13 on 2024-06-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='festival',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='festival',
            name='time',
            field=models.CharField(choices=[('00:00:00', '00:00:00'), ('01:00:00', '01:00:00'), ('02:00:00', '02:00:00'), ('03:00:00', '03:00:00'), ('04:00:00', '04:00:00'), ('05:00:00', '05:00:00'), ('06:00:00', '06:00:00'), ('07:00:00', '07:00:00'), ('08:00:00', '08:00:00'), ('09:00:00', '09:00:00'), ('10:00:00', '10:00:00'), ('11:00:00', '11:00:00'), ('12:00:00', '12:00:00'), ('13:00:00', '13:00:00'), ('14:00:00', '14:00:00'), ('15:00:00', '15:00:00'), ('16:00:00', '16:00:00'), ('17:00:00', '17:00:00'), ('18:00:00', '18:00:00'), ('19:00:00', '19:00:00'), ('20:00:00', '20:00:00'), ('21:00:00', '21:00:00'), ('22:00:00', '22:00:00'), ('23:00:00', '23:00:00')]),
        ),
    ]
