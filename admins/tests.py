from datetime import date

from django.test import TestCase
from .models import Person, Group, Membership

# Create your tests here.
class TestAdmin(TestCase):
    def setUp(self) -> None:
        ...
    
    def tearDown(self) -> None:
        Group.objects.all().delete()
        Person.objects.all().delete()
        Membership.objects.all().delete()
    
    def test_many_to_many(self):

        john = Person.objects.create(name='john')
        paul = Person.objects.create(name='paul')
        ringo = Person.objects.create(name='ringo')
        
        beatles = Group.objects.create(name='The beatles')

        beatles.members.add(john, through_defaults={
            "date_joined": date(1960, 8,1)
        })
        print('all persons should be 3')
        print(Person.objects.all())
        print('all beatles members shoule be 1')
        print(beatles.members.all())
        print('***')

        beatles.members.create(name='George Harrison', through_defaults={
            "date_joined": date(1960, 8,1)
        })

        print('all persons should be 4')
        print(Person.objects.all())
        print('all beatles members shoule be 2 - george, john')
        print(beatles.members.all())
        print('***')

        beatles.members.set([paul, ringo], through_defaults={
            "date_joined": date(1960, 8,1)
        })

        print('all persons should be 4')
        print(Person.objects.all())
        print('all beatles members shoule be 2, paul, ringo')
        print(beatles.members.all())
        print('***')

        beatles.members.remove(ringo)

        x = Person.objects.filter(
            group__name='The beatles',
            membership__date_joined__gte=date(1960, 8,1)
        )
    
        print('all persons should be 4')
        print(Person.objects.all())
        print('all beatles members shoule be 1 - paul')
        print(x)
        print('***')