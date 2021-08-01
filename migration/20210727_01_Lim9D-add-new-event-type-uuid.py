"""
Add new event type: uuid
"""

from yoyo import step

__depends__ = {'20210718_01_E6H4i-add-view-with-event-summary'}

steps = [
    step("ALTER TYPE \"event_type\" ADD VALUE IF NOT EXISTS 'uuid';")
]
