# Generated by Django 4.1.1 on 2022-09-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_tag_project_total_votes_project_vote_ratio_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='/static/images/default.jpg', null=True, upload_to=''),
        ),
    ]
