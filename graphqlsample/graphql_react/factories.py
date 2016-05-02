import factory
from . import models


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Address

    city = factory.sequence(lambda n: 'city%d' % n)
    postcode = factory.sequence(lambda n: 'postcode%d' % n)


class CustomerFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Customer

    address = factory.SubFactory(AddressFactory)


class LoanFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Loan

    user = factory.SubFactory(CustomerFactory)

