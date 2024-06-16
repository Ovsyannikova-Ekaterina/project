#   users/validator.py
from django.core.exceptions import ValidationError
import re

def validate_username(value):
    if not re.match(r'^[\w.@+\-\s]+$', value):  # исправленное регулярное выражение
        raise ValidationError(
            'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_/ spaces characters.'
        )
