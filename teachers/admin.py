from django.contrib import admin

from teachers.models import Teacher


class GroupsInlineTable(admin.TabularInline):

    model = Teacher.group_teachers.through
    fields = ['get_group_name', 'get_group_start', 'get_group_end']
    readonly_fields = fields
    extra = 0

    def get_group_name(self, instance):
        return instance.group.group_name

    get_group_name.short_description = 'Group name'

    def get_group_start(self, instance):
        return instance.group.start_date

    get_group_name.short_description = 'Group name'

    def get_group_end(self, instance):
        return instance.group.end_date

    get_group_name.short_description = 'Group name'
    get_group_start.short_description = 'Start date'
    get_group_end.short_description = 'End date'

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Teacher)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary',)
    list_display_links = list_display
    list_per_page = 25

    fieldsets = (
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Born', {'fields': (('birthdate', 'get_age'),)}),
        ('Contact', {'fields': (('email', 'city'),)}),
    )

    inlines = [
        GroupsInlineTable,
    ]

    def get_age(self, instance):
        return f'{instance.get_age()} year(s)'

    get_age.short_description = 'Age'
    readonly_fields = ('get_age',)
