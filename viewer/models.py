from django.db.models import Model, CharField


class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return self.name
