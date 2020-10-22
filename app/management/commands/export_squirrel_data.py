import csv
import datetime
from app.models import squirrel
from django.core.management.base import BaseCommand,CommandError
class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('squirrel_file')
    def handle(selfself,*args,**options):
        file=options['squirrel_file']
        with open(file,'w') as fp:
            writer=csv.DictWriter(fp)
            objs=squirrel.objects.get()
            for obj in objs:
                writer.writerow({'X':obj[0]},{'Y':obj[1]},{'Unique Squirrel ID':obj[2]},{'Shift':obj[3]},{'Date':obj[4]},{'Age':obj[5]})


