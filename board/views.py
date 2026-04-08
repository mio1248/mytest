from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BoardPostForm
from .models import BoardPost


def _get_editable_post(request, post_id):
    post = get_object_or_404(BoardPost.objects.select_related('author'), id=post_id)
    if request.user != post.author and not request.user.is_superuser:
        raise PermissionDenied
    return post


@login_required
def board_list(request):
    posts = BoardPost.objects.select_related('author')
    return render(request, 'board/board_list.html', {'posts': posts})


@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board_detail', post_id=post.id)
    else:
        form = BoardPostForm()

    return render(request, 'board/board_create.html', {'form': form})


@login_required
def board_detail(request, post_id):
    post = get_object_or_404(BoardPost.objects.select_related('author'), id=post_id)
    can_manage = request.user == post.author or request.user.is_superuser
    return render(request, 'board/board_detail.html', {'post': post, 'can_manage': can_manage})


@login_required
def board_update(request, post_id):
    post = _get_editable_post(request, post_id)

    if request.method == 'POST':
        form = BoardPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('board_detail', post_id=post.id)
    else:
        form = BoardPostForm(instance=post)

    return render(request, 'board/board_edit.html', {'form': form, 'post': post})


@login_required
def board_delete(request, post_id):
    post = _get_editable_post(request, post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('board_list')

    return redirect('board_detail', post_id=post.id)
