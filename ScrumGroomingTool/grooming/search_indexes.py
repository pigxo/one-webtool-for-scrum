import datetime
from grooming.models  import Grooming  
from haystack import indexes  

class GroomingIndex(indexes.SearchIndex, indexes.Indexable):  
    text = indexes.CharField(document=True, use_template=True) 
    Title = indexes.CharField(model_attr='title') 
    Sprint = indexes.CharField(model_attr='sprint') 
    Feature = indexes.CharField(model_attr='feature')    

    def get_model(self):  
        return Grooming  
    def index_queryset(self,using=None):  
        """Used when the entire index for model is updated."""    
        return self.get_model().objects.all() 