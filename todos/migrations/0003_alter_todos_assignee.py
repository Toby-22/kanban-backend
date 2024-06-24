# Generated by Django 5.0.6 on 2024-06-24 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_job_position'),
        ('todos', '0002_alter_todos_category_alter_todos_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact'),
        ),
    ]
