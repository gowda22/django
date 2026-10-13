
from django.contrib import admin
from .models import Cource, Student,User,Profile,Actor,Movies


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')  # display data
    search_fields = ('name',)  # search based on feature
    list_filter = ('course',)  # filter


class CourceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display=( 'actor_name','age','experence')
    list_filter=('age','experence')
    search_fields=('actor_name',)
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):

    list_display=('movie_name','realize_year')
    list_filter=('realize_year',)
    search_fields=('movie_name','actors__actor_name')
    filter_horizontal=('actors',)
    
    





admin.site.register(Cource, CourceAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.register(User)
admin.site.register(Profile)

