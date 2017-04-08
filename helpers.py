class RequestHandler:

	def __init__(self):
		self.drawn_coordinates = set()

	def handle_get(self):
		return self.prepare_get_response()


	def handle_post(self, raw_coorindates_str, phone_width, phone_height):
		self.process_post_data(raw_coorindates_str, phone_width, phone_height)
		return "success"


	def handle_clear(self):
		self.drawn_coordinates.clear()
		return "success"


	def prepare_get_response(self):
		if len(self.drawn_coordinates) == 0:
			return ""
		response = ""
		for dc in self.drawn_coordinates:
			response = response + "(" + dc + ");"
		return response


	def process_post_data(self, raw_coorindates_str, phone_width, phone_height):
		raw_coordinates = raw_coorindates_str.split(';')
		for rc in raw_coordinates:
			if len(rc) <= 3:
				continue
			rc = rc[1:-1].strip()
			rc = rc + ',' + phone_width + ',' + phone_height
			self.drawn_coordinates.add(rc)