from django.test import TestCase

from account.models import User 
users = User.objects.all()
users
#<QuerySet []>