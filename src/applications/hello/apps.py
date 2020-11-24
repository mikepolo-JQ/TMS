from django.apps import AppConfig


class HelloConfig(AppConfig):
    lable = "hello"
    name = f"applications.{lable}"
