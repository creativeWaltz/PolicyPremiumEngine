import unittest
import vessel


class VesselCreationAndMethodTests(unittest.TestCase):
    def setUp(self) -> None:
        self.t_vessel = vessel.Vessel("HMS Ship", "91234567", 10_000_000)

    def test_asset_creation(self):
        """test name of object is correct"""
        self.assertEqual(self.t_vessel.name, "HMS Ship")
        self.assertEqual(self.t_vessel.value, 10_000_000)
        self.assertEqual(self.t_vessel.imo, "91234567")
        self.assertEqual(self.t_vessel.owned, True)
        self.assertEqual(self.t_vessel.version, 1)

    def test_asset_gets_sold(self):
        self.t_vessel.sell()
        self.assertEqual(self.t_vessel.owned, False)
        self.assertEqual(self.t_vessel.version, 1)

    def test_asset_valuation_change_not_allowed_before_current_date(self):
        self.t_vessel.update_value(20_000_000, "20/03/2021")
        self.assertEqual(self.t_vessel.version, 1)
        self.assertEqual(self.t_vessel.value,10_000_000)

    def test_asset_valuation_same_date_not_allowed(self):
        self.t_vessel.update_value(30_000_000, "21/03/2021")
        self.assertEqual(self.t_vessel.version, 1)
        self.assertEqual(self.t_vessel.value, 10_000_000)


    def test_asset_valuation_same_amount_not_allowed(self):
        self.t_vessel.update_value(10_000_000, "21/03/2021")
        self.assertEqual(self.t_vessel.version, 1)
        self.assertEqual(self.t_vessel.value, 10_000_000)











if __name__ == '__main__':
    unittest.main()
