from django.db import models

# Create your models here.


class Designation (models.Model):

    """Model representing a project Photo."""
    name = models.CharField(max_length=200)
    
    class meta :
            ordering = ['-name'] 
            verbose_name = 'Designations'

    
    def __str__(self):
            """String for representing the Model object."""
            return self.name
        
        

class Team (models.Model):

    """Model representing a Team Members."""
    name= models.CharField(max_length=100)
    title = models.CharField(max_length=250) 
    designation= models.ForeignKey(Designation, on_delete= models.CASCADE, related_name="teamDesignation")
    phone_number=models.CharField(max_length=12, blank=True, null=True)
    yrs_of_experience= models.SmallIntegerField(blank=True, null=True)
    twitter= models.URLField(blank=True, null=True)
    facebook= models.URLField(blank=True, null=True)
    instagram= models.URLField(blank=True, null=True)
    linkedin= models.URLField(blank=True, null=True)
    picture= models.ImageField(upload_to='images/')

    class meta :
            ordering = ['-image'] 
            verbose_name = 'ProdPhotos'

    
    def __str__(self):
            """String for representing the Model object."""
            return self.name
        

class Text(models.Model):

    """Model representing a project Photo."""
    team= models.ForeignKey(Team, on_delete= models.CASCADE, related_name="teamText")
    paragraph= models.TextField()

    class meta :
            ordering = ['-image'] 
            verbose_name = 'Texts'

    
    def __str__(self):
            """String for representing the Model object."""
            return self.paragraph