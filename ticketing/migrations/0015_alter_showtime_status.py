# Generated by Django 4.0.6 on 2022-07-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0014_alter_cinema_options_alter_showtime_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='status',
            field=models.IntegerField(choices=[(4, 'فروش بلیت بسته شد'), (5, 'فیلم پخش شد'), (1, 'فروش آغاز نشده است'), (2, 'در حال فروش بلیت'), (3, 'بلیت تمام شده'), (6, 'سانس لغو شد')]),
        ),
    ]
