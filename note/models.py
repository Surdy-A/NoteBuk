from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse



class Note(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    author = author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, default=''
    )
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 related_name='note')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, default='')
    

    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('note:note_detail', args=[self.id])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save()
   



class Category(models.Model):
    CATEGORIES = (
        ('Uncategorized', 'Uncategorized'),
        ('Work', 'Work'),
        ('Family', 'Family Affair'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
        )

    note_category = models.CharField(max_length=200, default='', choices=CATEGORIES)
    slug = models.SlugField(blank=True, default='')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.note_category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.note_category)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('note:show_note_by_category', args=[self.slug])