def _validate_phone_number(phone_number):
    """Validates if phone number is a string starting with 5 or 6 and has nine digits"""
    if not (phone_number.isdigit() and phone_number.startswith(('5', '6')) and len(phone_number) == 9):
        raise Exception('Phone number must be a string starting with 5 or 6 consisting of 9 digits')


class Phone:
    """
    Models behavior of a phone
    """

    def __init__(self, phone_number):
        _validate_phone_number(phone_number)
        self.phone_number = phone_number
        self.call_in_progress = False

    def start_call(self, phone_number):
        """
        Starts a new call if no call is currently in progress
        Raises exception when trying to use invalid phone number,
        your own phone number or some call already in progress.
        """
        _validate_phone_number(phone_number)
        if self.call_in_progress:
            raise Exception('A call is already in progress!')
        elif phone_number == self.phone_number:
            raise Exception('You cannot call your own number!')
        else:
            self.call_in_progress = True

    def stop_call(self):
        """Stops call if call is in progress. Raises Exception if no call in progress"""
        if not self.call_in_progress:
            raise Exception('No call is in progress!')
        else:
            self.call_in_progress = False
