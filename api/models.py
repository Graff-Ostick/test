from django.utils.timezone import now
from django.db import models

class Author(models.Model):
    """ model of Author that have only name, and return it (str) """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    """ model of Article have some fields:
        author - associate it with Author
        title - str
        date - creation date (date.time format)
        link - url
     """
    title = models.TextField("Place for title")
    date = models.DateTimeField("Place for date", default=now)
    link = models.SlugField("Place for link", max_length=160, unique=True,)
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)
    upvotes = models.PositiveSmallIntegerField("amount of upvotes", default=0)


    def __str__(self):
        return self.title

    def add_upvote(self):
        self.upvotes+=1


    def resetUpvotes(self):
        self.upvotes = 0


class Review(models.Model):
    """ model of comment have some fields:
           name,text - str
           text - content of comment
           date - creation date (date.time format)
           parent - using it we can comment on comments
           article - associate it with Article
        """
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Comment", max_length=5000)
    date = models.DateTimeField("Place for date", default=now)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    article = models.ForeignKey(Article, verbose_name="Article", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.article}"