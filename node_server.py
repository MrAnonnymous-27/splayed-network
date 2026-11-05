import json
from flask import Flask, jsonify, request
from splayed_core import SplayedChain

app = Flask(__name__)

# Initialize local node copy of Splaychain
splay_node = SplayedChain()

@app.route('/chain', methods=['GET'])
def get_chain():
    """ Returns the complete Splayed Blockchain ledger """
    chain_data = []
    for block in splay_node.chain:
        chain_data.append(block.__dict__)
    
    return jsonify({
        "length": len(chain_data),
        "chain": chain_data,
        "max_supply": splay_node.max_supply,
        "network": "SPLAYED Mainnet Candidate v1.0"
    }), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """ Broadcast a new $SPL transfer transaction to the pending pool """
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    
    if not all(k in values for k in required):
        return jsonify({'error': 'Missing values'}), 400

    tx = {
        'from': values['sender'],
        'to': values['recipient'],
        'amount': values['amount']
    }
    splay_node.pending_transactions.append(tx)
    return jsonify({'message': f'Transaction will be added to Block #{len(splay_node.chain)}'}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    """ Node mining endpoint for local or remote miners """
    miner_address = request.args.get('miner', 'spl1q_community_node_miner')
    splay_node.mine_pending_transactions(miner_address)
    latest_block = splay_node.get_latest_block()
    
    return jsonify({
        'message': 'New Splay Block Successfully Mined!',
        'index': latest_block.index,
        'hash': latest_block.hash,
        'previous_hash': latest_block.previous_hash,
        'nonce': latest_block.nonce,
        'reward': splay_node.block_reward
    }), 200

if __name__ == '__main__':
    print("=" * 65)
    print(" 🌐   SPLAYED ($SPL) NETWORK — P2P NODE SERVER RUNNING   🌐")
    print("=" * 65)
    print("⚡ Listening on port 5000 for incoming peers, miners, and transactions...")
    app.run(host='0.0.0.0', port=5000)
