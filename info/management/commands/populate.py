from django.core.management.base import BaseCommand, CommandError
from info.models import User,ActivityPeriod
import datetime,string,random,pytz,time
from tqdm import tqdm
from django.conf import settings


class Command(BaseCommand):

    def handle(self,*args,**options):
        
        for i in tqdm(range(50)):
            full_name = ''.join(random.choices(string.ascii_uppercase, k = 6)) 
            timzone= pytz.all_timezones[random.randint(0,563)]
            
            z = User.objects.create(real_name=full_name,tz = timzone)
            
            for j in range(random.randint(1,3)):
                s_time = datetime.datetime.utcnow()+ datetime.timedelta(hours=random.randint(1,100))
                f_time = s_time+datetime.timedelta(hours=random.randint(1,100))
                x = ActivityPeriod.objects.create(related_to=z,start_time=s_time,finish_time=f_time )


            


           