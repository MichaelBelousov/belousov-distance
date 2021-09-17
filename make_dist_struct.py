# frequency chart copy+pasted from http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

source = """E   21912       E   12.02
T   16587       T   9.10
A   14810       A   8.12
O   14003       O   7.68
I   13318       I   7.31
N   12666       N   6.95
S   11450       S   6.28
R   10977       R   6.02
H   10795       H   5.92
D   7874        D   4.32
L   7253        L   3.98
U   5246        U   2.88
C   4943        C   2.71
M   4761        M   2.61
F   4200        F   2.30
Y   3853        Y   2.11
W   3819        W   2.09
G   3693        G   2.03
P   3316        P   1.82
B   2715        B   1.49
V   2019        V   1.11
K   1257        K   0.69
X   315         X   0.17
Q   205         Q   0.11
J   188         J   0.10
Z   128         Z   0.07"""

table = [[c.strip() for c in r.split()] for r in source.lower().split('\n')]
freqs = {k[0]:k[3] for k in table}
_64bit_segments = {k:max(1, round(64*(float(v)/100))) for k,v in freqs.items()}
# assert sum(_64bit_segments.values()) == 64, "64bit_segments not 64"

print(f"""
typedef struct Dist {{
    unsigned {','.join(f'{c}:{size}' for c,size in _64bit_segments.items())};
}} Dist;
""")

null = "'\\0'"
case_sep = '\n' + 3*4*' '

print(f"""
Dist hash(const char* const str) {{
    Dist result;
    for (const char* c = str; *c != {null}; ++c) {{
        switch (*c) {{
            {case_sep.join(f"case '{c.upper()}':{case_sep}case '{c}': result.{c} = result.{c} >= {2**size - 1} ? result.{c} : result.{c} + 1; break;" for c,size in _64bit_segments.items())}
        }}
    return result;
    }}
}}
""")
