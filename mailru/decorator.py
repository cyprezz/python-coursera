import json
import functools


def to_json(func):
    @functools.wraps(func)
    def compiled(*args, **kwargs):
        return str(json.dumps(func(*args, **kwargs)))
    return compiled


@to_json
def get_data():
    return {
        'data': 42
    }
