# Generated by Django 4.1.7 on 2023-02-28 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_alter_author_genre_alter_post_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="genre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="author_genre",
                to="post.category",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="blog_author",
                to="post.author",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="blog_category",
                to="post.category",
            ),
        ),
    ]