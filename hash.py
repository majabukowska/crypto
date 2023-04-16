import hashlib
import string
import random
import time

def md5(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return md5_hash

def sha256(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash

def sha3(data):
    sha3_hash = hashlib.sha3_256(data.encode()).hexdigest()
    return sha3_hash

def sha1(data):
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    return sha1_hash

def blake2s(data):
    blake2s_hash = hashlib.blake2s(data.encode()).hexdigest()
    return blake2s_hash

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def measure_hash_function_time(hash_func, length_of_string, num_trials):
    total_time = 0
    collisions = 0
    hashes = set()
    for i in range(num_trials):
        data = generate_random_string(length_of_string)
        start_time = time.time()
        hash_value = hash_func(data)
        if hash_value in hashes:
            collisions += 1
        hashes.add(hash_value)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / num_trials
    return (average_time, collisions)



for length in [5, 10, 20, 50, 100]:
    print("String length:", length)
    for hash_func in [md5, sha256, sha3, sha1, blake2s]:
        avg_time, collisions = measure_hash_function_time(hash_func, length, 10000)
        print(hash_func.__name__, f"- Time: {avg_time} seconds, Collisions: {collisions}")