from django.urls import path
from main.views import create_product_flutter, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register 
from main.views import login_user
from main.views import logout_user
from main.views import tambah_item 
from main.views import kurangi_item
from main.views import hapus_item
from main.views import get_product_json, add_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tambah_item/<int:id>/', tambah_item, name='tambah_item'),
    path('kurangi_item/<int:id>/', kurangi_item, name='kurangi_item'),
    path('hapus_item/<int:id>/', hapus_item, name='hapus_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]