from ..type.slack_types import Channel, ChannelList, ChannelResponseMetadata, MessageAndReplies, Replies, SlackMessageAndReply


def test_slack_replies():
    reply = Replies.from_dict({
        "ok": True,
        "messages": [{
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
            "client_msg_id": "XXXXX",
            "type": "message",
            "text": "test reply!!!",
            "user": "XXXXX",
            "ts": "1691499544.897429",
            "blocks": [{
                "type":
                    "rich_text",
                "block_id":
                    "dIFJ",
                "elements": [{
                    "type": "rich_text_section",
                    "elements": [{
                        "type": "text",
                        "text": "test reply!!!"
                    }]
                }]
            }],
            "team": "XXXXX",
            "thread_ts": "1691499518.024189",
            "parent_user_id": "XXXXX"
        }],
        "has_more": False
    })

    assert reply.to_dict() == {
        'ok':
            True,
        "has_more":
            False,
        "response_metadata": {
            "next_cursor": None
        },
        'messages': [{
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
            'client_msg_id': 'XXXXX',
            'type': 'message',
            'text': 'test reply!!!',
            'user': 'XXXXX',
            'ts': '1691499544.897429',
            'blocks': [{
                'type':
                    'rich_text',
                'block_id':
                    'dIFJ',
                'elements': [{
                    'type': 'rich_text_section',
                    'elements': [{
                        'type': 'text',
                        'text': 'test reply!!!'
                    }]
                }]
            }],
            'team': 'XXXXX',
            'thread_ts': '1691499518.024189',
            'parent_user_id': 'XXXXX'
        }]
    }


def test_slack_channel():
    channel = Channel.from_dict({
        "id": "XXXXX",
        "name": "alex-playground",
        "is_channel": True,
        "is_group": False,
        "is_im": False,
        "is_mpim": False,
        "is_private": True,
        "created": 1679889137,
        "is_archived": False,
        "is_general": False,
        "unlinked": 0,
        "name_normalized": "alex-playground",
        "is_shared": False,
        "is_org_shared": False,
        "is_pending_ext_shared": False,
        "pending_shared": [],
        "context_team_id": "XXXXX",
        "updated": 1679889137927,
        "parent_conversation": None,
        "creator": "XXXXX",
        "is_ext_shared": False,
        "shared_team_ids": ["XXXXX"],
        "pending_connected_team_ids": [],
        "is_member": True,
        "topic": {
            "value": "",
            "creator": "",
            "last_set": 0
        },
        "purpose": {
            "value": "Yeeeee",
            "creator": "XXXXX",
            "last_set": 1679889137
        },
        "num_members": 2
    })

    assert channel.to_dict() == {'id': 'XXXXX', 'name': 'alex-playground'}


def test_slack_channel_response_metadata():
    meta = ChannelResponseMetadata.from_dict({"next_cursor": "XXXXX"})

    assert meta.to_dict() == {"next_cursor": "XXXXX"}


def test_slacke_channel_list():
    channel_list = ChannelList.from_dict({
        "ok": True,
        "channels": [{
            "id": "XXXXX",
            "name": "random-yeeee",
            "is_channel": True,
            "is_group": False,
            "is_im": False,
            "is_mpim": False,
            "is_private": False,
            "created": 1592755831,
            "is_archived": False,
            "is_general": False,
            "unlinked": 0,
            "name_normalized": "random-yeeee",
            "is_shared": False,
            "is_org_shared": False,
            "is_pending_ext_shared": False,
            "pending_shared": [],
            "context_team_id": "XXXXX",
            "updated": 1592755831335,
            "parent_conversation": None,
            "creator": "XXXXX",
            "is_ext_shared": False,
            "shared_team_ids": ["XXXXX"],
            "pending_connected_team_ids": [],
            "is_member": False,
            "topic": {
                "value": "random conversation",
                "creator": "XXXXX",
                "last_set": 1592755831
            },
            "purpose": {
                "value": "random conversation.",
                "creator": "XXXXX",
                "last_set": 1592755831
            },
            "previous_names": [],
            "num_members": 123
        }, {
            "id": "XXXXX",
            "name": "alex-playground",
            "is_channel": True,
            "is_group": False,
            "is_im": False,
            "is_mpim": False,
            "is_private": True,
            "created": 1679889137,
            "is_archived": False,
            "is_general": False,
            "unlinked": 0,
            "name_normalized": "alex-playground",
            "is_shared": False,
            "is_org_shared": False,
            "is_pending_ext_shared": False,
            "pending_shared": [],
            "context_team_id": "XXXXX",
            "updated": 1679889137927,
            "parent_conversation": None,
            "creator": "XXXXX",
            "is_ext_shared": False,
            "shared_team_ids": ["XXXXX"],
            "pending_connected_team_ids": [],
            "is_member": True,
            "topic": {
                "value": "",
                "creator": "",
                "last_set": 0
            },
            "purpose": {
                "value": "Yeeeee",
                "creator": "XXXXX",
                "last_set": 1679889137
            },
            "num_members": 2
        }],
        "response_metadata": {
            "next_cursor": "XXXXX"
        }
    })

    assert channel_list.to_dict() == {
        'ok': True,
        'channels': [{
            'id': 'XXXXX',
            'name': 'random-yeeee'
        }, {
            'id': 'XXXXX',
            'name': 'alex-playground'
        }],
        'response_metadata': {
            'next_cursor': 'XXXXX'
        }
    }


def test_message_and_reply():
    msg_and_reply = MessageAndReplies.from_dict({
        "msg": {
            "text": "qqq",
            "ts": "121331.1331",
            "reply_count": 1
        },
        "replies": [{
            "text": "the reply",
            "ts": "121331.1331",
            "reply_count": 0
        }]
    })
    assert msg_and_reply.to_dict() == {
        'msg': {
            'text': 'qqq',
            'ts': '121331.1331',
            'reply_count': 1
        },
        'replies': [{
            'text': 'the reply',
            'ts': '121331.1331',
            'reply_count': 0
        }]
    }


def test_slack_message_and_reply():
    slack_msg_and_reply = SlackMessageAndReply.from_dict({
        "ok":
            True,
        "channel_name":
            "dummy",
        "channel_id":
            "XXXXX",
        "start_date":
            "2023-10-1",
        "start_ts":
            "1691499518.024189",
        "end_date":
            "2023-10-1",
        "end_ts":
            "1691499518.024189",
        "messages": [{
            'msg': {
                'text': 'qqq',
                'ts': '121331.1331',
                'thread_ts': '',
                'reply_count': 1
            },
            'replies': [{
                'text': 'the reply',
                'ts': '121331.1331',
                'thread_ts': '',
                'reply_count': 0
            }]
        }]
    })

    assert slack_msg_and_reply.to_dict() == {
        "ok":
            True,
        "channel_name":
            "dummy",
        "channel_id":
            "XXXXX",
        "start_date":
            "2023-10-1",
        "start_ts":
            "1691499518.024189",
        "end_date":
            "2023-10-1",
        "end_ts":
            "1691499518.024189",
        "messages": [{
            'msg': {
                'text': 'qqq',
                'ts': '121331.1331',
                'thread_ts': '',
                'reply_count': 1
            },
            'replies': [{
                'text': 'the reply',
                'ts': '121331.1331',
                'thread_ts': '',
                'reply_count': 0
            }]
        }]
    }
