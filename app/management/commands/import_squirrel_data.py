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
                obj.date=datetime.date(int(item['Date'][-4:]), int(item['Date'][:2]), int(item['Date'][2:4]))
                obj.age=item['Age']
                obj.primary_fur_color=item['Primary Fur Color']
                obj.location=item['Location']
                obj.specific_location=item['Specific Location']
                obj.running=item['Running'].capitalize()
                obj.chasing=item['Chasing'].capitalize()
                obj.climbing=item['Climbing'].capitalize()
                obj.eating=item['Eating'].capitalize()
                obj.foraging=item['Foraging'].capitalize()
                obj.other_Activities=item['Other Activities']
                obj.kuks=item['Kuks'].capitalize()
                obj.quaas=item['Quaas'].capitalize()
                obj.moans=item['Moans'].capitalize()
                obj.tail_flags=item['Tail flags'].capitalize()
                obj.tail_twitches=item['Tail twitches'].capitalize()
                obj.approaches=item['Approaches'].capitalize()
                obj.indifferent=item['Indifferent'].capitalize()
                obj.runs_From=item['Runs from'].capitalize()
                obj.save()

