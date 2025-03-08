# Automated-email-marketing-using-generative-AI

## Overview
This project automates email marketing campaigns using Cohere's AI-powered text generation to create personalized promotional emails. It reads recipient data from a CSV file, generates customized email content, and sends emails using SMTP.

## Features
- **AI-Generated Emails**: Uses Cohere's AI to craft personalized promotional emails.
- **Automated Email Sending**: Sends emails via SMTP (Gmail used in this example).
- **CSV-based Recipient Management**: Reads customer details (name, email, product) from a CSV file.

## Dependencies
Ensure you have the following Python libraries installed:

```bash
pip install cohere smtplib csv
```

## Setup
1. **Cohere API Key**: Replace `'my_api_key'` with your actual Cohere API key.
2. **Email Credentials**: Update `'my_email'` and `'my_password'` with your SMTP email credentials.
3. **Recipient Data**: Prepare a `recipients.csv` file with the following format:

```csv
Name,Email,Product
John Doe,john@example.com,Smartphone
Jane Smith,jane@example.com,Headphones
```

## Running the Script
Execute the script using Python:

```bash
py generated-automated-email.py
```

## How It Works
1. **Load Recipients**: Reads the `recipients.csv` file.
2. **Generate Email Content**: Uses Cohere's AI to generate a personalized email.
3. **Send Emails**: Connects to Gmail SMTP and sends the generated emails.
4. **Error Handling**: Skips recipients if content generation fails.

## Author
Alisher Aldamzharov

