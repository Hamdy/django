from typing import Any

from django.db import models

class UpperCharField(models.CharField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs['max_length'] = 255
        super().__init__(*args, **kwargs)
    
    def get_prep_value(self, value: Any) -> Any:
        return super().get_prep_value(value).upper()
