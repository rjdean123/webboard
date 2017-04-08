class RequestHandler:

	def __init__(self):
		self.count = 0
		self.drawn_coordinates = {}

	def handle_get(self):
		self.count += 1
		return "visitor: " + str(self.count)


	def handle_post(self, raw_coorindates_str):
		return raw_coorindates_str