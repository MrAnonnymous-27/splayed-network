import sys
import time
from splayed_core import SplayedChain

def start_miner():
    print("=" * 60)
    print(" ⛏️   SPLAYED ($SPL) NETWORK — OFFICIAL CLI MINER v1.0   ⛏️")
    print("=" * 60)
    
    miner_wallet = input("\n👉 Enter your Splay Wallet Address (e.g. spl1q9x...): ").strip()
    if not miner_wallet:
        miner_wallet = "spl1q_default_community_miner_node"
        print(f"⚠️  No wallet provided. Using fallback address: {miner_wallet}")
    
    print(f"\n✅ Connected to SPLAYED Layer-1 Node.")
    print(f"🔑 Target Reward Address: {miner_wallet}")
    print("⚡ Starting Proof-of-Work (PoW) Engine...\n")
    
    node = SplayedChain()
    blocks_mined = 0

    try:
        while True:
            blocks_mined += 1
            print("-" * 50)
            print(f"🔄 Preparing Block #{len(node.chain)} for Mining...")
            
            start_t = time.time()
            node.mine_pending_transactions(miner_wallet)
            elapsed = time.time() - start_t
            
            # Simple Hashrate Estimation
            estimated_hashes = node.get_latest_block().nonce
            hashrate = round(estimated_hashes / max(elapsed, 0.001), 2)
            
            print(f"💰 Reward Claimed: +50 $SPL")
            print(f"📊 Node Hashrate: {hashrate} H/s | Total Blocks Mined by You: {blocks_mined}")
            print("-" * 50 + "\n")
            
            time.sleep(1) # Interval before picking up the next transaction block
            
    except KeyboardInterrupt:
        print("\n\n⛔ Mining Session Stopped by User.")
        print(f"🎉 Session Summary: Mined {blocks_mined} blocks into {miner_wallet}.")
        sys.exit(0)

if __name__ == "__main__":
    start_miner()
