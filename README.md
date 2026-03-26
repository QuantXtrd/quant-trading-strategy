# Quant Trading Strategy (Python)

## Overview
This project implements a basic quantitative trading strategy using moving averages. It simulates buy and sell decisions based on price trends and calculates total profit.

## Strategy Logic
- A short-term moving average is compared to a long-term moving average
- When the short-term average crosses above the long-term average, the script generates a BUY signal
- When the short-term average crosses below the long-term average, the script generates a SELL signal

## Features
- Buy/sell signal generation
- Trade simulation
- Profit calculation
- Simple backtesting on sample price data

## Technologies Used
- Python

## How to Run
```bash
python trading_strategy.py
