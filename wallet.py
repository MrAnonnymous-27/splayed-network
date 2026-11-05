import hashlib
import os
import secrets

class SplayedWallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key(self.private_key)
        self.address = self.generate_address(self.public_key)

    def generate_private_key(self):
        # Generate 256-bit cryptographically strong random secret
        return secrets.token_hex(32)

    def generate_public_key(self, private_key):
        # Hash private key using SHA-256 to produce public key component
        return hashlib.sha256(private_key.encode('utf-8')).hexdigest()

    def generate_address(self, public_key):
        # Generate standard Splaychain address prefix (spl1q...)
        ripemd160_hash = hashlib.new('ripemd160', public_key.encode('utf-8')).hexdigest()
        return f"spl1q{ripemd160_hash[:34]}"

def create_wallet():
    print("=" * 65)
    print(" 🔑   SPLAYED ($SPL) NETWORK — CRYPTOGRAPHIC WALLET GENERATOR   🔑")
    print("=" * 65)
    
    wallet = SplayedWallet()
    
    print("\n✅ New Splaychain Account Generated Successfully!\n")
    print(f"📌 Public Wallet Address : {wallet.address}")
    print(f"🛡️  Public Key           : {wallet.public_key}")
    print(f"🔐 Private Key (SECRET)  : {wallet.private_key}")
    print("\n⚠️  IMPORTANT: Never share your Private Key with anyone! Keep it safe.")
    print("=" * 65)

if __name__ == "__main__":
    create_wallet()
