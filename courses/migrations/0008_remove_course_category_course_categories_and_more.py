# Generated by Django 4.1.3 on 2023-02-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0007_alter_category_slug_alter_course_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="category",
        ),
        migrations.AddField(
            model_name="course",
            name="categories",
            field=models.ManyToManyField(to="courses.category"),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(default="", unique=True),
        ),
    ]
