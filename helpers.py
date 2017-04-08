class RequestHandler:

	def __init__(self):
		self.drawn_coordinates = set()

	def handle_get(self):
		response = "no coordinates drawn yet"
		if len(self.drawn_coordinates) > 0:
			response = "coordinates drawn so far:"
			for dc in self.drawn_coordinates:
				response = response + " " + dc
		return response


	def handle_post(self, raw_coorindates_str):
		self.process_post_data(raw_coorindates_str)
		return "success"


	def process_post_data(self, raw_coorindates_str):
		raw_coordinates = raw_coorindates_str.split(';')
		for rc in raw_coordinates:
			if len(rc) <= 3:
				continue
			rc = rc[1:-1]
			self.drawn_coordinates.add(rc)