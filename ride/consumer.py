# # your_app/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from ride.models import RideLocation

class RideLocationConsumer(WebsocketConsumer):
    print("in ride location consumer")
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data, pk):
        ride_location_data = json.loads(text_data)
        ride_id = ride_location_data['ride_id']
        latitude = ride_location_data['latitude']
        longitude = ride_location_data['longitude']

        # Assuming RideLocation model has a 'ride' ForeignKey field
        RideLocation.objects.create(ride=ride_id, latitude=latitude, longitude=longitude)

    def update_location(self, event):
        self.send(text_data=json.dumps(event))
