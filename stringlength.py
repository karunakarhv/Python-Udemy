def password_controller(value):
    if(len(value) < 8):
        return False
    else:
        return True

password_controller("Karun")