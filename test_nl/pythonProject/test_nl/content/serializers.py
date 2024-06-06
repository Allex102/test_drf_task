from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from .models import Page, Content, Video, Audio, Text


class PageSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        exclude = ("id",)

    def get_detail_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(obj.get_absolute_url())
        return None


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ("title", "order", "counter", "bitrate")


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("title", "video_url", "subtitle_url", "counter")


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = (
            "title",
            "some_text",
            "counter",
        )


class ContentPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Audio: AudioSerializer,
        Text: TextSerializer,
        Video: VideoSerializer,
    }


class PageDetailSerializer(serializers.ModelSerializer):
    content = ContentPolymorphicSerializer(
        many=True,
    )

    class Meta:
        model = Page
        fields = ("title", "content")
