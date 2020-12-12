from django.apps import AppConfig


class OnboardingConfig(AppConfig):
    lable = "onboarding"
    name = f"applications.{ lable }"
