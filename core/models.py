from django.db import models
import uuid
import datetime

# Models Mixins
class CreatedUpdatedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Event(CreatedUpdatedModelMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    holder_name = models.CharField('Anfitrião(ões)', max_length=250, null=True)
    slug = models.SlugField('Url', max_length=255, null=False, unique=True)
    event_name = models.CharField('Nome do Evento', max_length=150, null=False)
    event_date = models.DateTimeField('Data do Evento', null=True)
    event_location = models.CharField('Local', max_length=255, null=True)
    is_active = models.BooleanField('Exibir Página', default=False)

    class Meta:
        db_table = 'events'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return "%s - %s" % (self.event_name, self.event_date)


class GiftList(CreatedUpdatedModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=255, null=False)

    event = models.ForeignKey('Event', related_name='gift_lists', on_delete=models.CASCADE)

    class Meta:
        db_table = 'gift_lists'
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'

    def __str__(self):
        return "%s" % self.name


class Gift(CreatedUpdatedModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=100, null=False)
    description = models.CharField('Descrição', max_length=255, null=True)
    is_active = models.BooleanField('Mostrar na lista', default=False)

    gift_list = models.ForeignKey('GiftList', related_name='gifts', on_delete=models.CASCADE)

    class Meta:
        db_table = 'gifts'
        verbose_name = 'Presente'
        verbose_name_plural = 'Presentes'

    def __str__(self):
        return "%s" % self.name
