from django.conf import settings
from django.db import models
from django.urls import reverse


class BoardPost(models.Model):
    title = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='board_posts',
        verbose_name='작성자',
    )
    created_at = models.DateTimeField('작성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시간', auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board_detail', args=[self.pk])
