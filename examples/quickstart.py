"""IQ Option OTC candles in a few lines. Runs on the free tier.

    pip install otcharts
    export OTCHARTS_API_KEY=otc_live_...      # free key: https://otcharts.com/account
    python examples/quickstart.py
"""
from otcharts import Client

otc = Client()

print("Instruments your key can read on IQ Option:")
for s in otc.symbols("iq"):
    print("  ", s.symbol, "-", s.name)

bars = otc.candles("iq", "EURUSD-OTC", tf=60, limit=10)
print("\nLast {} one-minute bars of EURUSD-OTC (time, open, high, low, close):".format(len(bars)))
for b in bars:
    print("  ", b.time, b.open, b.high, b.low, b.close)

u = otc.usage()
print("\nRequests left:", u.remaining, "of", u.quota_per)
