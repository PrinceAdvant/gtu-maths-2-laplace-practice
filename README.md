# GTU Maths 2 Laplace IVP Practice (3110015)

"Solve the IVP using Laplace transform" is a 7 marker that sat in **all 9** official GTU Mathematics-2 (3110015) papers we counted, Summer 2022 to Summer 2026. Unit 2 (Laplace) is 7 hours and 20% in the official syllabus. Ratta mat maar, method pakad.

This repo has:

- 4 practice IVPs with worked steps (below)
- `laplace_ivp_check.py`, a sympy script that solves each one the Laplace way and plugs the answer back into the equation
- `test_laplace_ivp_check.py`, unit tests for the script

> **The 4 practice IVPs are my own. They are NOT copied from GTU papers.** They are written in the same style so you can practise the method.

## The method in 4 lines

1. Transform both sides: L{y'} = sY - y(0), L{y''} = s²Y - s·y(0) - y'(0)
2. Collect Y(s) on one side and solve for it
3. Split Y(s) with partial fractions
4. Take the inverse transform, then put t = 0 into y(t) and y'(t) to check the initial conditions

## Practice set with worked steps

### 1. y'' + 4y = 0, y(0) = 1, y'(0) = 2

s²Y - s - 2 + 4Y = 0, so Y = (s + 2)/(s² + 4) = s/(s² + 4) + 2/(s² + 4).

**y = cos 2t + sin 2t**

### 2. y'' - 3y' + 2y = e^(3t), y(0) = 0, y'(0) = 0

(s² - 3s + 2)Y = 1/(s - 3), so Y = 1/((s - 1)(s - 2)(s - 3)) = (1/2)/(s - 1) - 1/(s - 2) + (1/2)/(s - 3).

**y = e^t/2 - e^(2t) + e^(3t)/2**

### 3. y'' + 2y' + 5y = 0, y(0) = 1, y'(0) = -1

s²Y - s + 1 + 2(sY - 1) + 5Y = 0, so Y = (s + 1)/((s + 1)² + 4). The first shifting theorem does the rest.

**y = e^(-t) cos 2t**

### 4. y'' + y = t, y(0) = 0, y'(0) = 2

s²Y - 2 + Y = 1/s², so Y = (2s² + 1)/(s²(s² + 1)) = 1/s² + 1/(s² + 1).

**y = t + sin t**

## Run the checker

```bash
pip install -r requirements.txt
python laplace_ivp_check.py          # prints Y(s), y(t) and ALL OK
python -m unittest -v                # 2 tests
```

Tested with Python 3 and sympy 1.14. sympy may print an equivalent form (for example sqrt(2)·sin(2t + π/4) for sum 1); the script checks it equals the expected answer.

Use it to check your own working, not to replace it. If the question says "using Laplace transform", GTU expects that method.

## Galti mat karna

- Forgetting the -s·y(0) - y'(0) terms. Most wrong answers start here.
- Using a shortcut when the question asks for Laplace. Method marks jaayenge.
- Skipping the check. Put t = 0 into your answer, 30 seconds ka kaam.

## Repeated topics in real 3110015 papers

Counted from 9 official GTU papers (S2022, W2022, S2023, W2023, S2024, W2024, S2025, W2025, S2026). A topic counts once per paper if it appears anywhere, compulsory or OR.

**Laplace (Unit 2)**

| Topic | Papers (out of 9) | Usual marks |
|---|---|---|
| Solve an IVP using Laplace transform | 9/9 | 7 |
| Laplace transform of f(t)/t | 7/9 (all except W2022, S2026) | 3 or 4 |
| Convolution theorem | 7/9 (all except W2023, S2025) | 3 to 7 |
| Second shifting theorem or unit step | 6/9 (S2022, W2022, S2023, S2024, W2024, S2026) | 3 or 4 |

**Other 9/9 topics:** Green's theorem (Q.1(c) in 8 of 9), div/curl/solenoidal/irrotational check, Fourier integral, variation of parameters, undetermined coefficients, Euler-Cauchy, equations not of first degree (p, Clairaut), power series solution.

### Same sum, different session (from the real papers)

These exact questions appeared in two different sessions:

| Question | Sessions |
|---|---|
| y'' - 2y' + 5y = 5x³ - 6x² + 6x, undetermined coefficients | S2024 Q.4(c) OR, W2025 Q.2(c) |
| y'' + y = sin x, variation of parameters | W2022 Q.4(c) OR, S2024 Q.4(c) |
| Power series solution of y'' + xy = 0 | W2022 Q.5(c), S2025 Q.2(c) |
| Series solution of (1 + x²)y'' + xy' - 9y = 0 | S2024 Q.3(c) OR, W2024 Q.4(c) OR |
| Series solution of 4xy'' + 2y' + y = 0 | W2022 Q.5(c) OR, S2024 Q.5(c) |
| Solve ye^x dx + (2y + e^x) dy = 0 | W2024 Q.1(b), S2025 Q.2(a) |
| Solve x²p² + xyp - 6y² = 0 | W2025 Q.4(a) OR, S2026 Q.4(b) |
| Fourier cosine integral of e^(-kx) | S2022 Q.2(b), S2024 Q.2(b) |
| Fourier cosine integral of (π/2)e^(-x) | W2022 Q.2(b), W2025 Q.3(c) OR |
| F = 2xyz i + (x²z + 2y) j + x²y k: conservative, find potential | W2022 Q.2(c) OR, S2026 Q.1(b) |
| Prove Rodrigues' formula for Pₙ(x) | S2023 Q.2(c) OR, S2026 Q.2(c) |

Past repetition is a pattern, not a promise. Use it to set priorities, not to skip the syllabus.

Full repeat table, exam pattern and study plan (GTU Hero is my project): <https://gtuhero.com/blogs/gtu-maths-2-papers-pyqs-repeated-sums>

## Official papers

gtu.ac.in/Download1.aspx: pick the session (S = Summer, W = Winter), pick BE, search 3110015, open the PDF.

Not affiliated with Gujarat Technological University. MIT licensed.
