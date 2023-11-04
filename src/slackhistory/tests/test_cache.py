from ..type.slack_types import CacheSetting


def test_cache_setting():
    cache_setting = CacheSetting.from_dict({
        "active": True,
        "cache_path": "/tmp",
        "cache_prefix": "slack_helper",
        "cache": {
            "channel_list": True,
            "channel_history": True,
            "message_replies": True,
        }
    })

    assert cache_setting.to_dict() == {
        "active": True,
        "cache_path": "/tmp",
        "cache_prefix": "slack_helper",
        "cache": {
            "channel_list": True,
            "channel_history": True,
            "message_replies": True,
        }
    }
