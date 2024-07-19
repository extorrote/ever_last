
from .models import property
from .forms import PropertyForm
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from .models import Recommendation
from .forms import RecommendationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from .forms import RegisterForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate,login,logout
from .utils import notify_users  # Import your notification function

from django.db.models import Q # ESTO LO IMPORTE PARA EL METODO DEL BUSCADOR
from .forms import PropertySearchForm 




#AQUI ESTOY MOSTRANDO TODAS LAS PROPIEDADES
def index(request):
     articulos= property.objects.all()

     return render(request,'index.html',{'articulos':articulos})
 
 

#######################ESTO ES PARA QUE CADA PROPIEDAD TENGA SU LINK  ######################
def property_link(request, pk):
    prop = get_object_or_404(property, pk=pk)

    return render(request, 'share_property.html', {'property': prop})
    






def about(request):
    return render(request,'about.html')






def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            new_property = form.save()  # Save the new property object
            property_url = request.build_absolute_uri(reverse('property_detail', args=[new_property.id]))
            notify_users(new_property, property_url)  # Notify users with property details and URL
            return redirect('home')  # Replace with your success URL
    else:
        form = PropertyForm()
    
    return render(request, 'add_property.html', {'form': form})




def property_search(request):
    query = request.GET.get('q')

    if query:
        properties = property.objects.filter(
            Q(id__icontains=query) |
            Q(price__icontains=query) |
            Q(property_size__icontains=query) |
            Q(bedrooms__icontains=query) |
            Q(bathrooms__icontains=query) |
            Q(property_type__icontains=query) |
            Q(property_status__icontains=query) |          
            Q(agent_name__icontains=query) |
            Q(status__icontains=query) |
            Q(location__icontains=query) |
            Q(development_name__icontains=query) |
            Q(pre_construction__icontains=query) |
            Q(pet_friendly__icontains=query) |
            Q(primary_view__icontains=query)
            
        )
    else:
        properties = property.objects.all()

    context = {
        'properties': properties,
        'query': query,
    }
    return render(request, 'index.html', context)



def set_appointment(request):
    return render(request,'appointment_request.html')





def submit_review(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews_list')
    else:
        form = RecommendationForm()
    
    return render(request, 'submit_review.html', {'form': form})


def reviews_list(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'reviews_list.html', {'recommendations': recommendations})



def portfolio(request):
    return render(request,'portfolio.html')


def faq(request):
    return render(request,'faq.html')




from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Process the form data, e.g., send an email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Message: {message}\nPhone: {phone}\nEmail: {email}',
                'wwwstephen95live@gmail.com',  # From email
                ['wwwstephen95live@gmail.com'],  # To email
                fail_silently=False,
            )
            
            
            messages.success(request, 'Email Sent! (Mensaje Enviado)')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})



########################## PRINCIPIO REGISTROUSUARIO ##############################



def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.is_active = False
                user.save()

                # Generate uidb64 and token
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)

                # Build activation URL
                current_site = get_current_site(request)
                protocol = 'https' if request.is_secure() else 'http'
                domain = current_site.domain
                activate_url = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})

                # Complete activation URL
                activation_link = f'{protocol}://{domain}{activate_url}'

                # Render activation email
                mail_subject = 'Activate your account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'activation_link': activation_link,
                })
                to_email = register_form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.content_subtype = 'html'
                email.send()

                messages.success(request, 'Email Confirmed! Now You Can Login')
                return redirect('activation_sent')

        return render(request, 'registro.html', {
            'register_form': register_form
        })



User = get_user_model()

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # Optionally log in the user after activation
        # login(request, user)
        return redirect('home')  # Redirect to home page after activation
    else:
        return render(request, 'activation_invalid.html')







def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid Login Credentials or Email not Confirmed.')
            return render(request, 'login.html')

    return render(request, 'login.html')


######################## FINAL REGISTRO USUARIO ############################33  
def activation_sent(request):
    return render(request, 'activation_sent.html')

def logout_user(request):
    logout(request)
    return redirect ('home')


####################################   RESTAURANTS RECOMENDATION SECTION ########################################
from .models import Restaurant_Recommendation
from .forms import Restaurant_RecommendationForm

def restaurant_recommendation_list(request):
    places = Restaurant_Recommendation.objects.all()
    return render(request, 'restaurant_recommendation_list.html', {'places': places})

