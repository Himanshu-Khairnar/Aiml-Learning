# Stock Price Prediction (Monte Carlo Simulation)

This project uses Monte Carlo simulations to predict future stock prices based on historical data. It models possible price paths using geometric Brownian motion.

## Features

- **Statistical Analysis**: Calculating Log Returns, Drift, and Variance from historical stock data.
- **Monte Carlo Simulation**: Running 1000 simulations to forecast stock prices for the next 30 days.
- **Visualization**: Plotting potential future price paths to understand possible outcomes.

## Observations

- **Uncertainty Modeling**: The simulations show a wide range of possible future prices, illustrating the inherent uncertainty and risk in stock market predictions.
- **Drift and Volatility**: The model incorporates both the expected return (drift) and the historical volatility, providing a probabilistic outlook rather than a single point prediction.

## Technologies Used

- **Python**
- **Pandas**: For data management.
- **NumPy**: For mathematical modeling and random number generation.
- **Matplotlib**: For visualizing simulation results.

## Files

- `StockPrediction.ipynb`: Simulation code and visualization.
- `stock_data.csv`: Historical input data.
- `monte_carlo_simulation.csv`: Output of the simulation runs.
