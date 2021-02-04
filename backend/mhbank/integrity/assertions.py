from django.db import connection


def email_uniqueness_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion email_uniqueness " +
            "check(unique(" +
            "select email from Account)) "
        )


def phone_uniqueness_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion phone_uniqueness " +
            "check(unique(" +
            "select phone from Account)) "
        )


def username_uniqueness_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion username_uniqueness " +
            "check(unique(" +
            "select username from Account)) "
        )


def tag_name_uniqueness_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion tag_name_uniqueness " +
            "check(unique(" +
            "select tname from Tag)) "
        )


def subtag_stid_uniqueness_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion subtag_stid_uniqueness " +
            "check(unique(" +
            "select stid from SubTag)) "
        )


def event_ename_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion event_ename_length " +
            "check(not exists( " +
            "select ename from Event where LEN(ename) > 200))"
        )
        cursor.execute(
            "Create assertion event_ename_uniqueness " +
            "check(unique( " +
            "select ename from Event"
        )


def problem_pid_uniqueness_assertion():
    with connection.cursor() as cursor:
        cursor.execute(
            "Create assertion problem_pid_uniqueness " +
            "check(unique(" +
            "select pid from Problem)) "
        )




