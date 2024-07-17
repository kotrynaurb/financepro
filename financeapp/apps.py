from django.apps import AppConfig


class FinanceappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'financeapp'

    def ready(self):
        from .signals import create_profile