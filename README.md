# Arbitrage Betting Application

This application helps identify arbitrage betting opportunities across different bookmakers. Arbitrage betting (also known as sure bets or miracle bets) is a technique where you place bets on all possible outcomes of an event at odds that guarantee a profit regardless of the result.

## Features

- Fetches odds from multiple bookmakers via APIs
- Calculates arbitrage opportunities automatically
- Displays potential profit percentages
- User-friendly web interface
- Real-time updates

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your API keys in a `.env` file (see `.env.example`)
4. Run the application:
   ```
   python src/app.py
   ```

## Usage

1. Navigate to `http://localhost:5000` in your web browser
2. Select sports and markets you're interested in
3. View identified arbitrage opportunities
4. Use the calculator to determine optimal stake distribution

## Technologies Used

- Python
- Flask (Web Framework)
- Requests (API calls)
- BeautifulSoup (Web scraping)
- Pandas (Data manipulation)

## License

MIT

## Disclaimer

This application is for educational purposes only. Be aware that many bookmakers prohibit arbitrage betting and may limit or close accounts that engage in this practice. Always check the terms and conditions of bookmakers before placing bets. 