from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    language_code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class Code(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_utc = models.DateTimeField(auto_now_add=True)
    last_updated_utc = models.DateTimeField(auto_now=True)
    total_views = models.IntegerField(default=0)
    snippet = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    is_private = models.BooleanField(default=False)
    password = models.CharField(max_length=1000, default="")

    def __str__(self):
        return f"{self.language} - {self.code[:30]}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_utc = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    code = models.ForeignKey(Code, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:30]
