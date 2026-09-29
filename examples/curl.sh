#!/usr/bin/env bash
# IQ Option OTC data over plain HTTP. Needs OTCHARTS_API_KEY in the environment.
set -euo pipefail
H="Authorization: Bearer ${OTCHARTS_API_KEY:?set OTCHARTS_API_KEY first}"

# The instruments your key can read, with their exact ids
curl -s -H "$H" "https://otcharts.com/v1/symbols?venue=iq"
echo
# The last five one-minute candles of EURUSD-OTC
curl -s -H "$H" "https://otcharts.com/v1/candles?venue=iq&symbol=EURUSD-OTC&tf=60&limit=5"
echo
