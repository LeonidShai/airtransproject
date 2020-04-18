from django.http import HttpResponse
from airtrans.models import *

def queries(request):

    aircraft_seats = Seat.objects.all().filter(aircraft_code=123)
    flight = Flight.objects.all().filter(depar_airport__airport_name="Pulkovo",
                                         arriv_airport__airport_name="Domodedovo").exclude(status="otlozhen")
    board_pass = BoardPas.objects.all().filter(flight_id__flight_id__aircraft_code__model="yak140")
    passname = TicketFlight.objects.all().filter(flight_id=378)

    d = str()
    d += f"<h3>a. Список рейсов между двумя аэропортами (Пулково - Домодедово)</h3>"
    for i in range(len(flight)):
        d += f"<p>{i+1}. {flight[i]}</p>"

    d += f"<h3>b. Список мест для выбранного самолёта: Yak-140</h3>"
    for i in range(len(aircraft_seats)):
        d += f"<p>{i+1}. {aircraft_seats[i]}</p>"

    d += f"<h3>c. Список выданных посадочных талонов для выбранного перелёта (Пулково - Домодедово)</h3>"
    for i in range(len(board_pass)):
        d += f"<p>Билет на место {board_pass[i].seat_no} выдан</p>"

    d += f"<h3>d. Список имён пассажиров данного рейса (Пулково - Домодедово)</h3>"
    for i in range(len(passname)):
        d += f"<p>{i+1}. {passname[i].ticket_no.passenger_name}</p>"

    return HttpResponse(d)
