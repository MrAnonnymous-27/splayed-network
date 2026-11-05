# ⚡ SPLAYED ($SPL) — Next-Gen Decentralized Layer-1 Currency

<p align="center">
  <img src="logo.svg" alt="SPLAYED Logo" width="160" height="160">
</p>

<p align="center">
  <b>Inspired by Bitcoin. Engineered for absolute financial freedom, supreme scalability, and strict scarcity.</b>
</p>

---

## 🌐 Overview
**SPLAYED ($SPL)** is an independent, decentralized Layer-1 blockchain network (The Splaychain) governed by a strict fixed supply model and Proof-of-Work (PoW) consensus. Designed to eliminate intermediaries and offer absolute sovereignty to its global user base.

- **Ticker:** $SPL
- **Max Total Supply:** 21,000,000 (Strictly Capped)
- **Consensus:** Proof-of-Work (SHA-256 Engine)
- **Official Website:** [https://mranonnymous-27.github.io/splayed-network/](https://mranonnymous-27.github.io/splayed-network/)

---

## 📂 Repository Architecture

- `index.html` — Official decentralized landing page & Testnet Faucet widget.
- `logo.svg` — Official Vector Brand Identity ("S-Curve Neon Glow").
- `splayed_core.py` — Core blockchain ledger and PoW mining algorithm.
- `miner.py` — Interactive CLI Miner client.
- `wallet.py` — Cryptographic key & secure wallet address generator.
- `node_server.py` — Flask-powered P2P node and transaction broadcasting server.
- `WHITEPAPER.md` — Comprehensive technical architecture specification.

---

## 💻 Running a Splaychain Node & Miner

To participate in the Splayed network, clone this repository and run the core modules locally:

### 1. Generate Your Secure Wallet
Create your cryptographic public address (`spl1q...`) and private key:
```bash
python wallet.py
