from tabnanny import verbose
from django.db import models

# Create your models here.


class Movie (models.Model):
    """
    Represent a Movie
    """
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField('نام', max_length=100)
    director = models.CharField('کارگردان', max_length=50)
    year = models.IntegerField('سال ساخت')
    length = models.IntegerField('مدت زمان')
    description = models.TextField('فرانمود')
    poster = models.ImageField('پوستر', upload_to='movie_posters/')

    def __str__(self):
        return self.name


class Cinema (models.Model):
    """
    Represent a Cinema
    """
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    cinema_id = models.IntegerField('کد سینما', primary_key=True)
    name = models.CharField('نام', max_length=50)
    city = models.CharField('شهر', max_length=30, default='اهواز')
    capacity = models.IntegerField('گنجایش')
    phone = models.CharField(
        'شماره تلفن', max_length=20, null=True, blank=True)
    address = models.TextField('آدرس')
    image = models.ImageField(
        '', upload_to='cinema_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class ShowTime (models.Model):
    """
    Represent a movie show in cinema at a specitic time
    """
    class Meta:
        verbose_name = 'زمان نمایش (سانس)'
        verbose_name_plural = 'زمان نمایش (سانس)'

    movie = models.ForeignKey(
        'Movie', on_delete=models.PROTECT, verbose_name='فیلم')
    cinema = models.ForeignKey(
        'Cinema', on_delete=models.PROTECT, verbose_name='سینما')
    start_time = models.DateTimeField('زمان آغاز نمایش')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('صندلی های قابل فروش')
    free_seats = models.IntegerField('صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLDOUT = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = {
        (SALE_NOT_STARTED, 'فروش آغاز نشده است'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLDOUT, 'بلیت تمام شده'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد')
    }
    status = models.IntegerField(
        'وضعیت', choices=status_choices, default=SALE_NOT_STARTED)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)

    def get_price_display(self):
        return '{} تومان'.format(self.price)

    def is_full(self):
        """
        Returns True if all seats are sold
        """
        return self.free_seats == 0
