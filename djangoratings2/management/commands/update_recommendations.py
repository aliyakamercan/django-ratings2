from django.core.management.base import NoArgsCommand, CommandError

from djangoratings2.models import SimilarUser

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        SimilarUser.objects.update_recommendations()
