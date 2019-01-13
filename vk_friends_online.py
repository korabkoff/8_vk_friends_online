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
    return getpass.getpass()


def get_online_friends(login, password):
    if not login or not password:
        return None

    apiversion = 5.92
    try:
        session = vk.AuthSession(
                                app_id=APP_ID,
                                user_login=login,
                                user_password=password,
                                scope='friends'
                                )
        api = vk.API(session)

    except vk.exceptions.VkAuthError as er:
        print(er)
        return None

    ids_friends_online = api.friends.getOnline(v=apiversion)

    friends_online = []
    for friend_id in ids_friends_online:
        friend_data = api.users.get(user_ids=(friend_id), v=apiversion)[0]
        friends_online.append(friend_data['first_name'] + ' ' + friend_data['last_name'])

    return friends_online


def output_friends_to_console(friends_online):
    """
    >>> output_friends_to_console(['korabkova Kim','Astahov Name'])
    korabkova Kim
    Astahov Name
    """

    if not friends_online:
        return None

    [print(friend_online) for friend_online in friends_online]


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
