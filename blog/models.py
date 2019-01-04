from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
import uuid
# Create your models here.


# create model blog
class Author(models.Model):
    blogger_name = models.CharField(max_length=50)
    blogger_introduce = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.blogger_name

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])


class Blog(models.Model):
    title = models.CharField(max_length=100, help_text="Write your blog title here")
    describe = models.TextField(max_length=3000, help_text="Write the text here")
    blog_write_time = models.DateTimeField(null=True, blank=True)
    blog_authors = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail-view', args=[str(self.id)])

    class Meta:
        ordering = ['blog_write_time']


class Comment(models.Model):
    comment_text = models.TextField(max_length=500, help_text="Weite your world here")
    comment_authors = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment_write_time = models.DateTimeField(null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse('blog-detail-view', args=[str(self.id)])

    class Meta:
        ordering = ['-comment_write_time']

    def display_commenttext(self):
        return self.comment_text[:15]
    display_commenttext.short_description = 'Comment'

