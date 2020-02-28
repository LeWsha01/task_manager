import argparse
import csv
import datetime
import os

from django.core import management
from django.conf import settings

from dashboard import models

FIELD_NAMES = [
    'name',
    'description',
    'created_at',
    'reported__username',
    'assigne__username',
    'deadline',
]


def _validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        msg = f"Invalid date {date_str}"
        raise argparse.ArgumentTypeError(msg)


class Command(management.BaseCommand):
    help = 'Help text'

    def add_arguments(self, parser):
        parser.add_argument(
            '-fd',
            '--fromdate',
            required=True,
            type=_validate_date
        )
        parser.add_argument(
            '-td',
            '--todate',
            required=True,
            type=_validate_date
        )

    def handle(self, *args, **options):
        issues = (
            models.Issue.objects
            .filter(
                created_at__gte=options['fromdate'],
                created_at__lte=options['todate']
            )
            .values(*FIELD_NAMES)
        )

        file = os.path.abspath(
            os.path.join(os.path.dirname(
                settings.BASE_DIR), '..', 'export.csv'))

        with open(file, 'w') as f:
            writer = csv.DictWriter(f, delimiter='|', fieldnames=FIELD_NAMES)
            writer.writeheader()
            for i in issues:
                writer.writerow(i)
