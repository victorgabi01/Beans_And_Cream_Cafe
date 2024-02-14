from django.urls import path
from app_beans_and_cream_cafe.views import home_view, contact, ProductListView, product_detail, upload_product, add_to_cart, delete_product, shopping_cart, finalizeaza_comanda


# in acest fisier definim rutele specifice aplicatie nostre sweet_market_place
app_name = 'app_beans_and_cream_cafe'  # in cadrul variabilei app_name salvam numele aplicatiei unde am definit url-urile specifice aplicatie nostre
                                      # ne vom folosi de acest nume cand vom  gestiona url-urile in sabloanele(fisierele html)

urlpatterns = [
    path('', home_view, name='home'),
    path('upload_product/', upload_product, name='upload-product'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>/', product_detail, name='product'),
    path('cart/', shopping_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('finalizeaza_comanda/', finalizeaza_comanda, name='finalizeaza_comanda'),
    path('contact/', contact, name='contact'),

    ]

