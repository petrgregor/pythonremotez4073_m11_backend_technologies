from django.db.models import Model, CharField, ForeignKey, SET_NULL, DateField, \
    TextField, DateTimeField, ManyToManyField, IntegerField


class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return self.name


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)
    flag = CharField(max_length=4, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    def __repr__(self):
        return f"Country(name={self.name}, flag={self.flag}"

    def __str__(self):
        return f"{self.name} {self.flag}"


class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    country = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators')
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname', 'name', 'date_of_birth']

    def __repr__(self):
        return f"Creator(name={self.name}, surname={self.surname}, date_of_birth={self.date_of_birth})"

    def __str__(self):
        if self.date_of_birth:
            return f"{self.name} {self.surname} ({self.date_of_birth.year})"
        return f"{self.name} {self.surname}"


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    countries = ManyToManyField(Country, blank=True, related_name='movies')
    length = IntegerField(null=True, blank=True)
    actors = ManyToManyField(Creator, blank=True, related_name='acting')
    directors = ManyToManyField(Creator, blank=True, related_name='directing')
    description = TextField(null=True, blank=True)
    released_date = DateField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_orig', 'released_date']

    def __repr__(self):
        return f"Movie(title_orig={self.title_orig}, released_year={self.released_date.year})"

    def __str__(self):
        return f"{self.title_orig} ({self.released_date.year})"

    # TODO: Definovat metodu pro převod délky filmu z minut na formát h:mm
