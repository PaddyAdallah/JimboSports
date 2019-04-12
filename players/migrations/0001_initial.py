# Generated by Django 2.2 on 2019-04-11 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=100)),
                ('birth_certificate', models.CharField(max_length=50)),
                ('date_joined', models.DateField()),
                ('date_left', models.DateField()),
                ('player_status', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=30)),
                ('sub_team', models.CharField(max_length=2)),
                ('current_team_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('additional_info', models.CharField(max_length=250)),
                ('from_team_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_team_name', to='users.Team')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.Players')),
                ('to_team_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_team_Name', to='users.Team')),
            ],
        ),
        migrations.CreateModel(
            name='PlayersStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField()),
                ('match_time', models.DateField()),
                ('injured', models.CharField(max_length=5)),
                ('cards', models.CharField(max_length=5)),
                ('match_fixture_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='matches.MatchFixtures')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.Players')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Team')),
            ],
        ),
    ]