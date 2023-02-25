from django import forms
from django.contrib import admin

from groups.models import Group


class StudentsInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = fields
    show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = ['get_first_name', 'get_last_name', 'get_salary']
    readonly_fields = fields
    extra = 0

    def get_first_name(self, instance):
        return instance.teacher.first_name

    def get_last_name(self, instance):
        return instance.teacher.last_name

    def get_salary(self, instance):
        return instance.teacher.salary

    get_first_name.short_description = 'First name'
    get_last_name.short_description = 'Last name'
    get_salary.short_description = 'Salary'

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman'].choices = [(s.pk, f'{s.first_name} {s.last_name}') for s in self.instance.students.all()]
        self.fields['headman'].choices.insert(0, (0, '-------'))

        self.fields['headman'].widget.can_add_related = False
        self.fields['headman'].widget.can_change_related = False
        self.fields['headman'].widget.can_view_related = False
        self.fields['headman'].widget.can_delete_related = False


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = ('group_name', 'start_date', 'end_date', 'headman')
    fields = (
        'group_name',
        ('start_date', 'end_date'),
        'headman',
        ('created', 'updated')
    )

    readonly_fields = ('created', 'updated')
    inlines = [
        StudentsInlineTable,
        TeachersInlineTable
    ]
