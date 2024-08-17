from django.core.management.base import BaseCommand, CommandError
from uuid import uuid4
from core.models import User

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    
    def add_arguments(self, parser):
        # positional arg
        parser.add_argument("total",  type=int, help="total_users")
        # optional arg
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )
        # flag / boolean
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')
        # arbitary list of args
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **options):
        total = options['total']
        prefix = options['prefix'] or 'user_'
        admin = options['admin']
        users_ids = options['user_id']
        for i in range(total):
            User.objects.create_user(str(uuid4()))
                