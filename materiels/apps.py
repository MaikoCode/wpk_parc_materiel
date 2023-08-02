from django.apps import AppConfig


class MaterielsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'materiels'
    def ready(self):
        import materiels.templatetags.custom_filters
        import materiels.signals