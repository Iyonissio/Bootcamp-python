import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primeiro_projecto.settings')

import django

django.setup()

import random
from primeira_app.models import Paginaweb, Topic, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.name()
        fake_date = fakegen.date()

        pagnaweb = Paginaweb.objects_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects_or_create(name=pagnaweb, date=fake_date)[0]


if __name__ == '__main__':
    print("Population Script")
    populate(20)
    print("Complete Population")
