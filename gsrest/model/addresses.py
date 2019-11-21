# TODO: put compute_balance() in a general module
from gsrest.model.blocks import ConvertedValue


def compute_balance(total_received_value, total_spent_value,
                    rates):
    balance_value = total_received_value - total_spent_value
    balance = ConvertedValue(balance_value, rates)
    return balance


class Address(object):
    """ Model representing an address """

    def __init__(self, address, addressId, firstTx, lastTx, noIncomingTxs,
                 noOutgoingTxs, totalReceived, totalSpent, inDegree,
                 outDegree):
        self.address = address
        self.addressId = addressId
        self.firstTx = firstTx
        self.lastTx = lastTx
        self.noIncomingTxs = noIncomingTxs
        self.noOutgoingTxs = noOutgoingTxs
        self.totalReceived = totalReceived
        self.totalSpent = totalSpent
        self.inDegree = inDegree
        self.outDegree = outDegree
#        self.balance = compute_balance(totalReceived.satoshi,
#                                        totalSpent.satoshi,
#                                        0)

    @staticmethod
    def from_row(row):
        return Address(row.address, row.address_id, row.first_tx, row.last_tx,
                       row.no_incoming_txs, row.no_outgoing_txs,
                       row.total_received, row.total_spent,
                       row.in_degree, row.out_degree)

    def to_dict(self):
        return self.__dict__
