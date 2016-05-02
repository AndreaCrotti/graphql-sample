import graphene
from graphene import relay, resolve_only_args
from graphene.contrib.django import DjangoNode, DjangoObjectType

from . import models

schema = graphene.Schema(name='Sample user loan schema')


class Customer(DjangoNode):
    class Meta:
        model = models.Customer

    @classmethod
    def get_node(cls, id, info):
        return Customer(models.Customer.objects.get(id))


class Query(graphene.ObjectType):
    customers = graphene.Field(Customer)


schema.register(Query)

schema.query = Query

