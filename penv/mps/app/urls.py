from django.urls import path
from app import views

urlpatterns = [
    
    #url for Home 
    path('home/',views.home_page,name='home'),
    
    #urls for CRUD Division
    path('division/',views.read_division,name='division'),
    path('create/',views.create_division,name='create'),
    path('division/update',views.update_division,name='update'),
    path('division/<id>/delete',views.delete_division,name='delete'),
    path('division/<id>/restore',views.restore_division,name='restore'),

    #urls for CRUD Material
    path('product/<product>/material/',views.material,name='material'),
    path('product/<product>/creatematerial',views.create_material,name='creatematerial'),
    path('product/updatematerial',views.update_material,name='updatematerial'),
    path('product/<id>/deletematerial',views.delete_material,name='deletematerial'),
    path('product/<id>/restoremateriale',views.restore_material,name='restoremateriale'),
    #Get Global Materials
    path('materials/',views.read_material,name='materials'),
   
    #urls for Calendar
    path('product/<product>/calendar/',views.calendar,name='calendar'),
    path('product/<product>/createcalendar/',views.create_calendar,name='createcalendar'),
    path('product/<product>/deleteday/',views.delete_day,name='deleteday'),

    #urls for Duplicate Calendar
    path('product/<product>/duplicatecalendar/',views.duplicate_calendar,name='duplicatecalendar'),

    #urls for copy calendar from product
    path('product/<product>/copycalendar/',views.copy_calendar,name='copycalendar'), 
    
    #urls for Custom Calendar
    path('product/<product>/customcalendar/',views.custom_calendar,name='customcalendar'),
    path('product/<product>/createcustomcalendar/',views.create_custom_calendar,name='createcustomcalendar'),
    path('product/<product>/deletedaycustom/',views.delete_day_custom,name='deletedaycustom'),
    
    #urls for CRUD product
    path('division/<division>/product/',views.product,name='product'),
    path('division/<division>/createproduct',views.create_product,name='createproduct'),
    path('division/updateproduct',views.update_product,name='updateproduct'),
    path('division/<id>/deleteproduct',views.delete_product,name='deleteproduct'),
    path('division/<id>/restoreproduct',views.restore_product,name='restoreproduct'),

    #urls for work data
    path('product/<product>/workdata/',views.work_data,name='workdata'),
    
    #urls for custom work data
    path('product/<product>/customwork/',views.custom_work,name='customwork'),
    
    #urls for CRUD CalendarConfigurationTraitement
    path('product/<product>/configTrait/',views.config_trait,name='configTrait'),
    path('product/<product>/createconfigTrait',views.create_conf_trait,name='createconfigTrait'),
    path('product/updateconfigTrait',views.update_conf_trait,name='updateconfigTrait'),
    path('product/<id>/deleteconfigTrait',views.delete_conf_trait,name='deleteconfigTrait'),
    path('product/<id>/restoreconfigTrait',views.restore_conf_trait,name='restoreconfigTrait'),
    
    
    #urls for CRUD CalendarConfigurationCpordo
    path('product/<product>/configCpordo/',views.config_cpordo,name='configCpordo'),
    path('product/<product>/createconfigCpordo',views.create_conf_cpordo,name='createconfigCpordo'),
    path('product/updateconfigCpordo',views.update_conf_cpordo,name='updateconfigCpordo'),
    path('product/<id>/deleteconfigCpordo',views.delete_conf_cpordo,name='deleteconfigCpordo'),
    path('product/<id>/restoreconfigCpordo',views.restore_conf_cpordo,name='restoreconfigCpordo'),
    
    #urls for upload files
    path('files/upload',views.upload_files,name='uploadfiles'), 
    path('files/savecoois',views.save_coois,name='savecoois'),
    path('files/savezpp',views.save_zpp,name='savezpp'), 
    
    #url for shopfloor
    path('shopfloor/',views.Shopfloor,name='shopfloor'), 
    
     
    
    
   
]
