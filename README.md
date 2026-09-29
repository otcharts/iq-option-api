# IQ Option API — free OTC market data, no SSID

IQ Option has no official API: no developer portal and no API keys. This repo shows the
simplest way to read IQ Option's OTC prices from code **without handing over your
session**, using the [OTCharts market-data API](https://otcharts.com/iq-option-api).

- **Candles and live prices** for IQ Option's instruments as JSON, plus payout
  percentages on the paid plans.
- **A free API key, no card.** Sign up, confirm your email, create a key.
- **No SSID and no IQ Option login.** Nothing touches your broker account: no session
  to copy, nothing to refresh, nothing to get flagged.
- **Read-only.** It cannot place trades. If you need to automate orders, this is not
  the tool, and you should stop here rather than pay for it.

> **Not affiliated with IQ Option.** An "official IQ Option API key" does not exist, and
> anyone selling one is not telling the truth. This is an OTCharts key, for market data.

## Quick start

1. Make a free account at [otcharts.com](https://otcharts.com) and confirm the email.
2. Create a key on your [account page](https://otcharts.com/account). It is shown once.
3. Run an example:

```bash
pip install otcharts                  # no dependencies
export OTCHARTS_API_KEY=otc_live_...
python examples/quickstart.py
```

```python
from otcharts import Client

otc = Client()                               # reads OTCHARTS_API_KEY

for s in otc.symbols("iq"):              # what your key can read, exact ids
    print(s.symbol, s.name)

bars = otc.candles("iq", "EURUSD-OTC", tf=60, limit=100)
print(bars[-1].time, bars[-1].close)

for tick in otc.stream("iq", "EURUSD-OTC"):   # live prices on one connection
    print(tick.symbol, tick.price)
```

Or plain HTTP, from any language:

```bash
curl -H "Authorization: Bearer $OTCHARTS_API_KEY" \
  "https://otcharts.com/v1/candles?venue=iq&symbol=EURUSD-OTC&tf=60&limit=5"
```

## SSID libraries vs this API

| | Community libraries | This API |
|---|---|---|
| What you give it | your IQ Option session (SSID) | an API key of its own |
| Your broker account | its session runs inside someone's code | never touched |
| When IQ Option changes its site | breaks until someone patches it | the feed is kept running for you |
| Places trades | yes | **no**, market data only |
| Price | free | free tier, published paid plans |

If you need to place orders, the community libraries are the only route there is. If
you only need the prices, this is far less to go wrong.

## Symbols

IQ Option ids look like `EURUSD-OTC` (hyphen, upper case). Do not keep your own list: `symbols("iq")` returns the
live catalogue, and an instrument the broker stops quoting drops out of it.

On the free tier your key reads these five: `EURUSD-OTC`, `GBPUSD-OTC`, `USDJPY-OTC`, `ETHUSD-OTC`, `AUDUSD-OTC`.

## Free tier and plans

| | Free | Lite | Build | Run | Desk |
|---|---|---|---|---|---|
| Price | $0 | $15/mo | $49/mo | $149/mo | $249/mo |
| Books | 1 | 1 | 1 | 3 | all 5 |
| Instruments | 5 | the whole book | the whole book | the whole book | the whole book |
| Requests | 1,500 a week | 7,000 a day | 25,000 a day | 100,000 a day | 500,000 a day |
| Live streams | 1 | 1 | 1 | 3 | 10 |
| Older history (`before=`) | no | no | yes | yes | yes |
| Payout percentages | no | yes | yes | yes | yes |

On this book each stream carries one instrument. Figures as of 30 September 2026. The live table is at
[otcharts.com/pricing](https://otcharts.com/pricing#api).

## Other books, same key

[Pocket Option](https://github.com/otcharts/pocket-option-api) ·
[Quotex](https://github.com/otcharts/quotex-api) ·
[IQ Option](https://github.com/otcharts/iq-option-api) · BinoDex · the real forex market.
Python client: [otcharts/otcharts-python](https://github.com/otcharts/otcharts-python).
Full reference: [otcharts.com/api](https://otcharts.com/api).

## FAQ

**Is this an official IQ Option API?** No. IQ Option does not publish one. OTCharts is
independent and holds its own connection to the price feed.

**Do I need a IQ Option account?** No.

**Can it place trades?** No. It reads prices and nothing else.

**Are OTC prices the real market?** No. OTC prices are the broker's own quotes, not
the interbank market. The API reports what the broker quotes, bar for bar.

## Licence

The examples here are MIT-licensed. The API itself is a service with its own
[terms](https://otcharts.com/terms).
