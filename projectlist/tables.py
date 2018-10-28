from table import Table
from table.columns import Column


from .models import projects


class projectTable(Table):
	id = Column(field='id')
	name = Column(field='name')
	class meta:
		model = projects
