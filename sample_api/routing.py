from carp_api.routing import router

from sample_api import endpoints


# version number can be string, tuple of strings/integers/mix of both or float
# number (the last one is not encourage as it may cause quirks)
router.enable('1.0', 'user', endpoints=[
    endpoints.user.v10.CreateUser,
    endpoints.user.v10.GetListOfUsers,
])

# we can run enable as many times as we wish in as many places as we wish
router.enable((1, 0), 'user', endpoints=[
    endpoints.user.v10.GetUserByPk,
])

# namespaces is whatever we put there, in this case we have slash and it does
# not make it related to user, it's for developer to build mental
# classification at most
router.enable(1.1, 'user/address', endpoints=[
    # endpoints.address.CreateUserAddress,
    endpoints.address.ChangeUserAddress,
    endpoints.address.DeleteUserAddress,
])

# version 1.1 has new implementation of GetUserByPk, one that returns Address
router.enable(1.1, 'user', endpoints=[
    endpoints.user.v11.GetUserByPk,
])

# in version 1.1 we add a namespace tag, user can tag things
router.enable((1, 2), 'tag', endpoints=[
    endpoints.tag.CreateTag,
    endpoints.tag.GetListOfTags,
])
