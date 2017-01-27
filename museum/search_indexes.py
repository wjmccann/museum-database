from haystack import indexes
from .models import *

class CollectionIndex (indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	
	def get_model(self):
		return Collection
		
class ItemIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	
	def get_model(self):
		return Item