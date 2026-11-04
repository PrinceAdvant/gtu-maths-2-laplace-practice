"""Check your Laplace-transform IVP answers (GTU Maths 2, 3110015 style).

Solves y'' + a y' + b y = f(t), y(0)=y0, y'(0)=y1 the Laplace way:
  s^2 Y - s y0 - y1 + a (s Y - y0) + b Y = F(s)
  => Y(s) = (F(s) + (s + a) y0 + y1) / (s^2 + a s + b)
then takes the inverse transform and plugs the answer back into the ODE.

Practice set below is my own (not copied from GTU papers).
Repeated sums and topic counts from real papers:
https://gtuhero.com/blogs/gtu-maths-2-papers-pyqs-repeated-sums (GTU Hero, my project)

Needs: pip install sympy
"""
import sympy as sp

t, s = sp.symbols("t s", positive=True)


def solve_ivp_laplace(a, b, f, y0, y1):
    F = sp.laplace_transform(f, t, s, noconds=True) if f != 0 else 0
    Y = sp.apart(sp.simplify((F + (s + a) * y0 + y1) / (s**2 + a * s + b)), s)
    y = sp.simplify(sp.inverse_laplace_transform(Y, s, t).subs(sp.Heaviside(t), 1))
    return Y, y


def check(a, b, f, y0, y1, y):
    ode = sp.simplify(sp.diff(y, t, 2) + a * sp.diff(y, t) + b * y - f)
    return ode == 0 and sp.simplify(y.subs(t, 0) - y0) == 0 and sp.simplify(sp.diff(y, t).subs(t, 0) - y1) == 0


PRACTICE = [
    # (label, a, b, f(t), y(0), y'(0), expected answer)
    ("y'' + 4y = 0, y(0)=1, y'(0)=2", 0, 4, 0, 1, 2, sp.cos(2 * t) + sp.sin(2 * t)),
    ("y'' - 3y' + 2y = e^(3t), y(0)=0, y'(0)=0", -3, 2, sp.exp(3 * t), 0, 0,
     sp.exp(t) / 2 - sp.exp(2 * t) + sp.exp(3 * t) / 2),
    ("y'' + 2y' + 5y = 0, y(0)=1, y'(0)=-1", 2, 5, 0, 1, -1, sp.exp(-t) * sp.cos(2 * t)),
    ("y'' + y = t, y(0)=0, y'(0)=2", 0, 1, t, 0, 2, t + sp.sin(t)),
]

if __name__ == "__main__":
    ok = True
    for label, a, b, f, y0, y1, expected in PRACTICE:
        Y, y = solve_ivp_laplace(a, b, f, y0, y1)
        good = sp.simplify(y - expected) == 0 and check(a, b, f, y0, y1, expected)
        ok &= good
        print(f"{label}\n  Y(s) = {Y}\n  y(t) = {sp.simplify(y)}\n  matches expected: {good}\n")
    print("ALL OK" if ok else "SOMETHING FAILED")
