from _typeshed import Incomplete

class UsBankAccountVerificationGateway:
    gateway: Incomplete
    config: Incomplete
    def __init__(self, gateway) -> None: ...
    def confirm_micro_transfer_amounts(self, verification_id, amounts): ...
    def find(self, verification_id): ...
    def search(self, *query): ...