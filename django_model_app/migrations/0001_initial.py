# Generated by Django 3.1.3 on 2020-11-27 17:29

from django.db import migrations, models
import django.db.models.deletion
import django_model_app.models.on_delete_option_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCASCADE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Post CASCADE',
            },
        ),
        migrations.CreateModel(
            name='PostDONOTHING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Post DO_NOTHING',
            },
        ),
        migrations.CreateModel(
            name='PostPROTECT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Post PROTECT',
            },
        ),
        migrations.CreateModel(
            name='PostSET',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Post SET',
            },
        ),
        migrations.CreateModel(
            name='PostSETDEFAULT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Post SET_DEFAULT',
            },
        ),
        migrations.CreateModel(
            name='PostSETNULL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Post SET_NULL',
            },
        ),
        migrations.CreateModel(
            name='CommentSETNULL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_set_null', to='django_model_app.postsetnull')),
            ],
            options={
                'verbose_name_plural': 'Comment SET_NULL',
            },
        ),
        migrations.CreateModel(
            name='CommentSETDEFAULT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('post', models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='comments_set_default', to='django_model_app.postsetdefault')),
            ],
            options={
                'verbose_name_plural': 'Comment SET_DEFAULT',
            },
        ),
        migrations.CreateModel(
            name='CommentSET',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('post', models.ForeignKey(on_delete=models.SET(django_model_app.models.on_delete_option_model.get_sentinel_post_set), related_name='comments_set', to='django_model_app.postset')),
            ],
            options={
                'verbose_name_plural': 'Comment SET',
            },
        ),
        migrations.CreateModel(
            name='CommentPROTECT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments_protect', to='django_model_app.postprotect')),
            ],
            options={
                'verbose_name_plural': 'Comment PROTECT',
            },
        ),
        migrations.CreateModel(
            name='CommentDONOTHING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments_do_nothing', to='django_model_app.postdonothing')),
            ],
            options={
                'verbose_name_plural': 'Comment DO_NOTHING',
            },
        ),
        migrations.CreateModel(
            name='CommentCASCADE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_cascade', to='django_model_app.postcascade')),
            ],
            options={
                'verbose_name_plural': 'Comment CASCADE',
            },
        ),
    ]
