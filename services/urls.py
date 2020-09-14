from django.urls import path
from . import views
from . import api

urlpatterns = [
    # path('',views.ListInvoiceView.as_view(),name = 'details'),
    # path('add/',views.CreateInvoiceView.as_view(),name = 'add'),
    # path('<pk>/edit/',views.UpdateInvoiceView.as_view(),name = 'put'),    

    path('',views.service,name='service'),

    path('plan/', views.plan, name = 'plan'),
    path('plan/<pk>/', views.planinfo, name = 'planinfo'),
    path('create_plan/', views.CreatePlan, name = 'createplan'),
    path('update_plan/<pk>/', views.updatePlan, name = 'updateplan'),
    path('delete_plan/<pk>/',views.deletePlan,name='delete_plan'),


    path('serv/', views.serv, name = 'serv'),
    path('serv/<pk>/', views.servinfo, name = 'servinfo'),
    path('create_service/', views.CreateService, name = 'createservice'),
    path('update_service/<pk>', views.updateService, name = 'updateservice'),
    path('delete_service/<pk>/',views.deleteService,name='delete_service'),

    path('prod/', views.product, name = 'prod'),
    path('prod/<pk>/', views.prodinfo, name = 'prodinfo'),
    path('create_product/', views.CreateProduct, name = 'createproduct'),
    path('update_product/<pk>', views.updateProduct, name = 'updateproduct'),
    path('delete_product/<pk>/',views.deleteProduct,name='delete_product'),


]


