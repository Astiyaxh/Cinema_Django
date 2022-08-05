# Generated by Django 4.0.6 on 2022-07-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0017_alter_showtime_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='image',
            field=models.ImageField(null=True, upload_to='cinema_images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='temporary', upload_to='movie_posters/', verbose_name='پوستر'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='showtime',
            name='status',
            field=models.IntegerField(choices=[(4, 'فروش بلیت بسته شد'), (2, 'در حال فروش بلیت'), (6, 'سانس لغو شد'), (5, 'فیلم پخش شد'), (3, 'بلیت تمام شده'), (1, 'فروش آغاز نشده است')]),
        ),
    ]
