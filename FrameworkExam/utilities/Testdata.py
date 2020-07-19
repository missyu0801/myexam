
def valid_data():
    validdata = [['mmhazel.yu@gmail.com', 'Victory@123!'], ['+639654257082', 'Victory@123!']]
    return validdata

def invalid_username():
    invusername = [['notexist@mail.com'], ['09654257082'], ['%@&*!']]
    return invusername

def valid_un_invalid_pw():
    invpass = [['mmhazel.yu@gmail.com', 'isinvalid'], ['+639654257082', 'isinvalid']]
    return invpass

