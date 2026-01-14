"""PlayVideo SDK Resources."""

from playvideo.resources.collections import SyncCollections, AsyncCollections
from playvideo.resources.videos import SyncVideos, AsyncVideos
from playvideo.resources.webhooks import SyncWebhooks, AsyncWebhooks
from playvideo.resources.embed import SyncEmbed, AsyncEmbed
from playvideo.resources.api_keys import SyncApiKeys, AsyncApiKeys
from playvideo.resources.account import SyncAccount, AsyncAccount
from playvideo.resources.usage import SyncUsage, AsyncUsage

__all__ = [
    "SyncCollections",
    "AsyncCollections",
    "SyncVideos",
    "AsyncVideos",
    "SyncWebhooks",
    "AsyncWebhooks",
    "SyncEmbed",
    "AsyncEmbed",
    "SyncApiKeys",
    "AsyncApiKeys",
    "SyncAccount",
    "AsyncAccount",
    "SyncUsage",
    "AsyncUsage",
]
