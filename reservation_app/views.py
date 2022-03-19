from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

from reservation_app.models import Room, ReservationStatus

# Create your views here.


class MainPage(View):
    def get(self, request):
        return render(request, 'menu_layout.html')


class AddRoomView(View):
    def get(self, request):
        return render(request, 'add_room_form.html')

    def post(self, request):
        name = request.POST.get('roomName')
        size = request.POST.get('roomSize')
        # return None if checkbox is not checked / return 'True' if checkbox is checked (value parameter in HTML)
        projector_available = request.POST.get('projectorAvailable')
        pa = True if projector_available == 'True' else False

        if name is False:
            return HttpResponse('Wrong data! - name can not be empty')

        all_rooms = Room.objects.all()
        for room in all_rooms:
            if name == room.name:
                return HttpResponse('Wrong data! - name is already in data base')

        if int(size) < 1:
            return HttpResponse('Wrong data! - size has to be positive value')

        # save given room to database
        Room.objects.create(name=name, size=size, projector_available=pa)

        return redirect(reverse('main_page_view'))


class AllRoomsView(View):
    def get(self, request):
        all_rooms = Room.objects.all()
        reservations = ReservationStatus.objects.all()
        if not all_rooms:
            return HttpResponse('There is no rooms in data base')

        for room in all_rooms:
            reservation_dates = [reservation.date for reservation in room.reservations.all()]
            room.reserved = date.today() in reservation_dates

        context = {
            'all_rooms': all_rooms,
        }

        return render(request, 'rooms_list_form.html', context=context)


class SpecificRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        reservation_info = ReservationStatus.objects.filter(room_id=room_id)
        context = {
            'room': room,
            'reservation_info': reservation_info,
        }
        return render(request, 'specific_room_form.html', context=context)


class ModifyRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        context = {'room': room}
        return render(request, 'modify_room_form.html', context=context)

    def post(self, request, room_id):
        name = request.POST.get('roomName')
        size = request.POST.get('roomSize')
        # return None if checkbox is not checked / return 'True' if checkbox is checked (value parameter in HTML)
        projector_available = request.POST.get('projectorAvailable')
        pa = True if projector_available == 'True' else False

        if name is False:
            return HttpResponse('Wrong data! - name can not be empty')

        all_rooms = Room.objects.all()
        for room in all_rooms:
            if name == room.name:
                return HttpResponse('Wrong data! - name is already in data base')

        if int(size) < 1:
            return HttpResponse('Wrong data! - size has to be positive value')

        specific_room = Room.objects.get(pk=room_id)
        specific_room.name = name
        specific_room.size = size
        specific_room.projector_available = pa
        specific_room.save()

        return redirect(reverse('all_rooms_view'))


class DeleteRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        room.delete()
        return redirect(reverse('all_rooms_view'))


class ReserveRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        context = {'room': room}
        return render(request, 'reserve_room_form.html', context=context)

    def post(self, request, room_id):
        comment = request.POST.get('comment')
        date_from_url = request.POST.get('date')
        reservations = ReservationStatus.objects.filter(room_id=room_id, date__exact=date_from_url)

        if len(reservations) >= 1:
            return HttpResponse('Reservation for this day already exist!')

        actual_date = date.today()
        date_to_compare_str = date_from_url
        year = int(date_to_compare_str[0:4])
        month = int(date_to_compare_str[5:7])
        day = int(date_to_compare_str[8:10])
        date_to_compare = date(year, month, day)
        dif = (date_to_compare - actual_date).days
        if dif < 0:
            return HttpResponse('date is from the past!')

        # save given room to database
        ReservationStatus.objects.create(date=date_from_url, comment=comment, room_id=room_id)

        return redirect(reverse('all_rooms_view'))
