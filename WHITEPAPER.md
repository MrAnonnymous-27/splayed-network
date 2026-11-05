# SPLAYED: A Peer-to-Peer Electronic Decentralized Currency System

**Author:** Splayed Core Development Group  
**Date:** June 2026  
**Ticker:** $SPL  
**Official Network:** Splaychain (Layer-1)  

---

## Abstract
SPLAYED ($SPL) is a decentralized, peer-to-peer digital currency designed to provide absolute financial sovereignty, immutable ledger security, and strict mathematical scarcity. Inspired by the architectural brilliance of Bitcoin, Splayed utilizes a Proof-of-Work (PoW) consensus mechanism coupled with an independent Layer-1 blockchain engine (The Splaychain). By removing central authorities, intermediaries, and inflationary monetary policy, Splayed establishes a trustless, global financial ecosystem with a hard-coded maximum supply of 21,000,000 tokens.

---

## 1. Introduction
Traditional fiat monetary systems suffer from systemic inflation, state censorship, and counterparty risks. Decentralized cryptocurrencies introduced a paradigm shift by utilizing cryptographic proofs instead of trust. However, many modern networks sacrifice decentralization for speed or compromise security for utility. 

Splaychain returns to first principles: a transparent, censorship-resistant, cryptographically secured append-only ledger where global nodes cooperate to validate transactions and secure network integrity through computational effort (Mining).

---

## 2. Tokenomics & Scarcity Model
To prevent devaluation through excessive money printing, Splayed implements an absolute, unalterable supply cap:

- **Maximum Total Supply:** 21,000,000 $SPL
- **Consensus Algorithm:** Proof-of-Work (SHA-256)
- **Initial Block Reward:** 50 $SPL per successfully mined block
- **Emission Schedule:** Programmatic block-reward reduction mirroring strict scarcity curves.

No entity, foundation, or developer can mint tokens outside the algorithmic rules hardcoded into the Splaychain protocol.

---

## 3. Cryptographic Wallets & Public Addresses
Every user on the Splayed network interacts via a mathematically secure cryptographic keypair:
1. **Private Key:** A 256-bit cryptographically secure secret used to sign transactions and authorize transfers.
2. **Public Key:** Derived via secure hashing algorithms from the private key.
3. **Splay Address (`spl1q...`):** The user-facing destination format, encoded for security and human readability, ensuring complete pseudonymity and user control.

---

## 4. Proof-of-Work (PoW) Consensus & Mining
Network security is maintained through the Splaychain PoW engine (`splayed_core.py` & `miner.py`). 
- Miners compete to solve cryptographic puzzles by adjusting a dynamic `nonce` until the resulting SHA-256 block hash matches the current network `difficulty` target (leading zeros).
- Once a block is solved, it is broadcasted across the peer-to-peer node architecture (`node_server.py`) and appended to the immutable ledger.
- This creates an energy-backed security model where altering past history requires a prohibitive share of global computational power.

---

## 5. Conclusion
SPLAYED ($SPL) bridges the visionary ideals of early decentralized currencies with modern modular architecture. By building an open-source, community-driven Layer-1 network from the ground up, Splayed empowers developers, miners, and holders worldwide to participate in the future of absolute digital scarcity.

---
*© 2026 Splayed Foundation. Open-source under the MIT License.*
