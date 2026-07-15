import logging
from flask import Flask, render_template, request


logging.basicConfig(
    filename="hotel_bookings.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: float, max_guests: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.is_available = True

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights: int) -> float:
        return self.price_per_night * nights

    def __str__(self):
        status = "თავისუფალი" if self.is_available else "დაკავებული"
        return f"ოთახი {self.room_number} ({self.room_type}) - {self.price_per_night}GEL/ღამე | სტატუსი: {status}"


class Customer:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room: Room):
        self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        if self.budget >= total_price:
            self.budget -= total_price
            self.reward_points += int(total_price * 0.1)
            return True
        return False

    def show_booking_summary(self) -> str:
        rooms_str = ", ".join([str(r.room_number) for r in self.booked_rooms])
        return f"მომხმარებელი: {self.name} | ბიუჯეტი: {self.budget}GEL | დაჯავშნილი ოთახები: [{rooms_str}] | ქულები: {self.reward_points}"


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.bookings_log = []

    def add_room_to_hotel(self, room: Room):
        self.rooms.append(room)

    def show_available_rooms(self, room_type: str = None) -> list:
        available = []
        for room in self.rooms:
            if room.is_available:
                if room_type is None or room.room_type.lower() == room_type.lower():
                    available.append(room)
        return available

    def calculate_total_booking(self, room_number: int, nights: int) -> float:
        for room in self.rooms:
            if room.room_number == room_number:
                return room.calculate_price(nights)
        return 0.0

    def log_booking(self, customer: Customer, room: Room, total_price: float):
        log_message = f"დაჯავშნა: {customer.name}-მა დაჯავშნა ოთახი {room.room_number} ({room.room_type}), ფასი: {total_price}GEL"
        self.bookings_log.append(log_message)
        logging.info(log_message)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int) -> bool:
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                total_price = room.calculate_price(nights)
                if customer.pay_for_booking(total_price):
                    room.book_room()
                    customer.add_room(room)
                    self.log_booking(customer, room, total_price)
                    return True
        return False

    def cancel_booking(self, customer: Customer, room_number: int) -> bool:
        for room in customer.booked_rooms:
            if room.room_number == room_number:
                room.release_room()
                customer.remove_room(room)
                log_message = f"გაუქმება: {customer.name}-მა გააუქმა ოთახი {room_number}"
                self.bookings_log.append(log_message)
                logging.info(log_message)
                return True
        return False



app = Flask(__name__)


hotel = Hotel("Grand Palace")
hotel.add_room_to_hotel(Room(101, "Single", 100.0, 1))
hotel.add_room_to_hotel(Room(102, "Double", 180.0, 2))
hotel.add_room_to_hotel(Room(103, "Suite", 300.0, 4))

customer = Customer("გიორგი", 1000.0)


@app.route("/", methods=["GET", "POST"])
def index():
    status_message = "სისტემის სტატუსი: მზად არის დასაჯავშნად."

    if request.method == "POST":
        room_type = request.form.get("room_type")
        try:
            days = int(request.form.get("days", 1))
            budget = float(request.form.get("budget", 0))
            customer.budget = budget
        except ValueError:
            status_message = "შეცდომა: შეიყვანეთ სწორი რიცხვები!"
            return render_template("index.html", hotel=hotel, customer=customer, status_message=status_message)

        available_rooms = hotel.show_available_rooms(room_type)

        if not available_rooms:
            status_message = f"სამწუხაროდ, {room_type} ტიპის თავისუფალი ოთახი აღარ არის!"
        else:
            selected_room = available_rooms[0]
            success = hotel.book_room_for_customer(customer, selected_room.room_number, days)
            if success:
                status_message = f"წარმატება! დაჯავშნეთ ოთახი {selected_room.room_number}. ფასი: {selected_room.calculate_price(days)} GEL."
            else:
                status_message = f"შეცდომა: არასაკმარისი ბიუჯეტი! ოთახის ღირებულებაა {selected_room.calculate_price(days)} GEL, თქვენ გაქვთ მხოლოდ {customer.budget} GEL."

    return render_template("index.html", hotel=hotel, customer=customer, status_message=status_message)


if __name__ == "__main__":
    app.run(debug=True)