from carp_api import endpoint


class CreateUserAddress(endpoint.BaseEndpoint):
    url = '/'

    methods = ['POST']

    def get_final_url(self, host=None):
        version = self.get_version()

        return '/{version}/user/uid/<user_uid>/address/'.format(
            version=version)


class ChangeUserAddress(endpoint.BaseEndpoint):
    url = '/'

    methods = ['PUT']

    def get_final_url(self, host=None):
        version = self.get_version()

        return (
            '/{version}/user/uid/<user_uid>/address/uid/<address_uid>/'.format(
                version=version
            )
        )


class DeleteUserAddress(endpoint.BaseEndpoint):
    url = '/'

    methods = ['DELETE']

    propagate = False
