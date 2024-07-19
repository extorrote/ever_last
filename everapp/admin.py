from django.contrib import admin

# Register your models here.

from .models import property
# Register your models here.
from .models import Recommendation

from .models import Restaurant_Recommendation,Bar_Recommendation,tour_Recommendation,GalleryRecommendation


# CONFIGURACION EXTRA
class propertyadmin(admin.ModelAdmin):
    name = 'everapp'
    readonly_fields=('created','updated')
    search_fields=('id', 'price','bedrooms','property_type','location','development_name','pre_construction','pet_friendly','primary_view')#ACA LE INDICO POR QUE CAMPOS QUIERO QUE ME BUSQUE LOS ELEMENTOS 
    list_filter=('status',) #ESTO ME SACA A LA DERECHA UNA SESION PARA SELECCIONAR SI ES VISIBLE O NO
    list_display=('id', 'price','bedrooms','property_type','location','development_name','pre_construction','primary_view','imagen1','imagen2','imagen3','imagen4','imagen5','imagen6','imagen7','imagen8') #ESTO ES LAS COLUMNAS  QUE QUIERO QUE ME MUESTRE CUANDO LAS BUSCO
    ordering=('created',) #SIN LA COMA AL ULTIMO NO FUNCIONA

admin.site.register(property,propertyadmin) #ACA E DEBO PASAR MI METODO PARA PODER QUE SE CARGUE 
title="Panel De Gestion de Propiedades Ever"
subtitle="Panel de Gestion"
admin.site.site_header=title #ESTE TAMBIEN SALE EN LA PESTAÑA DEL NAVEGADOR
admin.site.site_title=title #ESTE ES EL TITULO QUE APARECE EN LA PESTAÑA DEL NAVEGADOR 
admin.site.index_title="properties Puerto vallarta"


admin.site.register(Recommendation) #ACA E DEBO PASAR MI METODO PARA PODER QUE SE CARGUE 
title="Reviews"
subtitle="Panel de Gestion Reviews"
admin.site.site_header=title #ESTE TAMBIEN SALE EN LA PESTAÑA DEL NAVEGADOR
admin.site.site_title=title #ESTE ES EL TITULO QUE APARECE EN LA PESTAÑA DEL NAVEGADOR 
admin.site.index_title="Recommendations"


admin.site.register(Restaurant_Recommendation) #ACA E DEBO PASAR MI METODO PARA PODER QUE SE CARGUE 
title=" Restaurant Recommendations"
subtitle="Panel de Gestion Restaurant Recommendations"
admin.site.site_header=title #ESTE TAMBIEN SALE EN LA PESTAÑA DEL NAVEGADOR
admin.site.site_title=title #ESTE ES EL TITULO QUE APARECE EN LA PESTAÑA DEL NAVEGADOR 
admin.site.index_title="Restaurant Recommendations"


admin.site.register(Bar_Recommendation) #ACA E DEBO PASAR MI METODO PARA PODER QUE SE CARGUE 
title=" Bar Recommendations"
subtitle="Panel de Gestion Bar Recommendations"
admin.site.site_header=title #ESTE TAMBIEN SALE EN LA PESTAÑA DEL NAVEGADOR
admin.site.site_title=title #ESTE ES EL TITULO QUE APARECE EN LA PESTAÑA DEL NAVEGADOR 
admin.site.index_title="Bar Recommendations"


admin.site.register(tour_Recommendation) #ACA E DEBO PASAR MI METODO PARA PODER QUE SE CARGUE 
title=" tour Recommendations"
subtitle="Panel de Gestion tour Recommendations"
admin.site.site_header=title #ESTE TAMBIEN SALE EN LA PESTAÑA DEL NAVEGADOR
admin.site.site_title=title #ESTE ES EL TITULO QUE APARECE EN LA PESTAÑA DEL NAVEGADOR 
admin.site.index_title="Tour Recommendations"


admin.site.register(GalleryRecommendation) #ACA E DEBO PASAR MI METODO PARA PODER QUE SE CARGUE 
title=" Gallery Recommendations"
subtitle="Panel de Gestion Gallery Recommendations"
admin.site.site_header=title #ESTE TAMBIEN SALE EN LA PESTAÑA DEL NAVEGADOR
admin.site.site_title=title #ESTE ES EL TITULO QUE APARECE EN LA PESTAÑA DEL NAVEGADOR 
admin.site.index_title="Gallery Recommendations"




