from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)          # Bu alan auth.User tablosuna atıfta bulunuyoruz, on_delete = models.CASCADE user silinirse kullanıcının bütün makaleleri silinir
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)                     # verbose_name = "" // tırnak içerisinde yazdığımız değeri yazar
    article_image = models.FileField(blank=True, null= True, verbose_name='Upload Photo to Article')

    def __str__(self):
        return self.title                   # article bilgilerini nasıl göstermek iseteriz

    class Meta:                             # sıralama için django Model Meta options ordering
        ordering = ['-created_date']

# modeli değiştirirsek migrations işlemleri yapmalıyız

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article', related_name='comments')
    comment_author = models.CharField(max_length=50, verbose_name='Name')
    comment_content = models.CharField(max_length=250, verbose_name='Comment')
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']