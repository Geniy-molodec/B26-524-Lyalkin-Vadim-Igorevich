import re
login_re = re.compile(r"[A-Za-z][A-Za-z0-9_]{3,15}")
def is_valid_login(login):
    return login_re.fullmatch(login) is not None
LOGINS = [
    # из условия
    "user_123", "admin", "123user", "ab", "user-name", "very_long_username",

    # границы длины
    "abc", "abcd", "abcdefghijklmnop", "abcdefghijklmnopq", "", "a",

    # первый символ
    "_user", "1abc", "-abc", "Admin", "ZZZZ", "A123",

    # допустимые символы
    "a_b_c_d", "user____", "USER_123_abc", "a1b2c3d4", "test0000",

    # недопустимые символы
    "user name", "user.name", "user@mail", "user!", "user$$",
    " user", "user ", "user\n", "user\t", "\nuser",

    # юникод
    "юзер123", "userй", "usér", "user٣٣", "ｕｓｅｒ", "😀user",
]
for login in LOGINS:
    print(f"{login} -> {is_valid_login(login)}")