from typing import List
from enum import IntEnum
import base58
from nacl.signing import VerifyKey

# Fake blockhash so this example doesn't need a network connection. It should be queried from the cluster in normal use.
FAKE_RECENT_BLOCKHASH = "11111111111111111111111111111111"


def verify_signature(from_public_key: bytes, message: bytes, signature: bytes):
    assert len(signature) == 64, "signature size incorrect"
    verify_key = VerifyKey(from_public_key)
    verify_key.verify(message, signature)


class SystemInstruction(IntEnum):
    CreateAccount           = 0x00
    Assign                  = 0x01
    Transfer                = 0x02
    GetTxResult             = 0x03


# class MessageHeader:
#     def __init__(self, num_required_signatures: int, num_readonly_signed_accounts: int, num_readonly_unsigned_accounts: int):
#         self.num_required_signatures = num_required_signatures
#         self.num_readonly_signed_accounts = num_readonly_signed_accounts
#         self.num_readonly_unsigned_accounts = num_readonly_unsigned_accounts

#     def serialize(self) -> bytes:
#         return self.num_required_signatures.to_bytes(1, byteorder='little') + \
#                self.num_readonly_signed_accounts.to_bytes(1, byteorder='little') + \
#                self.num_readonly_unsigned_accounts.to_bytes(1, byteorder='little')

# class AccountMeta:
#     pubkey: bytes
#     is_signer: bool
#     is_writable: bool
#     def __init__(self, pubkey: bytes, is_signer: bool, is_writable: bool):
#         self.pubkey = pubkey
#         self.is_signer = is_signer
#         self.is_writable = is_writable

# Only support Transfer instruction for now
# TODO add other instructions if the need arises
class Instruction:
    data: bytes
    to_pubkey: bytes
    ticker: bytes
    def serialize(self) -> bytes:
        serialized: bytes = self.to_pubkey
        serialized += len(self.ticker).to_bytes(1, byteorder='little')
        serialized += self.ticker
        serialized += self.data
        return serialized

class TxResultInstruction:
    from_pubkey: bytes
    chain_pubkey: bytes
    ref_block_number: bytes
    method_name: bytes
    to_pubkey: bytes
    ticker: bytes
    data: bytes
    def serialize(self) -> bytes:
        serialized: bytes = self.from_pubkey
        serialized += self.chain_pubkey
        serialized += self.ref_block_number
        serialized += len(self.method_name).to_bytes(8, byteorder='little')
        serialized += self.method_name
        serialized += self.to_pubkey
        serialized += len(self.ticker).to_bytes(1, byteorder='little')
        serialized += self.ticker
        serialized += self.data
        return serialized

class SystemInstructionTransfer(Instruction):
    def __init__(self, to_pubkey: bytes, ticker: bytes, amount: bytes):
        self.data =  (amount).to_bytes(8, byteorder='little')
        self.to_pubkey = to_pubkey
        self.ticker = ticker
class SystemInstructionGetTxResult(TxResultInstruction):
    def __init__(self, from_pubkey: bytes, chain_pubkey: bytes, ref_block_number: int, method_name: bytes, to_pubkey : bytes, ticker: bytes, amount: int):
        self.from_pubkey = from_pubkey
        self.chain_pubkey = chain_pubkey
        self.ref_block_number = (ref_block_number).to_bytes(8, byteorder='little')
        self.method_name = method_name
        self.to_pubkey = to_pubkey
        self.ticker = ticker
        self.data = (amount).to_bytes(8, byteorder='little')
class MessageTransfer:
    recent_blockhash: bytes
    instruction: Instruction

    def __init__(self, instruction: Instruction):
        self.recent_blockhash = base58.b58decode(FAKE_RECENT_BLOCKHASH)
        self.instruction = instruction

    def serialize(self) -> bytes:
        serialized: bytes = self.recent_blockhash
        serialized += self.instruction.serialize()
        return serialized

class MessageTxResult:
    recent_blockhash: bytes
    txResultInstruction: TxResultInstruction

    def __init__(self, txResultInstruction: TxResultInstruction):
        self.recent_blockhash = base58.b58decode(FAKE_RECENT_BLOCKHASH)
        self.txResultInstruction = txResultInstruction

    def serialize(self) -> bytes:
        serialized: bytes = self.recent_blockhash
        serialized += self.txResultInstruction.serialize()
        return serialized
