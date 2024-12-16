from django.contrib import admin

from main_app.models import Student

# Register your models here.
admin.site.site_header = "St Anthony's High School"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "dob", "is_sporty", "kcpe_score"]
    search_fields = ["first_name", "last_name", "kcpe_score"]
    list_filter = ["is_sporty"]
    list_per_page = 25


admin.site.register(Student, StudentAdmin)
