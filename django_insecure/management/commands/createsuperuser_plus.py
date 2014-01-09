# -*- coding: utf-8 -*-

from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--username', dest='username', default=None,
                    help='Specifies the username for the superuser.'),
        make_option('--email', dest='email', default=None,
                    help='Specifies the email address for the superuser.'),
        make_option('--password', dest='password', default=None,
                    help='Specify superuser password.')
    )

    def handle(self, *args, **options):
        for key in ('password', 'username', 'email'):
            if key not in options:
                raise CommandError('Missing --%s' % key)
        options['interactive'] = 0
        User.objects.create_superuser(options['username'], options['email'],
                                      options['password'])
