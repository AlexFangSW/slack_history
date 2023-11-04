from ..type.slack_types import ChannelHistory


def test_slack_channel_history():
    channel_history = ChannelHistory.from_dict({
        "ok": True,
        "oldest": "1690899691.477708",
        "messages": [{
            "client_msg_id": "XXXXX",
            "type": "message",
            "text": "test message",
            "user": "XXXXX",
            "ts": "1691501749.923719",
            "blocks": [{
                "type":
                    "rich_text",
                "block_id":
                    "B7=Ub",
                "elements": [{
                    "type": "rich_text_section",
                    "elements": [{
                        "type": "text",
                        "text": "test message"
                    }]
                }]
            }],
            "team": "XXXXX"
        }, {
            "client_msg_id": "XXXXX",
            "type": "message",
            "text": "test message!!!",
            "user": "XXXXX",
            "ts": "1691499518.024189",
            "blocks": [{
                "type":
                    "rich_text",
                "block_id":
                    "2Box9",
                "elements": [{
                    "type": "rich_text_section",
                    "elements": [{
                        "type": "text",
                        "text": "test message!!!"
                    }]
                }]
            }],
            "team": "XXXXX",
            "thread_ts": "1691499518.024189",
            "reply_count": 1,
            "reply_users_count": 1,
            "latest_reply": "1691499544.897429",
            "reply_users": ["XXXXX"],
            "is_locked": False,
            "subscribed": False
        }, {
            "type": "message",
            "subtype": "channel_join",
            "ts": "1691499141.163529",
            "user": "XXXXX",
            "text": "<@XXXXX> \u5df2\u52a0\u5165\u983b\u9053",
            "inviter": "XXXXX"
        }, {
            "type": "message",
            "subtype": "bot_add",
            "text": "added an integration to this channel: <XXXXX>",
            "user": "XXXXX",
            "bot_id": "XXXXX",
            "bot_link": "<XXXXX>",
            "ts": "1691498801.191669"
        }],
        "has_more": False,
        "pin_count": 0,
        "channel_actions_ts": None,
        "channel_actions_count": 0
    })

    assert channel_history.to_dict() == {
        'ok':
            True,
        'has_more':
            False,
        'oldest':
            '1690899691.477708',
        'messages': [{
            'client_msg_id': 'XXXXX',
            'type': 'message',
            'text': 'test message',
            'user': 'XXXXX',
            'ts': '1691501749.923719',
            'blocks': [{
                'type':
                    'rich_text',
                'block_id':
                    'B7=Ub',
                'elements': [{
                    'type': 'rich_text_section',
                    'elements': [{
                        'type': 'text',
                        'text': 'test message'
                    }]
                }]
            }],
            'team': 'XXXXX'
        }, {
            'client_msg_id': 'XXXXX',
            'type': 'message',
            'text': 'test message!!!',
            'user': 'XXXXX',
            'ts': '1691499518.024189',
            'blocks': [{
                'type':
                    'rich_text',
                'block_id':
                    '2Box9',
                'elements': [{
                    'type': 'rich_text_section',
                    'elements': [{
                        'type': 'text',
                        'text': 'test message!!!'
                    }]
                }]
            }],
            'team': 'XXXXX',
            'thread_ts': '1691499518.024189',
            'reply_count': 1,
            'reply_users_count': 1,
            'latest_reply': '1691499544.897429',
            'reply_users': ['XXXXX'],
            'is_locked': False,
            'subscribed': False
        }, {
            'type': 'message',
            'subtype': 'channel_join',
            'ts': '1691499141.163529',
            'user': 'XXXXX',
            'text': '<@XXXXX> 已加入頻道',
            'inviter': 'XXXXX'
        }, {
            'type': 'message',
            'subtype': 'bot_add',
            'text': 'added an integration to this channel: <XXXXX>',
            'user': 'XXXXX',
            'bot_id': 'XXXXX',
            'bot_link': '<XXXXX>',
            'ts': '1691498801.191669'
        }]
    }
