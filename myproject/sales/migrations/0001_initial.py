# Generated by Django 3.0.4 on 2020-03-31 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ra.base.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date and time')),
                ('lastmod', models.DateTimeField(db_index=True, verbose_name='last modification')),
                ('slug', models.SlugField(blank=True, help_text='For fast recall', unique=True, verbose_name='refer code')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('fb', models.DecimalField(decimal_places=2, default=0, help_text='Opening Balance or initial balance ', max_digits=19, verbose_name='beginning balance')),
                ('address', models.CharField(blank=True, max_length=260, null=True, verbose_name='address')),
                ('telephone', models.CharField(blank=True, max_length=130, null=True, verbose_name='telephone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('lastmod_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_client_lastmod_related', to=settings.AUTH_USER_MODEL, verbose_name='last modification by')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_client_related', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
            bases=(ra.base.models.DiffingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date and time')),
                ('lastmod', models.DateTimeField(db_index=True, verbose_name='last modification')),
                ('slug', models.SlugField(blank=True, help_text='For fast recall', unique=True, verbose_name='refer code')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('fb', models.DecimalField(decimal_places=2, default=0, help_text='Opening Balance or initial balance ', max_digits=19, verbose_name='beginning balance')),
                ('lastmod_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_product_lastmod_related', to=settings.AUTH_USER_MODEL, verbose_name='last modification by')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_product_related', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(ra.base.models.DiffingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SimpleSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, verbose_name='refer code')),
                ('doc_date', models.DateTimeField(db_index=True, verbose_name='date')),
                ('doc_type', models.CharField(db_index=True, max_length=30)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='value')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date and time')),
                ('lastmod', models.DateTimeField(db_index=True, verbose_name='last modification')),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='price')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='discount')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Client')),
                ('lastmod_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_simplesales_lastmod_related', to=settings.AUTH_USER_MODEL, verbose_name='last modification by')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_simplesales_related', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Product')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
            bases=(ra.base.models.DiffingMixin, models.Model),
        ),
    ]
