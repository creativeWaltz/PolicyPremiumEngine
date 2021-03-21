import unittest
import vessel


class VesselCreationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.t_vessel = vessel.Vessel("HMS Ship", "91234567", 10_000_000)

    def test_asset_creation(self):
        """test name of object is correct"""
        self.assertEqual(self.t_vessel.name, "HMS Ship")
        self.assertEqual(self.t_vessel.value, 10_000_000)
        self.assertEqual(self.t_vessel.imo, "91234567")
        self.assertEqual(self.t_vessel.owned, True)
        self.assertEqual(self.t_vessel.version, 1)

    def test_asset_owned(self):
        """test the asset ownership is True"""
        pass


    def test_version_number_1_at_creation(self):
        """check version number is one when created"""
        pass






if __name__ == '__main__':
    unittest.main()
