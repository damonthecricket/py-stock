
import unittest

from . import test_candle
from . import test_stock


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_candle)  )
suite.addTests( loader.loadTestsFromModule(test_stock)   )

runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)