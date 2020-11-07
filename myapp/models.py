from django.db import models

# Create your models here.
#for saving data

#create categories model
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title
    
#create Image Model
class Image(models.Model):
    title=models.CharField(max_length=200)  
    description=models.TextField()  
    image=models.ImageField(upload_to='images')
    added_data=models.DateTimeField()
    #cascade delete means when we delete category it will delete related information
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

