from django.db import models
from django.conf import settings


class Activity(models.Model):
    index = models.SmallIntegerField(unique=True)
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=512, blank=True)
    publish_date = models.DateField(null=True)
    open = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['index']
        verbose_name_plural = 'activities'


class Section(models.Model):
    index = models.SmallIntegerField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    instructions = models.CharField(max_length=512)
    link_name = models.CharField(max_length=50, blank=True)
    link = models.URLField(default="", blank=True)

    def __str__(self):
        return self.activity.title + " Section " + str(self.index)

    class Meta:
        ordering = ['index']
        unique_together = ('activity', 'index')


class Item(models.Model):
    index = models.SmallIntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)

    def __str__(self):
        return str(self.section) + " Item " + str(self.index)

    class Meta:
        ordering = ['index']
        unique_together = ('section', 'index')


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField()
    post_date_time = models.DateTimeField()

    def __str__(self):
        return str(self.item) + " post by " + self.user.first_name

    class Meta:
        ordering = ['post_date_time']


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date_time = models.DateTimeField()

    def __str__(self):
        return "Comment by " + self.user.first_name + " on " + str(self.post)

    class Meta:
        ordering = ['comment_date_time']

