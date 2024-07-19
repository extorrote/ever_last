from django.db import models



from django.utils.timezone import now
# Create your models here.

class property(models.Model):
    price=models.CharField(max_length=50,null=True,blank=True)
    property_size=models.CharField(max_length=40, null=True,blank=True)
    bedrooms=models.CharField(max_length=50,null=True,blank=True)
    bathrooms=models.CharField(max_length=50, null=True,blank=True)
    property_type=models.CharField(max_length=200,null=True,blank=True)
    property_status=models.CharField(max_length=50, null=True,blank=True)
    
    agent_name=models.CharField(max_length=50, null=True,blank=True)
    status=models.CharField(max_length=50, null=True,blank=True)
    location=models.CharField(max_length=50, null=True,blank=True)
    
    
    pre_construction=models.CharField(max_length=50, null=True,blank=True)
    development_name=models.CharField(max_length=50, null=True,blank=True)
    pet_friendly=models.CharField(max_length=50, null=True,blank=True)
    primary_view=models.CharField(max_length=50, null=True,blank=True)
    imagen1=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen2=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen3=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen4=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen5=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen6=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen7=models.ImageField(upload_to='everapp',null=True,blank=True)
    imagen8=models.ImageField(upload_to='everapp',null=True,blank=True)
    video= models.FileField(upload_to='everapp',null=True,blank=True)
    water=models.CharField(max_length=500, null=True,blank=True)
    stories=models.CharField(max_length=150, null=True,blank=True)
    furnished=models.CharField(max_length=150, null=True,blank=True)
    comunity=models.CharField(max_length=150, null=True,blank=True)
    sewer=models.CharField(max_length=150, null=True,blank=True)
    walls=models.CharField(max_length=150, null=True,blank=True)
    road_type=models.CharField(max_length=150, null=True,blank=True)
    electricity=models.CharField(max_length=150, null=True,blank=True)
    unit_details=models.CharField(max_length=150, null=True,blank=True)
    amenities=models.CharField(max_length=150, null=True,blank=True)
    appliances=models.CharField(max_length=250, null=True,blank=True)
    oven=models.CharField(max_length=150, null=True,blank=True)
    range=models.CharField(max_length=150, null=True,blank=True)
    air_conditioning=models.CharField(max_length=150, null=True,blank=True)
    water_heater=models.CharField(max_length=150, null=True,blank=True)
    hoa=models.CharField(max_length=250, null=True,blank=True)
    info=models.CharField(max_length=250, null=True,blank=True)
    hoa_info=models.CharField(max_length=250, null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    google_maps = models.CharField(max_length=500, null=True, blank=True)
    
    
    def get_object_url(self):
        
        return f'/property/{self.id}/'
    
    class Meta:
        verbose_name='property'
        verbose_name_plural='properties'
        #ACA LE PUEDO PONER EL order_by
        def __str__ (self):
                return self.agent_name or 'Unnamed Agent'




class Recommendation(models.Model):
    imagen=models.ImageField(upload_to='everapp',null=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    recommendation = models.TextField()

    class Meta:
        verbose_name = ' Review '
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.name  or 'Unnamed '      
        
        

class Restaurant_Recommendation(models.Model):
    place_name = models.CharField(max_length=200, null=True, blank=True)
    thematic = models.CharField(max_length=200, null=True, blank=True)
    range_of_price = models.CharField(max_length=100, null=True, blank=True)
    title_h1 = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=6000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)  # Corrected 'adress' to 'address'
    imagen1 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='everapp', null=True, blank=True)
    google_maps = models.CharField(max_length=500, null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Recommend Restaurant'
        verbose_name_plural = 'Recommend Restaurants'

    def __str__(self):
        return self.place_name or 'Unnamed Restaurant'
    
    
    
    
class Bar_Recommendation(models.Model):
    
    place_name = models.CharField(max_length=200,  null=True, blank=True)
    thematic = models.CharField(max_length=200, null=True, blank=True)
    range_of_price = models.CharField(max_length=100, null=True, blank=True)
    title_h1 = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=6000, null=True, blank=True)
    
    address = models.CharField(max_length=200, null=True, blank=True)  # Corrected 'adress' to 'address'
    imagen1 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='everapp', null=True, blank=True)
    google_maps = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'recommend bar'
        verbose_name_plural = 'recommend bars'

    def __str__(self):
        return self.place_name or 'Unnamed Place'
    



class tour_Recommendation(models.Model):
    type_of_tour= models.CharField(max_length=200,  null=True, blank=True)
    tour_name = models.CharField(max_length=200, null=True, blank=True)
    tour_company_name = models.CharField(max_length=200,  null=True, blank=True)  
    email = models.EmailField(blank=True) 
    price = models.CharField(max_length=100, null=True, blank=True)    
    description = models.TextField(max_length=6000, null=True, blank=True)    
    company_address = models.CharField(max_length=200, null=True, blank=True)  # Corrected 'adress' to 'address'
    meet_up_at=models.CharField(max_length=200, null=True, blank=True)
    imagen1 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='everapp', null=True, blank=True)
    google_maps = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'recommend tour'
        verbose_name_plural = 'recommend tours'

    def __str__(self):
        return self.tour_name  or 'Unnamed tour'  
    


class GalleryRecommendation(models.Model):
    gallery_name = models.CharField(max_length=200,  null=True, blank=True)
    kind_of_art = models.CharField(max_length=200, null=True, blank=True)
    range_of_price = models.CharField(max_length=100, null=True, blank=True)
    title_h1 = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=6000, null=True, blank=True)   
    phone_number=models.CharField(max_length=200, null=True, blank=True)  
    address = models.CharField(max_length=200, null=True, blank=True)  
    days_open=models.CharField(max_length=300, null=True, blank=True)  
    days_closed=models.CharField(max_length=300, null=True, blank=True)  
    imagen1 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='everapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='everapp', null=True, blank=True)
    google_maps = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'recommend Gallery'
        verbose_name_plural = 'recommend Galleries'

    def __str__(self):
        return self.gallery_name or 'Unnamed Gallery'
    


