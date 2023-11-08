
# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.utils import timezone
from django.urls import reverse
from projects.models import Project


class Feature (models.Model):
    """Model representing a product feature."""
    
    name = models.CharField(max_length=200, help_text='Enter a product feature (e.g. Fan Kitchen-cabinet wardropes)')

    class meta :
        verbose_name_plural = 'Features' 


    def __str__(self):
        """String for representing the Model object."""
        return self.name



class Product(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=250, null= True, blank= True)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title_document = models.CharField(max_length=250, null= True, blank= True)
    description = models.CharField(max_length= 250, null= True, blank=True)
    # Foreign Key used because product can only have one project, but project can have multiple products
  
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    specification = models.CharField(max_length=300, help_text='Enter a brief specification of the product')
    location = models.CharField(max_length=300, help_text="Enter a the product location")
    bedrooms = models.PositiveIntegerField(null= True, blank=True)
    bathrooms= models.PositiveIntegerField(null= True, blank=True)
    payment_duration = models.PositiveIntegerField(help_text="Enter a number in months e.g 18")
    available_units = models.PositiveIntegerField(null= True, blank=True)
    features = models.ManyToManyField(Feature, help_text='Select a feature for this product')
    outright_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the outright payment price", default= 0, null= True, blank=True)
    mortgage_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the mortgage payment price",  default= 0, null= True, blank=True)
    installmental_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter installmental payment price",  default= 0, null= True, blank=True)
    featured_image= models.ImageField(upload_to="images/", default=True)
   
    floor_area = models.PositiveBigIntegerField(help_text="Enter the net floor area for the product")
    
    SALES_STATUS = (
        ('Sold Out', 'Sold Out'),
        ('Now Selling', 'Now Selling'),
        ('On Request', 'On Request'),
        ('Not Available', 'Not Available'),
    )

    sales = models.CharField(
        max_length=50,
        choices= SALES_STATUS,
        blank=True,
        default='Now Selling',
        help_text='Product sales status',
    )

    TYPE_STATUS = (
         ('Land', 'Land'),
        ('Building', 'Building'),
    )
    
    type = models.CharField(
        max_length=50,
        choices= TYPE_STATUS,
        blank=True,
        default='Building',
        help_text='Product type status',
    )

    class meta :
        ordering = ['-name']
        verbose_name = 'Products'


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    



class ProductPhoto (models.Model):

    """Model representing a project Photo."""
    product= models.ForeignKey(Product, on_delete= models.CASCADE, related_name="prodphoto")
    image= models.ImageField(upload_to='images/')

    class meta :
            ordering = ['-image'] 
            verbose_name = 'ProdPhotos'

    
    def __str__(self):
            """String for representing the Model object."""
            return self.image