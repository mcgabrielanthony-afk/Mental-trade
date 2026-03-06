# Mental Trade System

The Mental Trade System is a comprehensive solution designed for crypto and forex trading, integrating various analysis techniques and advanced machine learning models to optimize trading strategies. This README provides an overview of the system, its features, installation instructions, usage guidelines, architecture, and how it leverages technical and fundamental analysis.

## Features
- **Multi-Asset Trading**: Supports both cryptocurrency and forex markets.
- **Technical Analysis**: Utilizes standard indicators (e.g., RSI, MACD, Bollinger Bands) for market sentiment evaluation.
- **Fundamental Analysis**: Analyzes macroeconomic indicators and news events to inform trading decisions.
- **Machine Learning Models**: Employs supervised and unsupervised learning techniques to predict market trends.
- **User-Friendly Interface**: Intuitive dashboard for easy navigation and trading operations.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/mcgabrielanthony-afk/mental-trade.git
   cd mental-trade
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables**: Create a `.env` file and configure your API keys and other sensitive data.

## Usage
- **Starting the Application**:
   ```bash
   python app.py
   ```
- **Accessing the Interface**: Open your browser and go to `http://localhost:5000`.
- **Trading**: Use the dashboard to select assets, set parameters, and execute trades based on analytical insights.

## Architecture

The Mental Trade System is built on a modular architecture, ensuring scalability and maintainability:
- **Frontend**: User interface built with React.js, providing a seamless user experience.
- **Backend**: Python Flask server handling business logic and data processing.
- **Database**: PostgreSQL for storing user data and trade history.
- **Trading Engine**: Executes trades using algorithms based on analysis outputs.

## Technical Analysis Integration
The system incorporates various technical indicators to help traders make informed decisions. Key indicators include:
- **Relative Strength Index (RSI)**: Measures the speed and change of price movements to identify overbought or oversold conditions.
- **Moving Averages (MA)**: Calculates average price over a specific period to identify trends.
- **Bollinger Bands**: Indicates volatility and potential price breakouts.

## Fundamental Analysis Integration
Fundamental analysis is crucial for understanding the underlying value of assets. The Mental Trade System aggregates economic data such as:
- **Interest Rates**: Impact on currency strength.
- **GDP Growth Rates**: Indicators of economic health.
- **News Sentiment Analysis**: Utilizes Natural Language Processing to analyze news articles related to the markets.

## Machine Learning Models for Trading
Machine learning models in the Mental Trade System are designed to enhance predictive accuracy. Features include:
- **Supervised Learning**: Regression and classification models trained on historical pricing data.
- **Unsupervised Learning**: Clustering techniques to identify market patterns and anomalies.

## Conclusion
The Mental Trade System is a powerful tool for traders looking to leverage technical and fundamental analysis, along with machine learning, for optimal trading performance. Follow the installation and usage instructions to get started and enhance your trading strategies.