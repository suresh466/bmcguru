# Generated by Django 2.2.2 on 2019-07-27 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_question_question_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='iteration_num',
            new_name='iteration_num_computer_misc',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='last_answered',
            new_name='last_answered_computer_misc',
        ),
        migrations.RemoveField(
            model_name='question',
            name='right_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='total_right_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='total_wrong_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='wrong_count',
        ),
        migrations.AddField(
            model_name='info',
            name='iteration_num_excel',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='info',
            name='iteration_num_operating_system',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='info',
            name='iteration_num_powerpoint',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='info',
            name='iteration_num_uncategoryzed',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='info',
            name='iteration_num_word',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='info',
            name='last_answered_excel',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='last_answered_operating_system',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='last_answered_powerpoint',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='last_answered_uncategorized',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='last_answered_word',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='total_questions_computer_misc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='total_questions_excel',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='total_questions_operating_system',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='total_questions_powerpoint',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='total_questions_uncategorized',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='total_questions_word',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('uncategorized', 'Uncategorized'), ('excel', 'Excel'), ('word', 'Word'), ('powerpoint', 'Powerpoint'), ('operating_system', 'Operating System'), ('computer_misc', 'Computer Fundamental')], default='Uncategorized', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='opt_e',
            field=models.CharField(blank=True, default='-null-', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='opt_f',
            field=models.CharField(blank=True, default='-null-', max_length=255),
        ),
    ]
