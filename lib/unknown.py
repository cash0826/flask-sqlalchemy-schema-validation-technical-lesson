# lib/unknown.py 

from marshmallow import Schema, fields, post_load, ValidationError, INCLUDE, EXCLUDE
from pprint import pprint

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging
        
# schema

class DogSchema(Schema):
    name = fields.Str()
    breed = fields.Str()
    tail_wagging = fields.Boolean()
     
    @post_load
    def make_dog(self, data, **kwargs):
        return Dog(**data)

# validate during deserialization

friendly_dog = '{"name": "Snuggles","breed": "Beagle", "tail_wagging": true, "is_friendly" : true}'

try:
    # default_result = DogSchema().loads(friendly_dog)
    # raise_unknown_error_result = DogSchema(unknown=INCLUDE).loads(friendly_dog)
    # exclude_result = DogSchema(unknown=EXCLUDE).loads(friendly_dog)
    # raise_unknown_error_result2 = DogSchema().loads(friendly_dog, unknown=INCLUDE)
    exclude_result2 = DogSchema().loads(friendly_dog, unknown=EXCLUDE)
    pprint(exclude_result2)  # line not reached if error thrown

except ValidationError as err:
    print(err.messages)    # {'is_friendly': ['Unknown field.']}
    print(err.valid_data)  # {'name': 'Snuggles', 'breed': 'Beagle', 'tail_wagging': True}
    
