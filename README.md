# PyStock
[![codebeat badge](https://codebeat.co/badges/37586e5b-3222-4c71-89e3-c280ee363d65)](https://codebeat.co/projects/github-com-damonthecricket-pystock-master) [![Build Status](https://travis-ci.org/damonthecricket/pystock.svg?branch=master)](https://travis-ci.org/damonthecricket/pystock)

Python language stock library.


1. [Features](#features)
2. [Installation](#installation)



### Features
1. Candle. Tiny module to represent stock candle structure.
   ```python
   import pystock.candle as candle
   
   # Creates candle with 1999-11-18 date, 30.713 open, 33.754 high, 27.002 low,
   # 29.702 close, 66277506 volume properties.
   c = candle.create("1999-11-18", 30.713, 33.754, 27.002, 29.702, 66277506)
   ```
2. Stock Tiny module to represent stock structure.
   ```python
   import pystock.stock as stock
   
   # Loads stock market file with "a.us" name.
   s = stock.load("a.us")
   
   # Returns candles.
   c = s.candles()
   
   # Returns name ("a.us").
   n = s.name()
   ```
   
   
   
 ### Installation
  ```
  $ git clone https://github.com/damonthecricket/pystock.git
  ```
