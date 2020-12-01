from django.apps import AppConfig


class BlogConfig(AppConfig):
    lable = "blog"
    name = f"applications.{ lable }"
