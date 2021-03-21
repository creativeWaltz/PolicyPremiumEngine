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

    def test_asset_name_change(self):
        self.t_vessel.update_name("HMS Dog","21/12/2020")
        self.assertEqual(self.t_vessel.name, "HMS Dog")
        self.assertEqual(self.t_vessel.version, 2)
        self.assertNotEqual(self.t_vessel.name_date,"21/12/2020")












if __name__ == '__main__':
    unittest.main()
