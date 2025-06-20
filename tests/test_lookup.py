import unittest
from exchange_metadata.get_exchange_metadata import get_exchange_metadata

class TestExchangeMetadata(unittest.TestCase):
    def test_lookup_myx(self):
        meta = get_exchange_metadata("myx")
        self.assertEqual(meta["timezone"], "Asia/Kuala_Lumpur")

    def test_lookup_xtks(self):
        meta = get_exchange_metadata("XTKS")
        self.assertEqual(meta["currency"], "JPY")

    def test_invalid_code(self):
        with self.assertRaises(ValueError):
            get_exchange_metadata("UNKNOWN")

# This is not required for discovery, but useful for direct execution
if __name__ == '__main__':
    unittest.main()
