from django.contrib import admin
from .models import Article, Comment         # bulunduğumuz klasördeki models'den Article classını dahil et

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date']   # article hakkında farklı bilgiler vermek
    list_display_links = ['title']                       # title'a basıldığında içeriğe gider
    search_fields = ['title']                            # başlığa göre arama yapılabilir
    list_filter = ['created_date']                       # belirtilen filtreye göre filtre oluşturur
    
    class Meta:
        model = Article             # ArticleAdmin class'ı ile Article birleştirildi
