import csv
import datetime
from app.models import squirrel
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('squirrel_file')
    def handle(selfself,*args,**options):
        file=options['squirrel_file']
        with open(file) as fp:
            reader=csv.DictReader(fp)
            for item in reader:
                obj=squirrel()
                obj.latitude=item['X']
                obj.longitude=item['Y']
                obj.id=item['Unique Squirrel ID']
                obj.shift=item['Shift']
                obj.date=datetime.strptime('%m%d%y',item['Date']).date()
                obj.age=item['Age']
                obj.save()

