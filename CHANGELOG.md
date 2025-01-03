# Changelog

## 1.4.2

Features:

- changed the alignment of the text in the list of currencies
- change collapsed text color in Expansion Tile
- added header from Coins List


## 1.4.1

Fix:

- adjust the alignment and style of the text that I broke in the Flet update
- adjustment of some notes in the changelog


## 1.4.0

Fix:

- code adjustment to meet the standards of the new version of Flet 0.25.2


## 1.3.2

Features:

- added list of coins in the Poloniex and Binance tabs (still needs some tweaking)

Fix:

- improved position of the home page button


## 1.3.1

Fix:

- fixing overview that was committed without checking correct file


## 1.3.0

Features:

- overview restructing


## 1.2.0

Features:

- remove global scrolling and added only where necessary
- added btc value variation in coin info
- added Tabs to view the currencies of each exchange separately (still under construction)

Fix:

- fix the version name of the last commit in the CHANGELOG.md file


## 1.1.3

Features:

- standardized names of Poloniex price pairs
- added calculation for USDT/coin pair (e.g. USDT/BRL)

Fix:

- fixed float conversion in Utils format_big_number


## 1.1.2

Features:

- limited display size for large numbers (e.g. 12,345.67898765 -> 12,345.678)

Fix:

- fix Binace BTC value show in overview
- fix btc_value calculation for USDT
- fix "to string" of Coin


## 1.1.1

Features:

- added information about the currency on the ExpansionTile
- added more attributes to the “Coin” class
- added comma for large numbers (e.g. 1000.00 -> 1,000.00)
- added changelog

Fix:

- removed repeated code in “balance_update” to avoid future errors
- fix values for USDT
