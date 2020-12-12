from django.apps import AppConfig


class MainConfig(AppConfig):
    # name = 'main'
    label = "main"
    name = f"applications.{ label }"
