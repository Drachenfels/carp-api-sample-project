from . import v10


class GetUserByPk(v10.GetUserByPk):
    url = '/uid/<user_uid>/'
