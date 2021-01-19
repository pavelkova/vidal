import graphene
from graphene_django impot DjangoOjectType
from graphql_jwt.decorators import login_required

from users.schema import UserType
from .models import Card

class CardType(DjangoObjectType):
    class Meta:
        model = Card

class Query(graphene.ObjectType):
    card = graphene.Field(CardType, id=graphene.ID())
    cards = graphene.List(CardType)
    # cards_by_page
    # cards_by_date

    def resolve_card(self, info, id):
        return Card.objects.get(id=id)

    def resolve_cards(self, info, **kwargs):
        return Card.objects.all()

    def resolve_cards_by_date(self, info, date):
        return Cards.objects.filter(date=date)

class CreateCard(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()

    class Arguments:
        title = graphene.String()

        @login_required
        def mutate(self, info, title):
            user = info.context.user or None

            card = Card(title=title, user=user)
            card.save()

            return CreateCard(id=card.id, title=card, user=user)

class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
