from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.utils import timezone
from django.urls import reverse



class ProjectFacility (models.Model):
    """Model representing a project facilities."""

    name = models.CharField(max_length=200, help_text='Enter a product feature (e.g. Swimming-pool CCTV Solar-power)')

    class meta :
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Category (models.Model):
    name =  models.CharField( max_length=50, default='Residential', help_text='Project purpose',)

    class meta :
            ordering = ['-name']
            verbose_name = 'Categories'

    def __str__(self):
        """String for representing the Model object."""
        return self.name



class Project (models.Model):
        """Model representing a project."""

        name = models.CharField(max_length=250)


        description = models.TextField(max_length=1000, help_text='Enter a brief description of the project')
        location = models.CharField(max_length=300)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        # hectares = models.DecimalField(max_digits=6, decimal_places=1, help_text="Enter the number of hectares",null=True, blank=True,)
        featured_image= models.ImageField(upload_to="images/", default=True)
        client = models.CharField(max_length=250, blank=True, null=True)
        facilities = models.ManyToManyField(ProjectFacility, help_text='Select a feature for this project')
        category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

        PROJECT_STATUS = (
        ('Not started', 'Not started'),
        ('Inprogress', 'Inprogress'),
        ('Completed', 'Completed'),
    )

        status = models.CharField(
        max_length=50,
        choices= PROJECT_STATUS,
        blank=True,
        default='Not started',
        help_text='Project work status',
    )


        class meta :
            ordering = ['-name']
            verbose_name = 'Projects'


        def __str__(self):
            """String for representing the Model object."""
            return self.name

        def get_absolute_url(self):

            """Returns the URL to access a detail record for this project."""
            return reverse('project_detail', args=[str(self.id)])



class ProjectPhoto (models.Model):

    """Model representing a project Photo."""
    project= models.ForeignKey(Project, on_delete= models.CASCADE, related_name="projphoto")
    image= models.ImageField(upload_to='images/')

    class meta :
            ordering = ['-image']
            verbose_name = 'ProjPhotos'


    # def __str__(self):
    #         """String for representing the Model object."""
    #         return self.image