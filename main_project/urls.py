"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reservation_app.views import AddRoomView, MainPage, AllRoomsView, SpecificRoom, ModifyRoom, DeleteRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', MainPage.as_view(), name='main_page_view'),
    path('room/new/', AddRoomView.as_view(), name='add_room_view'),
    path('room/all/', AllRoomsView.as_view(), name='all_rooms_view'),
    path('room/<int:room_id>/', SpecificRoom.as_view(), name='specific_room_view'),
    path('room/modify/<int:room_id>/', ModifyRoom.as_view(), name='modify_room_view'),
    path('room/delete/<int:room_id>/', DeleteRoom.as_view(), name='delete_room_view'),
    path('room/reserve/<int:room_id>/', ReserveRoom.as_view(), name='reserve_room_view'),
]
