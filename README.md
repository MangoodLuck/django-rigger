# Django Rigger

**rigger is a django toolset that provides a daily common tool**

---

# Requirements
- Python (3.5, 3.6, 3.7, 3.8)
- Django (2.1, 2.2, 3.0)

I **highly recommend** and only officially support the latest patch release of each Python and Django series.
# Installation
Install using pip...

```
pip install django-rigger
```

Add 'rigger' to your INSTALLED_APPS setting.

```
INSTALLED_APPS = [
    ...
    'rigger',
]
```
## Example

### RegexValidator

These validators can be used to customized regex, the value must be match the 'word'(r"^[a-zA-Z\u4e00-\u9fa5]+$")

```
from rigger.validators import RegexValidator
from rigger.regexes import word
class ExampleSerializer(serializers.Serializer):
    # ...
    class Meta:
        validators = [
            RegexValidator(word)
        ]
```

