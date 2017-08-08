from django.core.management.base import BaseCommand, CommandError
from summerforprogress.models import Representative

class Command(BaseCommand):
    help = 'Saves all representatives to regenerate their score'

    def handle(self, *args, **options):
        representatives = Representative.objects.all()
        
        for rep in representatives:
            rep_name = rep.first + ' ' + rep.last + ' ' + rep.state + ' ' + rep.district
            
            rep.save()

            self.stdout.write(self.style.SUCCESS('Successfully saved representative "%s"' % rep_name))
