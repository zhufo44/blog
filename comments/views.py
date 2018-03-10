from django.shortcuts import render,redirect,get_object_or_404
from myblog.models import Post

from .models import Comment
from .form import CommentForm

def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'myblog/detail.html',context=context)
    return redirect(post)

# Create your views here.
