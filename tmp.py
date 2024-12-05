with open("tests/test_wallet.py", "w") as f:
    f.write("""# Test cases for Wallet

import unittest
from src.wallet import Wallet

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet("test_wallet", 100)

    def test_initial_balance(self):
        self.assertEqual(self.wallet.get_balance(), 100)

    def test_add_transaction(self):
        self.wallet.add_transaction({"amount": 50, "type": "deposit"})
        self.assertEqual(len(self.wallet.transactions), 1)

if __name__ == "__main__":
    unittest.main()
    """)
print("Populated tests/test_wallet.py")
