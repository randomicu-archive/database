"""
Add view with event summary
"""

from yoyo import step

__depends__ = {'20201026_01_1kkUg-add-new-types-to-event-type'}

steps = [
    step("""
    CREATE VIEW event_groups(day, month, year, language, event_type, count) AS
        SELECT date_part('day'::text, event.created_at)   AS day,
               date_part('month'::text, event.created_at) AS month,
               date_part('year'::text, event.created_at)  AS year,
               event.language,
               event.event_type,
               count(event.event_id)                      AS count
        FROM event
        GROUP BY (date_part('day'::text, event.created_at)), (date_part('month'::text, event.created_at)),
                 (date_part('year'::text, event.created_at)), event.language, event.event_type
        ORDER BY event.language, event.event_type
    """,
    """
     DROP VIEW IF EXISTS event_groups;
    """)
]
