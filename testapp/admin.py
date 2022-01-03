from django.contrib import admin

from testapp.models import Record, DataType


class RecordInline(admin.StackedInline):
    model = Record
    extra = 0


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_type', 'value', 'recorded_date')


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RecordInline]
