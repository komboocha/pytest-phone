import pytest

from phone import Phone


def test_cannot_initialize_phone_with_invalid_number():
    with pytest.raises(Exception, match='Phone number must be a string starting with 5 or 6 consisting of 9 digits'):
        Phone('1234')


def test_initializing_phone_with_valid_number():
    p = Phone('601234234')
    assert p.phone_number == '601234234'


def test_can_start_call_to_valid_phone_number():
    p = Phone('601234234')
    p.start_call('601234235')
    assert p.call_in_progress


def test_cannot_start_call_to_invalid_phone_number():
    p = Phone('601234234')
    with pytest.raises(Exception, match='Phone number must be a string starting with 5 or 6 consisting of 9 digits'):
        p.start_call('60123')


def test_cannot_start_call_to_own_phone_number():
    p = Phone('601234234')
    with pytest.raises(Exception, match='You cannot call your own number!'):
        p.start_call('601234234')


def test_cannot_start_call_while_call_is_in_progress():
    p = Phone('601234234')
    p.call_in_progress = True
    with pytest.raises(Exception, match='A call is already in progress!'):
        p.start_call('601234235')


def test_can_stop_call_when_call_is_in_progress():
    p = Phone('601234234')
    p.call_in_progress = True
    p.stop_call()
    assert p.call_in_progress is False


def test_cannot_stop_call_when_no_call_is_in_progress():
    p = Phone('601234234')
    p.call_in_progress = False
    with pytest.raises(Exception, match='No call is in progress!'):
        p.stop_call()