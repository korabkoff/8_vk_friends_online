import vk
import getpass


def get_user_login():
    try:
        login = input('Login: ')
        return login

    except ValueError:
        return None


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    if not login or not password:
        return None

    try:
        session = vk.AuthSession(
                                app_id=6807175,
                                user_login=login,
                                user_password=password,
                                scope='friends'
                                )
        api = vk.API(session)

    except vk.exceptions.VkAuthError:
        return None

    all_friends_data = api.friends.get(fields=('first_name, last_name', 'online'), v=5.92)['items']

    friends_online = []
    for friend_data in all_friends_data:
        if friend_data['online'] == 1:
            first_name = friend_data['first_name']
            last_name = friend_data['last_name']
            friends_online.append(first_name + ' ' + last_name)

    return friends_online


def output_friends_to_console(friends_online):
    """
    >>> output_friends_to_console(['korabkova Kim','Astahov'])
    korabkova Kim
    Astahov
    """

    if not friends_online:
        return None

    [print(friend_online) for friend_online in friends_online]


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
