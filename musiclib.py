from datetime import date
from marshmallow import Schema, fields, pprint

class ArtistSchema(Schema):
    name = fields.Str()

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

artist1 = dict(name='Ween')
album = dict(artist=artist1, title='White Pepper', release_date=date(2000, 5, 2))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result.data, indent=1)