# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.models.confirmation.request.confirmation_request import \
    ConfirmationRequest


class ConfirmationRedirect(ConfirmationRequest):
    """
    Class representing redirect confirmation data object
    """
    __return_url = None

    __enforce = None

    def __init__(self, *args, **kwargs):
        super(ConfirmationRedirect, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.REDIRECT:
            self.type = ConfirmationType.REDIRECT

    @property
    def return_url(self):
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        cast_value = str(value)
        if cast_value:
            self.__return_url = cast_value
        else:
            raise ValueError('Invalid returnUrl value')

    @property
    def enforce(self):
        return self.__enforce

    @enforce.setter
    def enforce(self, value):
        self.__enforce = bool(value)
