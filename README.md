Federated Data Aggregator (FDA)
Project Title:
Federated Data Aggregator using OpenWeatherMap, NewsAPI, and Unsplash

Problem Statement
Modern applications rarely rely on a single data source. Instead, they interact with multiple external services through APIs to fetch, process, and present meaningful information. This open-ended lab focuses on building a Federated Data Aggregator (FDA) in Python that connects to multiple public APIs, aggregates their data, and presents a unified result.

 Project Objective
The objective of this project is to design and implement a Python-based application that:
⦁	Connects to multiple thirdparty public APIs
⦁	Aggregates and transforms the retrieved data
⦁	Demonstrates Object-Oriented Programming (OOP) principles
⦁	Uses secure configuration management for API keys
⦁	Implements robust error handling and logging

 Project Description
This FDA application fetches:
⦁	 Real-time weather information for a given city using OpenWeatherMap API
⦁	 Latest news headlines related to the city or general topic using NewsAPI
⦁	 A relevant high-quality image using Unsplash API
The data from these independent services is aggregated and displayed together, providing a single coherent output to the user.

 Technologies and Tools Used
⦁	Python 3.x
⦁	requests
⦁	python-dotenv
⦁	logging module
⦁	OpenWeatherMap API
⦁	NewsAPI
⦁	Unsplash API

Software Design (OOP)
The application follows Object-Oriented Design principles:
1. Abstract API Client
A base abstract class defines a common interface for all API clients.
2. Concrete API Clients
⦁	WeatherClient → Handles OpenWeatherMap API
⦁	NewsClient → Handles NewsAPI
⦁	ImageClient → Handles Unsplash API
Each client:
⦁	Encapsulates API keys and URLs
⦁	Handles its own request logic and error handling
3. Data Aggregator Class
The DataAggregator class:
⦁	Instantiates all API clients
⦁	Calls each service
⦁	Aggregates and formats the data into a unified output

Secure Configuration Management
⦁	API keys are stored in a .env file
⦁	Environment variables are loaded using python-dotenv
⦁	The .env file is excluded from version control using .gitignore
.env.example
OPENWEATHER_API_KEY=
NEWS_API_KEY=
UNSPLASH_ACCESS_KEY=

 Error Handling and Robustness
The project implements:
⦁	try...except blocks for API calls
⦁	Handling of:
oHTTP errors (401, 404, 429)
oNetwork errors (ConnectionError)
⦁	Validation of API response data to avoid runtime errors

Logging
The built-in Python logging module is used to:
⦁	Log successful API calls
⦁	Log errors with timestamps and detailed messages

Project Structure
Federated-Data-Aggregator/
│
├── api_clients/
│   ├── base_client.py
│   ├── weather_client.py
│   ├── news_client.py
│   └── image_client.py
│
├──  screenshots/
├    ├──output.jpeg
├    ├──output(1).jpeg
├── aggregator.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── venv/

.gitignore
.env
venv/
__pycache__/

Installation Instructions
1.Clone or extract the project folder
2.Create and activate a virtual environment
Windows
python -m venv venv
venv\Scripts\activate
3.Install dependencies
pip install -r requirements.txt

Run the Application
1.Create a .env file in the project root
2.Add your API keys:
OPENWEATHER_API_KEY=e83b82868bd7375c7ac1f9b27bee0176
NEWS_API_KEY=fd55248ad9554a5c990f8ca8fb5eed5b
UNSPLASH_ACCESS_KEY=d3FN508ZP9kMf1mJi_Nc8dZF0TgE1os26yywcWBOX8I
3.Run the application:
python main.py

Functional Features
⦁	Fetches live weather data
⦁	Retrieves latest news headlines
⦁	Displays a relevant image
⦁	Aggregates data from multiple APIs
⦁	Secure API key handling
⦁	Robust error handling and logging

Learning Outcomes
⦁	Practical experience with REST APIs
⦁	Understanding federated data systems
⦁	Applying OOP principles in Python
⦁	Secure handling of sensitive configuration
⦁	Writing maintainable and documented code

Author Information
Name: Manahil Shujah, Zainab Bibi, Sarosh Majeed
Course: Software Construction and Development
Instructor: Sir Shehzad
Institution: Fatima Jinnah Women University
Submission Date: 23-12-2025

Screenshots
![WhatsApp Image 2025-12-23 at 4 30 46 PM](https://github.com/user-attachments/assets/8995a1f1-b929-4b10-a88a-2c03814c7ab7)
![WhatsApp Image 2025-12-23 at 4 29 38 PM](https://github.com/user-attachments/assets/1edef294-ed54-4797-a8de-00b12860fc1a)

