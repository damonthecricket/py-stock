
import unittest

try:
	from .. import stock
except:
	import stock



# StockTest

class StockTest(unittest.TestCase):

	def testLoad(self):
		for m in self._load_mock():
			s = stock.load(m)

			self.assertTrue(len(s.candles()) > 0)


	def testInstance(self):
		name = "a"
		candles = self._instance_mock()
		s = stock.create(name, candles)

		self.assertEqual(s.name(), name)
		self.assertEqual(s.candles(), candles)


	def _load_mock(self):
		return [
		'a.us', 'aa.us', 'aaap.us', 'aaba.us', 'aac.us'
		]


	def _instance_mock(self):
		return [
			( "1999-11-18", 30.713, 33.754, 27.002, 29.702, 66277506 ),
			( "1999-11-19", 28.986, 29.027, 26.872, 27.257, 16142920 ),
			( "1999-11-22", 27.886, 29.702, 27.044, 29.702, 6970266  ),
			( "1999-11-23", 28.688, 29.446, 27.002, 27.002, 6332082  )
			]
		