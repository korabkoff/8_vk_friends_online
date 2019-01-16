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


def get_online_friends_data(login, password, app_id, version):
    if not login or not password:
        return None

    try:
        session = vk.AuthSession(
            app_id=app_id,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        online_friends_data = api.users.get(user_ids=(api.friends.getOnline(v=version)), v=version)

    except vk.exceptions.VkAuthError:
        online_friends_data = None

    return online_friends_data


def output_friends_to_console(friends_online):
    """
    >>> output_friends_to_console(['korabkova Kim','Astahov'])
    korabkova Kim
    Astahov
    """

    if not friends_online:
        print('Something goes wrong')
        return None
    if friends_online == []:
        print('No friends oline :(')
        return None

    [print(friend_online) for friend_online in friends_online]


if __name__ == '__main__':

    login = get_user_login()

    password = get_user_password()

    app_id = 6807175
    version = 5.92
    online_friends_data = get_online_friends_data(login, password, app_id, version)

    friends_online = []
    try:
        for friend_data in online_friends_data:
            friends_online.append('{} {}'.format(friend_data['first_name'], friend_data['last_name']))
    except TypeError:
        friends_online = None

    output_friends_to_console(friends_online)
