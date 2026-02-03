class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add these if you want to use them in your forms
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=(('draft','Draft'), ('published','Published')))
    featured_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
