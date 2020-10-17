from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    language_code = models.IntegerField(default=100, null=False, blank=False)
    is_popular = models.BooleanField(default=False, verbose_name="Popular")
    short_name = models.CharField(max_length=30, null=True, blank=True)
    file_extension = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Code(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_utc = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    # last_updated_utc = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    total_views = models.IntegerField(default=0)

    snippet_title = models.CharField(max_length=1000, default="", verbose_name="Title/Filename")
    snippet_body = models.TextField(verbose_name="Code Snippet")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    is_private = models.BooleanField(default=False, verbose_name="Private")
    password = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return f"{self.snippet_title[:30]}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_utc = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    code = models.ForeignKey(Code, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:30]
