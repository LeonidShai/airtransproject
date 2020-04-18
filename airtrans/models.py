from django.db import models

# Create your models here.

class Booking(models.Model):
    book_ref = models.SlugField(max_length=10, primary_key=True)
    book_date = models.DateField()
    total_amount = models.FloatField()

    def __str__(self):
        return f"{self.book_ref} -- {self.total_amount}, {self.book_date}"


class Ticket(models.Model):
    ticket_no = models.PositiveIntegerField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=50)
    contact_data = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.ticket_no}, {self.passenger_name}, {self.book_ref}"


class Airport(models.Model):
    airport_code = models.SlugField(primary_key=True, max_length=10)
    airport_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.airport_code}, {self.airport_name}, {self.city}"


class Aircraft(models.Model):
    aircraft_code = models.SlugField(primary_key=True, max_length=10)
    model = models.CharField(max_length=10)
    range = models.IntegerField()
    seat_q = models.PositiveIntegerField()

    def __str__(self):
        return f"Aircraft: {self.model} -- {self.range}"


class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    flight_no = models.IntegerField()
    schedul_depar = models.DateTimeField()
    schedul_arriv = models.DateTimeField()
    depar_airport = models.ForeignKey(Airport, related_name="departure_airport",
                                      on_delete=models.CASCADE)
    arriv_airport = models.ForeignKey(Airport, related_name="arrival_airport",
                                      on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    actual_depar = models.CharField(max_length=10, blank=True)
    actual_arriv = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.depar_airport} - {self.arriv_airport}, {self.schedul_depar} - {self.schedul_arriv}"


class TicketFlight(models.Model):
    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    fare_condition = models.CharField(max_length=10)
    amount = models.IntegerField()

    class Meta:
        unique_together = (('ticket_no', 'flight_id'))

    def __str__(self):
        return f"{self.flight_id}, {self.amount}"


class Seat(models.Model):
    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    seat_no = models.SlugField(max_length=10, unique=True)
    fare_condition = models.CharField(max_length=10)

    class Meta:
        unique_together = (('aircraft_code', 'seat_no'))

    def __str__(self):
        return f"{self.seat_no}, {self.fare_condition}"


class BoardPas(models.Model):
    ticket_no = models.OneToOneField(TicketFlight, related_name="bp_ticket",
                                     on_delete=models.CASCADE)
    flight_id = models.OneToOneField(TicketFlight, related_name="bp_flight",
                                     on_delete=models.CASCADE)
    boarding_no = models.IntegerField()
    seat_no = models.SlugField(max_length=10, unique=True)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'))

    def __str__(self):
        return f"{self.boarding_no}, {self.seat_no}"
