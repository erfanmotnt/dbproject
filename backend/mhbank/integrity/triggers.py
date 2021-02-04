from django.db import connection


def phone_trigger():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create trigger phone_trigger " +
            "before insert on Account " +
            "referencing new as nt " +
            "for each row when(" +
            "nt.phone like '09%' " +
            "SIGNAL.SQL State '7005' ('phone number is invalid'))"
        )


def stt_comment_trigger():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create trigger comment_trigger " +
            "before insert on STT " +
            "referencing new as nstt " +
            "for each row when(" +
            "LEN(nstt.comment) > 10000 " +
            "SIGNAL.SQL State '7005' ('comment is very long'))"
        )


def st_level_trigger():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create trigger st_level_trigger " +
            "before insert on ST " +
            "referencing new as nst " +
            "for each row when(" +
            "nst.level < 1 AND nst.level > 5 " +
            "SIGNAL.SQL State '7005' ('level isn't in range'))"
        )


def problem_minaar_trigger():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create trigger minaar_trigger " +
            "before insert on Problem " +
            "referencing new as np " +
            "for each row when(" +
            "nst.level < 1 AND nst.level > 12 " +
            "SIGNAL.SQL State '7005' ('minaar isn't in range'))"
        )
