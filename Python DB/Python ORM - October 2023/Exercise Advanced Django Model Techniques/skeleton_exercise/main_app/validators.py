from django.core.exceptions import ValidationError


def check_name_type(value):
    if all(x.isalpha() or x.isspace() for x in value):
        pass
    else:
        raise ValidationError("Name can only contain letters and spaces")


def check_phone_number(value):
    if value.startswith('+359') and len(value) == 13:
        pass
    else:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
