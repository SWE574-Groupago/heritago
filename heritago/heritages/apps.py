from django.apps import AppConfig


class HeritagesConfig(AppConfig):
    name = 'heritages'

    def ready(self):
        super().ready()
        from heritago.heritages import search
