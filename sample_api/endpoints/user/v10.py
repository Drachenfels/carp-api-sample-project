from carp_api import endpoint


class CreateUser(endpoint.BaseEndpoint):
    url = '/'

    methods = ['POST']


class GetListOfUsers(endpoint.BaseEndpoint):
    """Get list of available users
    """
    url = '/'

    name = 'get_user'

    def action(self):
        return [
            ('John', 'Doe', 'New York'),
            ('Jane', 'Doe', 'London'),
            ('Santa', 'Claus', 'Lapland'),
        ]


class GetUserByPk(endpoint.BaseEndpoint):
    url = '/uid/<user_id>'
