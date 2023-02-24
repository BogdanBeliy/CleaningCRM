from django.db import models


class LeadStatus(models.TextChoices):
    NEW = 'new', 'Новая'
    IN_PROCESSING = 'in_processing', 'В обработке'
    TO_WORK = 'to_work', 'В работу'
    CANCEL = 'cancel', 'Отмена'
    DONE = 'done', 'Выполнена'


