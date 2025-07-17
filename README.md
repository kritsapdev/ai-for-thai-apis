# AI for Thai API Gateway

This project demonstrates a two-tier API architecture using Python, Flask, and Docker Compose, leveraging AI for Thai services for text summarization and sentiment analysis.

- **API1 (Summarization & Orchestrator):** Receives user requests, calls AI for Thai Text Summarization, then forwards the summarized text to API2 for sentiment analysis, and finally returns a combined result to the user.
- **API2 (Sentiment Analysis):** Receives text from API1, calls AI for Thai Social Sensing (SSENSE) for sentiment analysis, and returns the result.

Both APIs log their activities to the console, visible via Docker logs.

## Project Structure