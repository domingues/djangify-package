from . import django_manage  # noqa: F401, I001

from .models import Post, Comment

number_of_posts = Post.objects.count()
number_of_comments = Comment.objects.count()

print(f"Number of posts: {number_of_posts}")
print(f"Number of comments: {number_of_comments}")
