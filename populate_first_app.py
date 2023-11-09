import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_app.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import django 
django.setup 

##FAKE POP SCRIPT

import random

from first_app.models import Topic,AccessRecord,WebPage 
from faker import Faker 

fakegen = Faker() 
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t 

def populate(N=5):
    
    for entry in range(N):
        
        #get the topic for the entry
        top = add_topic()
        
        fake_url = fakegen.url()
        fake_date = fakegen.date() 
        fake_name = fakegen.company()
        webpg = WebPage.objects.get_or_create(topic = top ,url = fake_url,name = fake_name)[0]
        
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('Populating complet')
        
