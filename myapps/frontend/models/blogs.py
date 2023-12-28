from django.db import models




class BlogCategory(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blogs Categories'

    def __str__(self) -> str:
        return f"Blog - {self.title}"



class Blog(models.Model):
    category = models.ForeignKey("frontend.BlogCategory", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blogs')
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self) -> str:
        return f"Blog - {self.title}"