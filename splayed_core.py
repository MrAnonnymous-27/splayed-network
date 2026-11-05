import hashlib
import json
import time

class SplayedBlock:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0, difficulty=4):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.difficulty = difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        target = "0" * self.difficulty
        print(f"⛏️  Mining Splayed Block #{self.index} with difficulty {self.difficulty}...")
        start_time = time.time()
        
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        elapsed_time = round(time.time() - start_time, 2)
        print(f"✨ Block #{self.index} Mined Successfully in {elapsed_time}s!")
        print(f"🔗 Hash: {self.hash}")
        print(f"🎲 Nonce: {self.nonce}\n")

class SplayedChain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.max_supply = 21000000  # 21 Million Max Supply ($SPL)
        self.block_reward = 50       # Initial reward per mined block
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        print("🚀 Initializing SPLAYED ($SPL) Genesis Block...")
        genesis_block = SplayedBlock(0, "0" * 64, time.time(), ["Genesis Block: SPLAYED Network Live"], difficulty=self.difficulty)
        genesis_block.mine_block()
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        # Reward Transaction for the Miner
        reward_tx = {"from": "NETWORK", "to": miner_address, "amount": self.block_reward}
        self.pending_transactions.append(reward_tx)

        new_block = SplayedBlock(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            timestamp=time.time(),
            transactions=self.pending_transactions,
            difficulty=self.difficulty
        )
        
        new_block.mine_block()
        self.chain.append(new_block)
        self.pending_transactions = []

# Quick Local Node Test Engine
if __name__ == "__main__":
    splay_node = SplayedChain()

    # Simulate First Miner Mining Block 1
    miner_wallet = "spl1q9xh287zxa8z0d7p4k0w3e8q5a2x9u7y1z3spl"
    print(f"💰 Miner Wallet Initialized: {miner_wallet}\n")

    splay_node.mine_pending_transactions(miner_wallet)
    splay_node.mine_pending_transactions(miner_wallet)