def restaurant_recommendation_link_to_share(request, pk):
    place = Restaurant_Recommendation.objects.get(pk=pk)
    return render(request, 'restaurant_recommendation_detail.html', {'place': place})

def restaurant_recommendation_create(request):
    if request.method == 'POST':
        form = Restaurant_RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant_recommendation_list')
    else:
        form = Restaurant_RecommendationForm()
    return render(request, 'place_recommendation_form.html', {'form': form})



def restaurant_recommendation_edit(request, pk):
    place = Restaurant_Recommendation.objects.get(pk=pk)
    if request.method == 'POST':
        form = Restaurant_RecommendationForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('restaurant_recommendation_list')
    else:
        form = Restaurant_RecommendationForm(instance=place)
    return render(request, 'place_recommendation_form.html', {'form': form})


####################################   BAR RECOMENDATION SECTION ########################################
from .models import Bar_Recommendation
from .forms import Bar_RecommendationForm

def bar_recommendation_list(request):
    places = Bar_Recommendation.objects.all()
    return render(request, 'bar_recommendation_list.html', {'places': places})

def bar_recommendation_link_to_share(request, pk):
    place = Bar_Recommendation.objects.get(pk=pk)
    return render(request, 'bar_recommendation_detail.html', {'place': place})

def bar_recommendation_create(request):
    if request.method == 'POST':
        form = Bar_RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bar_recommendation_list')
    else:
        form = Bar_RecommendationForm()
    return render(request, 'place_recommendation_form.html', {'form': form})



def bar_recommendation_edit(request, pk):
    place = Bar_Recommendation.objects.get(pk=pk)
    if request.method == 'POST':
        form = Bar_RecommendationForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('bar_recommendation_list')
    else:
        form = Bar_RecommendationForm(instance=place)
    return render(request, 'place_recommendation_form.html', {'form': form})




####################################   tour RECOMENDATION SECTION ########################################
from .models import tour_Recommendation
from .forms import tour_RecommendationForm

def tour_recommendation_list(request):
    places = tour_Recommendation.objects.all()
    return render(request, 'tour_recommendation_list.html', {'places': places})

def tour_recommendation_link_to_share(request, pk):
    place = tour_Recommendation.objects.get(pk=pk)
    return render(request, 'tour_recommendation_detail.html', {'place': place})

def tour_recommendation_create(request):
    if request.method == 'POST':
        form = tour_RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tour_recommendation_list')
    else:
        form = tour_RecommendationForm()
    return render(request, 'tour_recommendation_form.html', {'form': form})



def tour_recommendation_edit(request, pk):
    place = tour_Recommendation.objects.get(pk=pk)
    if request.method == 'POST':
        form = tour_RecommendationForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('tour_recommendation_list')
    else:
        form = tour_RecommendationForm(instance=place)
    return render(request, 'tour_recommendation_form.html', {'form': form})


####################################   Gallery RECOMENDATION SECTION ########################################
from .models import GalleryRecommendation
from .forms import GalleryRecommendationForm

def gallery_recommendation_list(request):
    places = GalleryRecommendation.objects.all()
    return render(request, 'gallery_recommendation_list.html', {'places': places})

def gallery_recommendation_link_to_share(request, pk):
    place = GalleryRecommendation.objects.get(pk=pk)
    return render(request, 'gallery_recommendation_detail.html', {'place': place})

def gallery_recommendation_create(request):
    if request.method == 'POST':
        form = GalleryRecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_recommendation_list')
    else:
        form = GalleryRecommendationForm()
    return render(request, 'gallery_recommendation_form.html', {'form': form})



def gallery_recommendation_edit(request, pk):
    place = GalleryRecommendation.objects.get(pk=pk)
    if request.method == 'POST':
        form = GalleryRecommendationForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('gallery_recommendation_list')
    else:
        form = GalleryRecommendationForm(instance=place)
    return render(request, 'gallery_recommendation_form.html', {'form': form})




def author(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Process the form data, e.g., send an email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Message: {message}\nPhone: {phone}\nEmail: {email}',
                'wwwstephen95live@gmail.com',  # From email
                ['wwwstephen95live@gmail.com'],  # To email
                fail_silently=False,
            )
            
            
            messages.success(request, 'Email Sent! (Mensaje Enviado)')
            return redirect('web_developer_puerto_vallarta')
    else:
        form = ContactForm()

    return render(request, 'paginas_web_puerto_vallarta.html', {'form': form})




def attorney(request):
    return render(request,'attorney.html') 



