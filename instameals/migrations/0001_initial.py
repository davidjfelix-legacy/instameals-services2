# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-02 16:10
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'permissions': (('APIUser', 'APIUser'),),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('line1', models.TextField()),
                ('line2', models.TextField(blank=True, default='')),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('postal_code', models.TextField()),
                ('country', models.TextField()),
            ],
            options={
                'permissions': (('Address', 'Address'),),
            },
        ),
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=250)),
            ],
            options={
                'permissions': (('Allergen', 'Allergen'),),
            },
        ),
        migrations.CreateModel(
            name='DietaryFilter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteSeller',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('favoriter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_sellers', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_sellers_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=10000)),
                ('portions', models.PositiveSmallIntegerField()),
                ('portions_available', models.PositiveSmallIntegerField()),
                ('available_from', models.DateTimeField()),
                ('available_to', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('allergens', models.ManyToManyField(blank=True, related_name='meals', to='instameals.Allergen')),
                ('dietary_filters', models.ManyToManyField(blank=True, related_name='meals', to='instameals.DietaryFilter')),
                ('images', models.ManyToManyField(related_name='meals', to='instameals.Image')),
                ('ingredients', models.ManyToManyField(blank=True, related_name='meals', to='instameals.Ingredient')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meal', to='instameals.Location')),
                ('pickup_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='instameals.Address')),
                ('preview_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preview_meals', to='instameals.Image')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_meal', 'View Meal'),),
            },
        ),
        migrations.CreateModel(
            name='MealReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_review_of', to='instameals.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billed_orders', to='instameals.Address')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instameals.Meal')),
                ('pickup_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_orders', to='instameals.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_reviews_of', to='instameals.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=10000)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='SellerReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller_review', to='instameals.Review')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_reviews', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_reviews_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orderreview',
            name='review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_review', to='instameals.Review'),
        ),
        migrations.AddField(
            model_name='orderreview',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mealreview',
            name='review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meal_review', to='instameals.Review'),
        ),
        migrations.AddField(
            model_name='mealreview',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apiuser',
            name='addresses',
            field=models.ManyToManyField(related_name='users', to='instameals.Address'),
        ),
        migrations.AddField(
            model_name='apiuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='apiuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
