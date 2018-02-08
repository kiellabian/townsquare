import json
from channels import Group


def ws_connect(message):
    Group('users').add(message.reply_channel)


def ws_receive(message):
    Group('users').send({'text': json.dumps(message.as_dict())})


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)
