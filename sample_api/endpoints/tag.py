from carp_api import endpoint


class CreateTag(endpoint.BaseEndpoint):
    url = '/'

    methods = ['POST']


class GetListOfTags(endpoint.BaseEndpoint):
    url = '/'
