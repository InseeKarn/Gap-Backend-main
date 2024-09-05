# Generated by Django 4.1.2 on 2022-12-29 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordMessage',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False)),
                ('discord_id', models.IntegerField()),
                ('channel_id', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=10000)),
                ('timestamp', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscordMessageMentionUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discordmessage')),
            ],
        ),
        migrations.CreateModel(
            name='DiscordMessageMentionRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discordmessage')),
            ],
        ),
        migrations.CreateModel(
            name='DiscordMessageMentionChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=100)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discordmessage')),
            ],
        ),
        migrations.CreateModel(
            name='DiscordMessageEmoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(max_length=100)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discordmessage')),
            ],
        ),
        migrations.CreateModel(
            name='DiscordMessageAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discordmessage')),
            ],
        ),
    ]
