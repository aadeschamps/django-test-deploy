from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):

	posts = Post.objects.filter(author=request.user)

	return render(request, 
		'blog/post_list.html', 
		{
			'posts': posts
		}
	)