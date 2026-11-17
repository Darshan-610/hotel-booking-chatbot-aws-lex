import random

PRICES = {"classic": 2500, "deluxe": 3500, "duplex": 5000, "suite": 8000}

def lambda_handler(event, context):
    intent = event["sessionState"]["intent"]
    slots = intent["slots"]

    def val(name):
        return slots[name]["value"]["interpretedValue"]

    room = val("RoomType")
    date = val("CheckInDate")
    nights = int(float(val("Nights")))
    guests = val("Guests")
    name = val("GuestName")

    price_per_night = PRICES.get(room.lower(), 2500)
    total = price_per_night * nights
    booking_id = "HTL" + str(random.randint(10000, 99999))

    message = (
        f"Booking confirmed, {name}!\n"
        f"Booking ID: {booking_id}\n"
        f"Room type: {room}\n"
        f"Check-in date: {date}\n"
        f"Duration of stay: {nights} night(s)\n"
        f"Guests: {guests}\n"
        f"Price per night: Rs.{price_per_night}\n"
        f"Total price: Rs.{total}\n"
        f"Thank you for choosing us!"
    )

    intent["state"] = "Fulfilled"
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": intent
        },
        "messages": [{"contentType": "PlainText", "content": message}]
    }