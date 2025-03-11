MOD = 998244353

n, q = map(int, input().split())
s = list(input().strip())

# Initial count of '1's
C1 = s.count('1')

# Precompute 2^(n-4) mod MOD, handling negative exponents
exponent = n - 4
if exponent >= 0:
    pow_2 = pow(2, exponent, MOD)
else:
    inv_exponent = -exponent
    inv_val = pow(2, inv_exponent, MOD)
    pow_2 = pow(inv_val, MOD - 2, MOD)

for _ in range(q):
    i = int(input()) - 1  # Convert to 0-based index
    if s[i] == '1':
        C1 -= 1
        s[i] = '0'
    else:
        C1 += 1
        s[i] = '1'

    sum_a = (2 * C1 - n) % MOD
    sum_a_squared = (sum_a * sum_a) % MOD
    term = (sum_a_squared + n - 2) % MOD
    ans = (pow_2 * term) % MOD
    print(ans)