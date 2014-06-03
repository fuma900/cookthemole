# CookTheMole API implemetned using Google Cloud Endpoints

import endpoints, logging
from parse_url import parseCollection
from protorpc import messages
from protorpc import message_types
from protorpc import remote

WEB_CLIENT_ID = '743605158714-vfjtaobdqlgshs7157r43e1ohntdkbe6.apps.googleusercontent.com'
package = 'cookthemole_api'

# Define the model for a single direction (or step) of a reciepe.
class Directions(messages.Message):
	"""Greeting that stores a message."""
	index = messages.IntegerField(1)
	sentence = messages.StringField(2)
	time = messages.IntegerField(3)

# Define the model for a collection of directions (or steps) of a reciepe.
class DirectionsCollection(messages.Message):
	"""Collection of Greetings."""
	length = messages.IntegerField(1)
	steps = messages.MessageField(Directions, 2, repeated=True)

############################# Example ################################
STORED_DIRECTIONS = DirectionsCollection(steps=[
	Directions(sentence='hello world!'),
	Directions(sentence='goodbye world!'),
])
######################################################################

# Here starts the API itself
# Declaration of API features
@endpoints.api(name='cookthemole', version='v1', 
				allowed_client_ids=[WEB_CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID],
				scopes=[endpoints.EMAIL_SCOPE])
class CookTheMoleApi(remote.Service):
	"""CookTheMole API v1."""
	# API method to retrieve the directions of a reciepe using parseCollection() function (See parse_url.py for more info)
	@endpoints.method(Directions, DirectionsCollection,
						path='directionsCollection', http_method='POST',
						name='directions.getDirectionsCollection')
	def get_directions_collection(self, request):
		current_user = endpoints.get_current_user()
		logging.info(current_user.email() if current_user is not None
             else 'Anonymous')
		current_user = endpoints.get_current_user()
		try:
			response = parseCollection(request)
			length = response['length']
			steps = response['steps']
			return DirectionsCollection(length=length, steps=steps)
		except (IndexError, TypeError):
			raise endpoints.NotFoundException('Reciepe url "%s" not found.' %
											  (request.sentence,))

# Starts the API server
APPLICATION = endpoints.api_server([CookTheMoleApi])
