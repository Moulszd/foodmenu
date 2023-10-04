from django.apps import AppConfig



class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Import and connect your signals here
        import users.signals