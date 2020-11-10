from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)

    def __str__(self):
        return "%s, by %s" % (self.name, self.author)
