import unittest
import santorini


class MyTests(unittest.TestCase):

	def test_validatePosition_TopLeftCornerValidPos(self):
		player = santorini.Player()
		validation = player.validatePosition([0, 0])
		self.assertTrue(validation)

	def test_validatePosition_BottomRightCornerValidPos(self):
		player = santorini.Player()
		validation = player.validatePosition([4, 4])
		self.assertTrue(validation)

	def test_validatePosition_LeftEdgeInvalidPos(self):
		player = santorini.Player()
		validation = player.validatePosition([2, -1])
		self.assertFalse(validation)

	def test_validatePosition_RightEdgeInvalidPos(self):
		player = santorini.Player()
		validation = player.validatePosition([2, 5])
		self.assertFalse(validation)

	def test_validatePosition_TopEdgeInvalidPos(self):
		player = santorini.Player()
		validation = player.validatePosition([-1, 0])
		self.assertFalse(validation)

	def test_validatePosition_BottomEdgeInvalidPos(self):
		player = santorini.Player()
		validation = player.validatePosition([5, 0])
		self.assertFalse(validation)

	def test_getNeighboringPositions_TopLeftCorner(self):
		player = santorini.Player()
		worker = santorini.Worker()
		worker.row = 0
		worker.col = 0
		neighboringPositions = player.getNeighboringPositions(worker)
		self.assertEqual([[0, 1], [1, 0], [1, 1]], neighboringPositions)

	def test_getNeighboringPositions_BottomRightCorner(self):
		player = santorini.Player()
		worker = santorini.Worker()
		worker.row = 4
		worker.col = 4
		neighboringPositions = player.getNeighboringPositions(worker)
		self.assertEqual([[3, 4], [3, 3], [4, 3]], neighboringPositions)

	def test_getNeighboringPositions_Center(self):
		player = santorini.Player()
		worker = santorini.Worker()
		worker.row = 2
		worker.col = 2
		neighboringPositions = player.getNeighboringPositions(worker)
		self.assertEqual([[1, 2], [1, 3], [1, 1], [2, 3], [2, 1], [3, 2], [3, 3], [3, 1]], neighboringPositions)

if __name__ == '__main__':
	unittest.main()
