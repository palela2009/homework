import unittest
from hotel_system import Room, Customer, Hotel

class TestHotelSystem(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Grand Palace")
        self.room1 = Room(101, "Single", 100.0, 1)
        self.room2 = Room(102, "Double", 180.0, 2)
        self.hotel.add_room_to_hotel(self.room1)
        self.hotel.add_room_to_hotel(self.room2)
        self.customer = Customer("გიორგი", 500.0)

    def test_pay_for_booking_success(self):
        initial_budget = self.customer.budget
        result = self.customer.pay_for_booking(200.0)
        self.assertTrue(result)
        self.assertEqual(self.customer.budget, initial_budget - 200.0)
        self.assertEqual(self.customer.reward_points, 20)

    def test_pay_for_booking_insufficient_budget(self):
        result = self.customer.pay_for_booking(600.0)
        self.assertFalse(result)
        self.assertEqual(self.customer.budget, 500.0)

    def test_book_room_for_customer_success(self):
        result = self.hotel.book_room_for_customer(self.customer, 101, 2)
        self.assertTrue(result)
        self.assertFalse(self.room1.is_available)
        self.assertIn(self.room1, self.customer.booked_rooms)
        self.assertEqual(self.customer.budget, 300.0)

    def test_book_room_already_occupied(self):
        self.hotel.book_room_for_customer(self.customer, 101, 2)
        another_customer = Customer("ნიკა", 400.0)
        result = self.hotel.book_room_for_customer(another_customer, 101, 1)
        self.assertFalse(result)

    def test_cancel_booking(self):
        self.hotel.book_room_for_customer(self.customer, 102, 1)
        result = self.hotel.cancel_booking(self.customer, 102)
        self.assertTrue(result)
        self.assertTrue(self.room2.is_available)
        self.assertNotIn(self.room2, self.customer.booked_rooms)

if __name__ == "__main__":
    unittest.main()