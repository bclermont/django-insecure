# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
            parser.add_argument(
                '--username',
                help='Specifies the username for the superuser.'
            )
            parser.add_argument(
                '--email',
                help='Specifies the email address for the superuser.'
            )
            parser.add_argument(
                '--password',
                help='Specify superuser password.'
            )
            parser.add_argument(
                '--ignore_existing',
                type=bool,
                help='Do not fail if user already exists'
            )

    def handle(self, *args, **options):
        for key in ('password', 'username', 'email'):
            if key not in options:
                raise CommandError('Missing --%s' % key)
        options['interactive'] = 0
        try:
            User.objects.create_superuser(options['username'], options['email'],
                                          options['password'])
        except IntegrityError, err:
            if not options['ignore_existing']: 
                raise err
