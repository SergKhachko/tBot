import json
import jsonpickle


def tb_message_to_dict(message):
    return json.loads(jsonpickle.encode(message))
