import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangol2ex.settings')

import django
django.setup()
from exapp.models import User

from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        ffn = fake_name[0]
        fln = fake_name[1]
        fake_email = fakegen.email()
        fuser = User.objects.get_or_create(first_name=ffn,last_name=fln, email = fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
