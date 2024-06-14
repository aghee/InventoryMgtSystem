from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("register/",views.registerUser,name="register"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("create-prod/",views.createProduct,name="create-product"),
    path("product/<str:pk>/",views.ProductDetail.as_view(),name="product-detail"),
    path("update-prod/<str:pk>/",views.updateProduct,name="update-product"),
    path("delete-prod/<str:pk>/",views.deleteProduct,name="delete-product"),
    path("order/<str:pk>/",views.specific_order,name="order"),
    path("create-order/",views.createOrder,name="create-order"),
    path("update-order/<str:pk>/",views.updateOrder,name="update-order"),
    path("orderdetail/<str:pk>/",views.OrderDetail.as_view(),name="order-detail"),
    path("delete-order/<str:pk>/",views.deleteOrder,name="delete-order"),
    
]
