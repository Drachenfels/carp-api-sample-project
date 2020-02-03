from carp_api import endpoint


class CreateUserAddress(endpoint.BaseEndpoint):
    url = '/'

    methods = ['POST']

    @classmethod
    def get_final_url(cls, version, namespace, host=None):
        return '/{version}/user/uid/<id>/address/'.format(version=version)


class ChangeUserAddress(endpoint.BaseEndpoint):
    url = '/'

    methods = ['PUT']

    @classmethod
    def get_final_url(cls, version, namespace, host=None):
        return (
            '/{version}/user/uid/<user_id>/address/uid/<address_id>/'.format(
                version=version
            )
        )


class DeleteUserAddress(endpoint.BaseEndpoint):
    url = '/'

    methods = ['DELETE']

    propagate = False
