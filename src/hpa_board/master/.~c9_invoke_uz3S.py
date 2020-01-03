from django.contrib.auth.models import AbstractUser
from django.db import models

from hpa_board.models import BaseModelMixin


class Team(AbstractUser):
    username = models.CharField('チーム名', max_length=30, unique=True)
    email = models.EmailField('連絡先')
    REQUIRED_FIELDS = ['']
    
    TEAM_TYPE_STUDENT = 1
    TEAM_TYPE_ADULT = 2
    TEAM_TYPE_CHOICES = (
        (TEAM_TYPE_STUDENT, '学生'),
        (TEAM_TYPE_ADULT, '社会人'),
    )
    team_type = models.PositiveIntegerField(
        'チーム種別', choices=TEAM_TYPE_CHOICES, default=TEAM_TYPE_STUDENT
    )


class News(BaseModelMixin):
    from_team = models.ForeignKey(Team, verbose_name='発信チーム', on_delete=models.CASCADE)
    contents = models.TextField('内容')
    send_date = models.DateTimeField('送信予定日時')
    NEWS_STATUS_DRAFT = 1
    NEWS_STATUS_SEND = 2
    NEWS_STATUS_SENDED = 3
    NEWS_STATUS_CHOICES = (
        (NEWS_STATUS_DRAFT, '下書き'),
        (NEWS_STATUS_SEND, '送信予定'),
        (NEWS_STATUS_SENDED, '送信済'),
    )
    news_status = models.PositiveIntegerField(
        'ステータス', choices=NEWS_STATUS_CHOICES, default=NEWS_STATUS_DRAFT
    )
