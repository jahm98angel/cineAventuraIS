# Generated manually for User.add_to_class() fields

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peliculas', '0006_remove_resena_usuarios_util_resena_util_count'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS auth_user_peliculas_favoritas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
                    pelicula_id INTEGER NOT NULL REFERENCES peliculas_pelicula(id) ON DELETE CASCADE,
                    UNIQUE(user_id, pelicula_id)
                );
                CREATE INDEX IF NOT EXISTS auth_user_peliculas_favoritas_user_id ON auth_user_peliculas_favoritas(user_id);
                CREATE INDEX IF NOT EXISTS auth_user_peliculas_favoritas_pelicula_id ON auth_user_peliculas_favoritas(pelicula_id);
            """,
            reverse_sql="DROP TABLE IF EXISTS auth_user_peliculas_favoritas;"
        ),
        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS auth_user_peliculas_ver_despues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
                    pelicula_id INTEGER NOT NULL REFERENCES peliculas_pelicula(id) ON DELETE CASCADE,
                    UNIQUE(user_id, pelicula_id)
                );
                CREATE INDEX IF NOT EXISTS auth_user_peliculas_ver_despues_user_id ON auth_user_peliculas_ver_despues(user_id);
                CREATE INDEX IF NOT EXISTS auth_user_peliculas_ver_despues_pelicula_id ON auth_user_peliculas_ver_despues(pelicula_id);
            """,
            reverse_sql="DROP TABLE IF EXISTS auth_user_peliculas_ver_despues;"
        ),
    ]