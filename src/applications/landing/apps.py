from django.apps import AppConfig


class LandingConfig(AppConfig):
    # name = 'landing'
    lable = "landing"
    name = f"applications.{lable}"
