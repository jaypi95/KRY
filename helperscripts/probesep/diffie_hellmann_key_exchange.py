import random

###### INPUT ######
# 1. A prime number p
p = 23
# 2. A base g
g = 5
# 3. Alice's secret number a
a = random.randint(2, p - 1)
# a = 4 # if you want to use a specific number
# 4. Bob's secret number b
b = random.randint(2, p - 1)
###################

###### CONSTANTS ######
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text
#######################

def calculate_public_key(g, a, p):
    return (g ** a) % p

def calculate_shared_secret(B, a, p):
    return (B ** a) % p

def confirm_shared_secret(sA, sB):
    return sA == sB

A = calculate_public_key(g, a, p)
B = calculate_public_key(g, b, p)

sA = calculate_shared_secret(B, a, p)
sB = calculate_shared_secret(A, b, p)


print(f"Alice's public key: {BOLD}{A}{RESET}")
print(f"Bob's public key: {BOLD}{B}{RESET}")
print(f"Alice's shared secret: {BOLD}{sA}{RESET}")
print(f"Bob's shared secret: {BOLD}{sB}{RESET}")

if confirm_shared_secret(sA, sB):
    print(f"{GREEN}Shared secret confirmed!{RESET}")
else:
    print(f"{RED}Shared secret not confirmed!{RESET}")