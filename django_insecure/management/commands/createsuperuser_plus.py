# -*- coding: utf-8 -*-

from optparse import make_option
from django.contrib.auth.management.commands import createsuperuser
from django.core.management.base import CommandError
from django.contrib.auth.models import User

class Command(createsuperuser.Command):
    option_list = createsuperuser.Command.option_list + (
        make_option('--password', dest='password', default=None,
                    help='Specify superuser password.'),
    )

    def handle(self, *args, **options):
        password = options.get('password', None)
        # force interactive, force --user
        options['interactive'] = True
        if not password:
            raise CommandError("Missing --password")
        createsuperuser.Command.handle(self, *args, **options)
        user = User.objects.get(username=options.get('username'))
        user.set_password(password)
        user.save()
