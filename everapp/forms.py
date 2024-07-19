from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators 
from .models import Restaurant_Recommendation,Bar_Recommendation,tour_Recommendation,GalleryRecommendation
from .models import property
class PropertyForm(forms.ModelForm):
    class Meta:
        model = property
        fields = '__all__'  # Use all fields from the Property model
        labels = {
            'price': 'Price',
            'property_size': 'Property Size',
            'bedrooms': 'Bedrooms',
            'bathrooms': 'Bathrooms',
            'property_type': 'Property Type',
            'property_status': 'Property Condition',
            'agent_name': 'Agent Name',
            'status': ' Status',
            'location': 'Location',
            'pre_construction': 'Pre Construction',
            'development_name': 'Development Name',
            'pet_friendly': 'Pet Friendly',
            'primary_view': 'Primary View',
            'imagen1': 'Image 1',
            'imagen2': 'Image 2',
            'imagen3': 'Image 3',
            'imagen4': 'Image 4',
            'imagen5': 'Image 5',
            'imagen6': 'Image 6',
            'imagen7': 'Image 7',
            'imagen8': 'Image 8',
            'video':'Video',
            'water':'Water',
            'stories':'Stories',
            'furnished':'Furnished',
            'comunity':'Comunity',
            'swer':'Swer',
            'walls':'Walls',
            'road_type':'Road type',
            'electricity':'Electricity',
            'unit_details':'Unit details',
            'amenities':'Amenities',
            'appliances':'Appliences',
            'oven':'Oven',
            'range':'Range',
            'air_conditioning':'Air Conditioning',
            'water_heater': 'Water Heater',
            'hoa': 'HOA',
            'info':'Info',
            'hoa_info':'HOA info',
            'google_maps': 'Google Maps Location',         
        }
        widgets = {
            'google_maps': forms.Textarea(attrs={'rows': 5}),
        }
        
    
    
    

        
################ BUSCADOR ##########################       
class PropertySearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    
    
from .models import Recommendation

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['name', 'email', 'recommendation','imagen']
        labels={'imagen': 'image'}
        widgets = {
            'google_maps': forms.Textarea(attrs={'rows': 5}),
        }

from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()    
    phone = forms.CharField(
        max_length=15, 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    message = forms.CharField(widget=forms.Textarea)



class RegisterForm(UserCreationForm):
    class Meta:
        model =User
        fields=['username','email','first_name','last_name','password1','password2' ]#PARA VER QUE CAMPOS LE PUEDO PONER AQUI PUEDO VERLOS EN EL auth_user   DEL dbrowser 







class Restaurant_RecommendationForm(forms.ModelForm):
    class Meta:
        model = Restaurant_Recommendation
        fields = '__all__'  # To include all fields of the model        
        labels={
            'place_name':'Place Name',
            'thematic':'Type of Food',
            'range_of_price': 'Range of Price',
            'title_h1': 'Title for Description',
            'description': 'Description',
            'address': 'Address',
            'imagen1': 'Image 1',
            'imagen2': 'Image 2',
            'imagen3': ' Image 3',
            'imagen4': 'Image 4',
            
        }
        widgets = {
            'google_maps': forms.Textarea(attrs={'rows': 5}),
        }
        
        

class Bar_RecommendationForm(forms.ModelForm):
    class Meta:
        model = Bar_Recommendation
        fields = '__all__'  # Use all fields from the Property model
        labels = {
            'place_name': 'Place Name',
            'thematic': 'Thematic',
            'range_of_price': 'Range of Price',
            'title_h1': 'Title for Description',
            'description': 'Description',
            'address': 'Address',
            'imagen1': 'Image 1',
            'imagen2': 'Image 2',
            'imagen3': ' Image 3',
            'imagen4': 'Image 4',
            
        }
        widgets = {
            'google_maps': forms.Textarea(attrs={'rows': 5}),
        }
        


class tour_RecommendationForm(forms.ModelForm):
    class Meta:
        model = tour_Recommendation
        fields = '__all__'  # Use all fields from the Property model
        labels = {
            'type_of_tour': 'Type of tour',
            'tour_name': 'Tour Name',
            'tour_company_name': 'Tour Company Name',
            'email': 'Company Email',
            'price': ' Range of Price',
            'company_address':'Company Address',
            'description': 'Any Tour Description',
            'imagen1': 'Image 1',
            'imagen2': 'Image 2',
            'imagen3': 'Image 3',
            'imagen4': 'Image 4',
            
        }
        widgets = {
            'google_maps': forms.Textarea(attrs={'rows': 5}),
        } 
        
        
        
class GalleryRecommendationForm(forms.ModelForm):
        class Meta:
            model = GalleryRecommendation
            fields = '__all__'  # Use all fields from the Property model
            labels = {
                'gallery_name': 'Gallery Name',
                'kind_of_art': 'Kiend of Art',
                'range_of_price': 'Range of Price',
                'title_h1': 'Description Title',
                'description': ' Description',
                'address':'Address',
                'phone_number':'Phone Number',
                'days_open': 'Days and Hors Open',
                'days_closed':'Days Closed',
                'imagen1': 'Image 1',
                'imagen2': 'Image 2',
                'imagen3': 'Image 3',
                'imagen4': 'Image 4',
                
            }
            widgets = {
            'google_maps': forms.Textarea(attrs={'rows': 5}),
        } 
            

            
