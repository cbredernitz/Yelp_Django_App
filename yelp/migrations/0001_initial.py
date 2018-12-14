# Generated by Django 2.1.4 on 2018-12-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attire',
            fields=[
                ('attire_id', models.AutoField(primary_key=True, serialize=False)),
                ('attire', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'Business attire',
                'verbose_name_plural': "Business's attire",
                'db_table': 'attire',
                'ordering': ['attire'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_name', models.CharField(max_length=100)),
                ('yelp_business_id', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=15, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('business_stars', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('business_review_count', models.IntegerField(blank=True, null=True)),
                ('is_open', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Business Information',
                'verbose_name_plural': "Business's Information",
                'db_table': 'business',
                'ordering': ['business_name', 'business_stars', 'is_open'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'Business city',
                'verbose_name_plural': "Business's city",
                'db_table': 'city',
                'ordering': ['city_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NoiseLevel',
            fields=[
                ('noise_level_id', models.AutoField(primary_key=True, serialize=False)),
                ('noise', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'Business volumn inside',
                'verbose_name_plural': "Business's volumn inside",
                'db_table': 'noise_level',
                'ordering': ['noise'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('stars', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('review_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Review made by user about a business',
                'verbose_name_plural': 'Reviews made by users about various businesses',
                'db_table': 'review',
                'ordering': ['business', 'user', 'stars', 'date_created', 'review_text'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_abbrev', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'State where the Business is located',
                'verbose_name_plural': 'State where the Business is located',
                'db_table': 'state',
                'ordering': ['state_abbrev'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=45)),
                ('review_count', models.IntegerField()),
                ('yelper_since', models.DateField(blank=True, null=True)),
                ('useful', models.IntegerField(blank=True, null=True)),
                ('cool', models.IntegerField(blank=True, null=True)),
                ('funny', models.IntegerField(blank=True, null=True)),
                ('average_stars', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('yelp_user_id', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'User that has made a review about a business',
                'verbose_name_plural': 'Users that have created reviews about various businesses',
                'db_table': 'user',
                'ordering': ['user_name', 'review_count', 'average_stars', 'yelper_since'],
                'managed': False,
            },
        ),
    ]
