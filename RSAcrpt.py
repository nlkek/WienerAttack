
def encrypt_file(file_to_encrypt, encrypted_file, e=13, n=21079):
    #
    print("encrypting file...")
    f_in = open(file_to_encrypt, 'br')
    f_out = open(encrypted_file, 'w')
    for byte in f_in.read():
        byte = byte**e % n
        f_out.write(str(byte) + '\n')
    f_in.close()
    f_out.close()
    print("finished")


def decrypt_file(file_to_decrypt, decrypted_file, d=9589, n=21079):
    #
    print("decrypting file...")
    f_in = open(file_to_decrypt, 'r')
    f_out = open(decrypted_file, 'bw')
    for byte in f_in:
        byte_ = int(byte)**d % n
        # bytes([])  [] is necessary
        f_out.write(bytes([byte_]))
    f_in.close()
    f_out.close()
    print("finished")


def euler_func(p, q):
    return (p-1)*(q-1)


def is_coprime(a, b):
    if euclid(a, b) == 1:
        return True
    else:
        return False


def euclid(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return euclid(b, r)


def extended_euclid(euler_func_ret, e):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while e > 0:
        q = euler_func_ret // e
        r = euler_func_ret % e
        x = x2 - q * x1
        y = y2 - q * y1
        euler_func_ret = e
        e = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return y2

if __name__ == 'builtins':
    p = 107
    q = 197
    n = p*q
    e = 13
    d = extended_euclid(euler_func(p, q), e)
    print("p={:d} q={:d} n={:d} e={:d} d={:d}".format(p, q, n, e, d))