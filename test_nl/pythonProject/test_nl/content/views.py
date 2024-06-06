from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.db import models, transaction


from .tasks import increment_counter
from .models import Page
from .serializers import (
    PageSerializer,
    PageDetailSerializer,
)


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)


class PageDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        """Для брокера сообщений"""
        # increment_counter.delay(instance.id)
        with transaction.atomic():
            for content in instance.content.all():
                content.counter = models.F("counter") + 1
                content.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
