from restaurant.models import Booking

from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist == True:
            raise serializers.ValidationError(
                "This reservation date + time are already taken, pealse select another time or date"
            )

        return data
