from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/categorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.nom

class Video(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    video = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.titre

class Gallerie(models.Model):
    photo = models.ImageField(upload_to='images_gallerie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return "photo"


class Photo(models.Model):
    image = models.ImageField()
    titre = models.CharField(max_length=255)
    description = models.TextField()
    auteur = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categorie_photo')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE,related_name='commentaire_photo')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.nom

class Blog(models.Model):
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE,related_name='photo_blog')
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categorie_blog')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.photo.titre




