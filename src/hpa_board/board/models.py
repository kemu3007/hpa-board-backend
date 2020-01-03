from django.db import models

from hpa_board.models import BaseModelMixin
from hpa_board.master.models import Team


class Event(BaseModelMixin):
    name = models.CharField('イベント名', max_length=20)
    admin_team = models.ForeignKey(Team, verbose_name='主催チーム', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField('開始日時', null=True, blank=True)
    end_datetime = models.DateTimeField('終了日時', null=True, blank=True)
    application_start_datetime = models.DateTimeField('募集開始日時', null=True, blank=True)
    application_end_datetime = models.DateTimeField('募集締切日時', null=True, blank=True)
    place = models.CharField('場所', max_length=50)
    meeting_place = models.CharField('集合場所', max_length=50)
    details = models.TextField('詳細', null=True, blank=True)


class Application(BaseModelMixin):
    event = models.ForeignKey(Event, verbose_name='イベント', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name='チーム', on_delete=models.CASCADE)
    people_num = models.PositiveIntegerField('申し込み人数')
    remarks = models.TextField('備考')
 