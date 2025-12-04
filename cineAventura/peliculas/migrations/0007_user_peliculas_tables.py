# Generated manually for User.add_to_class() fields

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peliculas', '0006_remove_resena_usuarios_util_resena_util_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_peliculas_favoritas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pelicula', models.ForeignKey(on_delete=models.deletion.CASCADE, to='peliculas.pelicula')),
            ],
            options={
                'db_table': 'auth_user_peliculas_favoritas',
                'unique_together': {('user', 'pelicula')},
            },
        ),
        migrations.CreateModel(
            name='User_peliculas_ver_despues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pelicula', models.ForeignKey(on_delete=models.deletion.CASCADE, to='peliculas.pelicula')),
            ],
            options={
                'db_table': 'auth_user_peliculas_ver_despues',
                'unique_together': {('user', 'pelicula')},
            },
        ),
    ]