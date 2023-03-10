# Generated by Django 4.1.7 on 2023-03-10 16:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0084_merge_0081_alter_page_title_0083_workflowcontenttype"),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]