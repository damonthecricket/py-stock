
import unittest

try:
	from .. import candle
except:
	import candle



# CandleTest

class CandleTest(unittest.TestCase):

	def testInstance(self):
		for m in self._instance_mock():
			date = m[0]
			open_ = m[1]
			high = m[2]
			low = m[3]
			close = m[4] 
			volume = m[5]

			c = candle.create(date, open_, high, low, close, volume)

			self.assertEqual(c.date(), date)
			self.assertEqual(c.open(), open_)
			self.assertEqual(c.high(), high)
			self.assertEqual(c.low(), low)
			self.assertEqual(c.close(), close)
			self.assertEqual(c.volume(), volume)


	def testEquality(self):
		for m in self._instance_mock():
			date = m[0]
			open_ = m[1]
			high = m[2]
			low = m[3]
			close = m[4] 
			volume = m[5]

			created = candle.create(date, open_, high, low, close, volume)
			c = candle.Candle(date, open_, high, low, close, volume)

			self.assertEqual(created, c)


	def testPorperties(self):
		for m in self._properties_mock():
			date = m[0]
			open_ = m[1]
			high = m[2]
			low = m[3]
			close = m[4]
			volume = m[5]
			is_bullish = m[6]
			is_bearish = m[7]
			is_unit = m[8]
			current = m[9]

			c = candle.create(date, open_, high, low, close, volume)

			self.assertEqual(c.date(), date)
			self.assertEqual(c.open(), open_)
			self.assertEqual(c.high(), high)
			self.assertEqual(c.low(), low)
			self.assertEqual(c.close(), close)
			self.assertEqual(c.volume(), volume)
			self.assertEqual(c.is_bullish(), is_bullish)
			self.assertEqual(c.is_bearish(), is_bearish)
			self.assertEqual(c.current(), current)


	def _instance_mock(self):
		return [
			( "1999-11-18", 30.713, 33.754, 27.002, 29.702, 66277506 ),
			( "1999-11-19", 28.986, 29.027, 26.872, 27.257, 16142920 ),
			( "1999-11-22", 27.886, 29.702, 27.044, 29.702, 6970266  ),
			( "1999-11-23", 28.688, 29.446, 27.002, 27.002, 6332082  )
		]


	def _properties_mock(self):
		return [
			# date, 		open, 	high, 	low, 	close, 	volume
			( "1999-11-18", 30.713, 33.754, 27.002, 29.702, 66277506, True, False, False, 33.754 ),
			( "1999-11-19", 28.986, 29.027, 26.872, 27.257, 16142920, True, False, False, 29.027 ),
			( "1999-11-22", 27.886, 29.702, 27.044, 29.702, 6970266,  True, False, False, 29.702 ),
			( "1999-11-23", 28.688, 29.446, 27.002, 27.002, 6332082,  True, False, False, 29.446 )
		]
