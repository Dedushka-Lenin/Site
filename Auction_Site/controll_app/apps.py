from django.apps import AppConfig

class ControllAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'controll_app'

    def ready(self):
        # Ваши инициализационные действия здесь
        # from .startup import startup_routine
        # startup_routine()

        pass



default_app_config = 'controll_app.apps.ControllAppConfig'