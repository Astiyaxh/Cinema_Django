# Generated by Django 4.0.6 on 2022-07-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_alter_showtime_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='status',
            field=models.IntegerField(choices=[(6, 'سانس لغو شد'), (2, 'در حال فروش بلیت'), (5, 'فیلم پخش شد'), (3, 'بلیت تمام شده'), (1, 'فروش آغاز نشده است'), (4, 'فروش بلیت بسته شد')]),
        ),
    ]
