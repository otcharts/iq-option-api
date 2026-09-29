"""Live IQ Option prices on one connection. Runs on the free tier (one pair).

    python examples/stream_one_pair.py
"""
from otcharts import Client

otc = Client()
seen = 0
for tick in otc.stream("iq", "EURUSD-OTC"):
    print(tick.symbol, tick.price)
    seen += 1
    if seen >= 20:          # stop after 20 prices; remove this to run forever
        break
