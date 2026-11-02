# Binance Wallet Agent — Starter Project

A small, security-first starter repository for exploring crypto market data and planning trades.

## Current status

This is a **starter template**, not a live trading bot. It does not connect to Binance, request API credentials, place orders, or move funds. The initial version provides:
- a project overview and security checklist
- an example `.env.example` file with no real secrets
- a basic risk-limit configuration template
- a placeholder Python entry point for future development

Do not claim features are operational until they have actually been implemented and tested.

## Quick start

1. Install Python 3.10+.
2. Create a virtual environment (optional but recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` only if you later add a supported integration. Never commit `.env`.
5. Run the starter:

   ```bash
   python main.py
   ```

## Safety principles

- Never commit API keys, API secrets, wallet private keys, seed phrases, recovery codes, or `.env` files.
- Start with public market data and paper trading before considering live orders.
- Keep withdrawal permissions disabled for any trading API key.
- Use least-privilege permissions and IP restrictions where supported.
- Set explicit per-order and daily loss limits before enabling any real trading.
- Do not use leverage or futures in the initial implementation.
- Verify the official API documentation and the identity of any third-party service before connecting accounts.

## Repository structure

```text
binance-wallet-agent/
├── README.md
├── main.py
├── config.example.json
├── .env.example
├── .gitignore
├── requirements.txt
└── LICENSE
```

## Roadmap

- [ ] Public market-data research
- [ ] Paper-trading simulator
- [ ] Tests for risk limits
- [ ] Optional exchange integration after reviewing official documentation
- [ ] Explicit confirmation and safeguards before any live order

## Disclaimer

This repository is educational starter code, not financial advice. Cryptocurrency trading involves risk. No trading results or API access are guaranteed.
