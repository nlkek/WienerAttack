
class Alpha:
    def __init__(self, up, down):
        self.up = up
        self.down = down


def wiener_attack_func(alpha_prev, a_prev, p_prev, q_prev, p_prev_prev, q_prev_prev):
    global l_res
    alpha = Alpha(alpha_prev.down, alpha_prev.up - a_prev * alpha_prev.down)
    if alpha.down == 0:
        return
    a = alpha.up // alpha.down
    p = a * p_prev + p_prev_prev
    q = a * q_prev + q_prev_prev
    l_res.append(p)
    l_res.append(q)
    wiener_attack_func(alpha, a, p, q, p_prev, q_prev)


N = 9449868410449
e = 6792605526025
d = 569


fraction = Alpha(N, e)
l_res = []
alpha_prev_prev = fraction
a_prev_prev = fraction.up // fraction.down
p_prev_prev = 1
q_prev_prev = 1
alpha_prev = Alpha(alpha_prev_prev.down, alpha_prev_prev.up - a_prev_prev * alpha_prev_prev.down)
a_prev = alpha_prev.up // alpha_prev.down
p_prev = a_prev_prev * a_prev + 1
q_prev = a_prev


if __name__ == "builtins":
    wiener_attack_func(alpha_prev, a_prev, p_prev, q_prev, p_prev_prev, q_prev_prev)
    for i in l_res[::2]:
        if i == d:
            print("success! d = {:d}".format(i))


