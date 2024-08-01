
from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views

from .views import (home_page_view, user_only_view, staff_member_required)
from checkout import views as checkout_views

from subscriptions import views as subscriptions_views

urlpatterns = [
    path('', home_page_view, name='home'),
    # path('login/', auth_views.login_view),
    # path('register/', auth_views.register_view),
    path('checkout/sub-price/<int:price_id>',
         checkout_views.product_price_redirect_view, name="sub-price-checkout"),
    path('checkout/start/',
         checkout_views.checkout_redirect_view, name="stripe-checkout-start"),
    path('checkout/success/', checkout_views.checkout_finalize_view,
         name='stripe-checkout-end'),
    path('pricing/', subscriptions_views.subscription_price_view, name='pricing'),
    path('pricing/<str:interval>/',
         subscriptions_views.subscription_price_view, name='pricing_interval'),
    path('accounts/billing/', subscriptions_views.user_subscription_view,
         name="user_subscription"),
    path('accounts/', include('allauth.urls')),
    path('accounts/billing/', subscriptions_views.user_subscription_view,
         name='user_subscription'),
    path('accounts/billing/cancel', subscriptions_views.user_subscription_cancel_view,
         name='user_subscription_cancel'),
    path('protected/user-only/', user_only_view, name='user_only'),
    path('protected/staff-only/', staff_member_required, name='user_only'),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
