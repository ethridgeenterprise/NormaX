# NormaX

**A Behavior-Aware Statistical Model for the Real World**

NormaX is a modern twist on the classic normal distribution, designed to account for real-world behaviors such as incentive shifts and irrational decisions. It adds two additional layers to the Gaussian curve: one for external motivation, and another for nonlinear behavioral response.

## Why NormaX?

Traditional models assume symmetry and rationality. Real life doesn’t.

NormaX adapts to:

- Incentive-driven decision-making
- Psychological extremes (fear, urgency, desire)
- Irregular behavior at price or performance thresholds
- Outliers that actually *matter*

## Core Equation

```
F(x) = (1 / (σ√(2π))) * e^(-(x - μ)^2 / (2σ^2)) + α(x - x₀) + β * tanh(γ(x - μ))
```

## Features

- Built on the normal distribution
- Modifiable for any real-world scenario
- Tunable with just four behavior-aware parameters
- Lightweight and easy to implement in Python or R

## Example Use Case: Customer Purchase Behavior

Modeling how customers react near a pricing threshold, NormaX shows increased buying below $50 and a steep drop above $60, capturing market behavior the normal curve misses.

![NormaX Curve](assets/NormaX_Equation_Logo.png)

## Files

- `normax_model.py` – Core function
- `sample_data.csv` – Sample data
- `whitepaper/` – PDF + TXT white paper
- `notebooks/` – Jupyter notebook demo
- `assets/` – Logos and visuals

## License

MIT License – free to use and modify with credit.

---

Want to help us bend the curve of statistical modeling? **Star, fork, or try NormaX in your own projects.**
