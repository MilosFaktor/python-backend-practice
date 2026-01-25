# transform.py

from xs14.models import PayloadRaw, UserOut


def get_active_users(payload_raw: PayloadRaw) -> list[UserOut]:
    users = payload_raw.message
    users_out = []
    for user in users:
        if user.active is True:
            id = user.id
            name = user.name
            user_out = UserOut(id=id, name=name)
            users_out.append(user_out)

    return users_out
