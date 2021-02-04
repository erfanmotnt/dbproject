from django.db import connection


def phone_trigger():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create trigger phone_trigger " +
            "before insert of phone on Account " +
            "referencing new as nt " +
            "for each row when(" +
            "nt.phone like '09%' " +
            "SIGNAL.SQL State '7005' ('phone number is invalid'))"
        )


def stt_comment_trigger():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create trigger comment_trigger " +
            "before insert of comment on STT " +
            "referencing new as nstt " +
            "for each row when(" +
            "LEN(nstt.comment) > 10000 " +
            "SIGNAL.SQL State '7005' ('comment is very long'))"
        )