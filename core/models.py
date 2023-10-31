from django.db import models
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=300)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='children')
    position = models.PositiveIntegerField()
    is_named_link = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_named_link:
            self.link = self.get_full_url()
        super(MenuItem, self).save(*args, **kwargs)

    def get_full_url(self):
        try:
            full_url = reverse(self.link)
            return full_url
        except NoReverseMatch:
            return ''


class Menu(models.Model):
    title = models.CharField(max_length=50, unique=True)
    menu_item = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.title
