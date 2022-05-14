from django.urls import path
from .import views
from .views import(
    VipPostDetailView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, TrandingVipPostDetailView, TrandingPostDetailView,
    SearchView
)

urlpatterns = [
    #path('', views.index, name='index'),
    path('', PostListView.as_view(), name='index'),

    path('about/', views.about, name='about'),
    path('page-not-found/', views.PageNotFound, name='pagenotfound'),
    path('contact/', views.contact, name='contact'),
    path('mahabharata-war/', views.mahabharata, name='mahabharata-war'),
    path('karna-war/', views.karna, name='karna-war'),
    path('role-of-military/', views.military, name='role-of-military'),
    path('shivaji-maharaj-warfare/', views.shiva, name='shivaji-maharaj-warfare'),

    path('search/', SearchView.as_view(), name='search'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('vippost/<int:pk>/', VipPostDetailView.as_view(), name='vip-post-detail'),
    
    path('tranding-vip-post/<int:pk>/', TrandingVipPostDetailView.as_view(), name='tranding-vip-post-detail'),
    path('tranding-post/<int:pk>/', TrandingPostDetailView.as_view(), name='tranding-post-detail'),

    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
