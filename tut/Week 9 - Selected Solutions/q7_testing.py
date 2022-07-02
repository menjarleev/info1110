from q5_q6_pet import Pet

import unittest

class PetTest(unittest.TestCase):
	
	def test_has_nickname(self):
		p = Pet('Rover', 5, 'Dog', True)
		p.add_nickname('Doggo')
		self.assertFalse(p.has_nickname('Igloo'))
		self.assertTrue(p.has_nickname('Doggo'))
		
	def test_add_nickname(self):
		p = Pet('Rover', 5, 'Dog', True)
		p.add_nickname('Doggo')
		self.assertEqual('Doggo', p.nicknames[0])
		

