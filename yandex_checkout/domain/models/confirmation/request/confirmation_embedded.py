# -*- coding: utf-8 -*-
from yandex_checkout.domain.common.confirmation_type import ConfirmationType
from yandex_checkout.domain.models.confirmation.request.confirmation_request import \
    ConfirmationRequest


class ConfirmationEmbedded(ConfirmationRequest):
    """
    Class representing embedded confirmation data object
    """

    def __init__(self, *args, **kwargs):
        super(ConfirmationEmbedded, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.EMBEDDED:
            self.type = ConfirmationType.EMBEDDED
