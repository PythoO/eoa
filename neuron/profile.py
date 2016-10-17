import config
data = 0


def load_profile():
    """
    Function to load the VA configuration.
    :return:
    """
    print('loading profile')
    global data
    data = config.data
