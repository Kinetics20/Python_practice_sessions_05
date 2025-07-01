import hashlib
import itertools

def check_hash(candidate: str, target_hash: str, hash_type: str) -> bool:
    h = getattr(hashlib, hash_type)()
    h.update(candidate.encode())
    return h.hexdigest() == target_hash