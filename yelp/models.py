# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

class Attire(models.Model):
    attire_id = models.AutoField(primary_key=True)
    attire = models.CharField(unique=True, max_length=45)


    class Meta:
        managed = False
        db_table = 'attire'
        ordering = ['attire']
        verbose_name = 'Business attire'
        verbose_name_plural = "Business's attire"

    def __str__(self):
        return self.attire

'''
class Attire(models.Model):
    attire_id = models.AutoField(primary_key=True)
    attire = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'attire'
'''

class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100)
    yelp_business_id = models.CharField(max_length=45, blank=True, null=True)
    noise_level = models.ForeignKey('NoiseLevel', models.PROTECT, blank=True, null=True)
    attire = models.ForeignKey('Attire', models.PROTECT, blank=True, null=True)
    city = models.ForeignKey('City', models.PROTECT, blank=True, null=False)
    state = models.ForeignKey('State', models.PROTECT, blank=True, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    business_stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    business_review_count = models.IntegerField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business'
        ordering = ['business_name', 'business_stars', 'is_open']
        verbose_name = 'Business Information'
        verbose_name_plural = "Business's Information"

    def __str__(self):
        return self.business_name


'''
class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100)
    yelp_business_id = models.CharField(max_length=45, blank=True, null=True)
    noise_level = models.ForeignKey('NoiseLevel', models.DO_NOTHING, blank=True, null=True)
    attire = models.ForeignKey('Attire', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    business_stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    business_review_count = models.IntegerField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business'
'''


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'city'
        ordering = ['city_name']
        verbose_name = 'Business city'
        verbose_name_plural = "Business's city"

    def __str__(self):
        return self.city_name


'''
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(unique=True, max_length=45)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
'''


class NoiseLevel(models.Model):
    noise_level_id = models.AutoField(primary_key=True)
    noise = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'noise_level'
        ordering = ['noise']
        verbose_name = 'Business volumn inside'
        verbose_name_plural = "Business's volumn inside"

    def __str__(self):
        return self.noise


'''
class NoiseLevel(models.Model):
    noise_level_id = models.AutoField(primary_key=True)
    noise = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'noise_level'
'''


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    business = models.ForeignKey('Business', models.PROTECT, blank=False, null=False)
    user = models.ForeignKey('User', models.PROTECT, blank=False, null=False)
    stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    date_created = models.DateField(blank=True, null=False)
    review_text = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'review'
        ordering = ['business', 'user', 'stars', 'date_created', 'review_text']
        verbose_name = 'Review made by user about a business'
        verbose_name_plural = "Reviews made by users about various businesses"

'''
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    business = models.ForeignKey(Business, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
'''


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_abbrev = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'state'
        ordering = ['state_abbrev']
        verbose_name = 'State where the Business is located'
        verbose_name_plural = "State where the Business is located"

    def __str__(self):
        return self.state_abbrev

'''
class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_abbrev = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'state'
'''


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    review_count = models.IntegerField()
    yelper_since = models.DateField(blank=True, null=False)
    useful = models.IntegerField(blank=True, null=True)
    cool = models.IntegerField(blank=True, null=True)
    funny = models.IntegerField(blank=True, null=True)
    average_stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    yelp_user_id = models.CharField(max_length=45, blank=True, null=False)

    business = models.ManyToManyField(Business, through='Review')

    class Meta:
        managed = False
        db_table = 'user'
        ordering = ['user_name', 'review_count', 'average_stars', 'yelper_since']
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
		# return reverse('site_detail', args=[str(self.id)])
        return reverse('user_detail', kwargs={'pk': self.pk})

    @property
    def business_names(self):

        businesses = self.business.order_by('business_name')

        names = []
        for business in businesses:
            name = business.business_name
            if name is None:
                continue
            if name not in names:
                names.append(name)
        return ', '.join(names)

'''
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    review_count = models.IntegerField()
    yelper_since = models.DateField(blank=True, null=True)
    useful = models.IntegerField(blank=True, null=True)
    cool = models.IntegerField(blank=True, null=True)
    funny = models.IntegerField(blank=True, null=True)
    average_stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yelp_user_id = models.CharField(max_length=45, blank=True, null=True)

    business_info = models.ManyToManyField(Business, through='Review')

    class Meta:
        managed = False
        db_table = 'user'
'''