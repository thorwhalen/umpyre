# Problem: Serialize/deserialize from python objects to json and back

# Solution (elements)

It depends what you mean. 

What I mean is "*make a (`json.dump` and `json.load`) serializers/deserializer pair, specific to a class of objects, with the ease of `pickle.dump` and `pickle.load`, but with more control.*"

A few relevant links:
- Marshmallow: <https://github.com/marshmallow-code/marshmallow>
- glom: <https://glom.readthedocs.io/en/latest/>
- remap: <https://sedimental.org/remap.html#collect-interesting-values>
- <https://github.com/i2mint/py2mint/blob/master/py2mint/routing_forest.py>
- <https://github.com/i2mint/py2mint/blob/master/py2mint/switch_case_tree.py>
- <https://github.com/i2mint/py2api/blob/master/py2api/py2rest/input_trans.py>
- <https://github.com/i2mint/py2api/blob/master/py2api/output_trans.py>
