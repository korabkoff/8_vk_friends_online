import vk
import getpass


APP_ID = 6807175  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev

def get_user_login():
    try:
        login = input('Login: ')
        return login

    except ValueError:
        print("Invalid input")
        return None


def get_user_password():
    try:
        password = getpass()
        return password

    except ValueError:
        print("Invalid input")
        return None


def get_online_friends(login, password):
    if not login or not password:
        return None

    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    vk_friends = api.friends.get.fields(status)
    return friends_online

def output_friends_to_console(friends_online):
    print([friend_online for friend_online in friends_online])
    # return friends_online



    return parser.parse_args(args)
if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
