from django.db import models

class Cars(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    about = models.TextField(blank=True)
    image = models.CharField(max_length=255,blank=True,default=' ')
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-title']
        indexes=[
            models.Index(fields=['-title'])
        ]
class Review(models.Model):
    user = models.CharField(max_length=255)
    rev = models.TextField(blank=True)

    def __str__(self):
        return f"Review by {self.user}"

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
            ]

class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    about = models.TextField(blank=True)
    image = models.CharField(max_length=255,blank=True,default=' ')
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-title']
        indexes=[
            models.Index(fields=['-title'])
        ]
class Subscriptions(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    about = models.TextField(blank=True)
    image = models.CharField(max_length=255,blank=True,default=' ')
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-title']
        indexes=[
            models.Index(fields=['-title'])
        ]
class gadgets(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    about = models.TextField(blank=True)
    image = models.CharField(max_length=255,blank=True,default=' ')
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-title']
        indexes=[
            models.Index(fields=['-title'])
        ]
