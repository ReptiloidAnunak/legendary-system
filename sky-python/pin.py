def check_pin(pin):
    int_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(pin) != 4:
        return False
    else:
        pass
    for number in pin:
        if number in int_num:
            pass
        else:
            return False

    return True
