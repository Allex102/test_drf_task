from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline

from .models import Page, Content, Video, Audio, Text


class ContentInline(StackedPolymorphicInline):
    class TextInline(
        StackedPolymorphicInline.Child,
    ):
        readonly_fields = ("counter",)
        model = Text

    class VideoInline(StackedPolymorphicInline.Child):
        readonly_fields = ("counter",)
        model = Video

    class AudioInline(
        StackedPolymorphicInline.Child,
    ):
        readonly_fields = ("counter",)
        model = Audio

    model = Content
    child_inlines = (
        AudioInline,
        TextInline,
        VideoInline,
    )


@admin.register(Page)
class PageAdmin(SortableAdminMixin, PolymorphicInlineSupportMixin, admin.ModelAdmin):
    extra = 0
    fields = ["title", "is_active"]
    search_fields = ["title"]
    inlines = [
        ContentInline,
    ]
