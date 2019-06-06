from py2neo.ogm import GraphObject, Property, RelatedTo


class User(GraphObject):
	__primarykey__ = 'email'

	name = Property()
	email = Property()

	products = RelatedTo('Product', 'BOUGHT')
	receipts = RelatedTo('Receipt', 'HAS')
	stores = RelatedTo('Store', 'GOES_TO')
