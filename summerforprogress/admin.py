from django.contrib import admin

from models import *

@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    exclude = ()
    
    list_display = ('first','last','score','state','district','healthcare','college_tuition','minimum_wage','wall_street','womens_rights','voting_rights','justice','climate','last_updated')
    
    search_fields = ('first','last','state','district')
    
    readonly_fields = ('score',)

    # def get_actions(self, request):
    #     actions = super(RepresentativeAdmin, self).get_actions(request)
    #     del actions['delete_selected']
    #     return actions
