try:
    import cPickle as pickle
except ImportError:
    import pickle
import json

d = dict(name = 'zzp', age = 23)
print pickle.dumps(d)
print json.dumps(d)