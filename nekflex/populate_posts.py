# populate_posts.py
import os
from django.core.files import File
from accounts.models import CustomUser
from blog.models import Category, Post

# Get the superuser (or first user)
user = CustomUser.objects.first()

# Create categories
categories = ['Action', 'Drama', 'Comedy', 'Horror', 'Sci-Fi']
cat_objs = {}
for cat in categories:
    cat_objs[cat], _ = Category.objects.get_or_create(name=cat)

# Create posts
sample_posts = [
    {
        'title': 'Epic Adventure',
        'category': 'Action',
        'content': 'An epic journey across mountains and seas.',
        'featured_image': 'media/posts/post1.jpg',
        'is_featured': True
    },
    {
        'title': 'Love in Paris',
        'category': 'Drama',
        'content': 'A heartfelt story of love and loss.',
        'featured_image': 'media/posts/post2.jpg',
        'is_featured': False
    },
    {
        'title': 'Laugh Out Loud',
        'category': 'Comedy',
        'content': 'Comedy gold with endless laughs.',
        'featured_image': 'media/posts/post3.jpg',
        'is_featured': False
    },
    {
        'title': 'Nightmare Alley',
        'category': 'Horror',
        'content': 'A spine-chilling tale you will never forget.',
        'featured_image': 'media/posts/post4.jpg',
        'is_featured': False
    },
    {
        'title': 'Future World',
        'category': 'Sci-Fi',
        'content': 'A thrilling journey into the unknown future.',
        'featured_image': 'media/posts/post5.jpg',
        'is_featured': False
    }
]

for post_data in sample_posts:
    post, created = Post.objects.get_or_create(
        title=post_data['title'],
        author=user,
        category=cat_objs[post_data['category']],
        content=post_data['content'],
        status='published',
        is_featured=post_data['is_featured']
    )
    # Attach image if exists
    img_path = post_data['featured_image']
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            post.featured_image.save(os.path.basename(f.name), File(f), save=True)

print("✅ Sample posts created successfully!")
