# Generated by Django 5.0.7 on 2024-07-29 00:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=280)),
                ('tweet_type', models.CharField(choices=[('TWEET', 'TWEET'), ('REPLY', 'REPLY'), ('QUOTE', 'QUOTE')], default='TWEET', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL)),
                ('referenced_tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retweets', to=settings.AUTH_USER_MODEL)),
                ('referenced_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reposts', to='tweets.tweet')),
            ],
            options={
                'unique_together': {('account', 'referenced_tweet')},
            },
        ),
        migrations.CreateModel(
            name='LikedTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_tweets', to=settings.AUTH_USER_MODEL)),
                ('referenced_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='tweets.tweet')),
            ],
            options={
                'unique_together': {('account', 'referenced_tweet')},
            },
        ),
        migrations.CreateModel(
            name='DislikedTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disliked_tweets', to=settings.AUTH_USER_MODEL)),
                ('referenced_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='tweets.tweet')),
            ],
            options={
                'unique_together': {('account', 'referenced_tweet')},
            },
        ),
    ]
