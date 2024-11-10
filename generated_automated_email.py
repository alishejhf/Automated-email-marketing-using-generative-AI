import cohere
import smtplib

# Initialize the Cohere client with your API key
co = cohere.Client('my_api_key')

sender = 'my_email' 
password = 'my_password'

def generate_email_content(recipient_name, product_name):
    try:
        prompt = (f"""Write a friendly email promoting {product_name} to {recipient_name} 
                     that is approximately 170 words long. Ensure the email has an introduction, 
                     a detailed middle section about the benefits of the product, and a clear conclusion inviting the recipient to respond or to contact for more information. 
                     The email must end with 'Looking forward to hearing from you! Best regards, Alisher Aldamzharov' and should not contain any additional text after this closing statement.
                     Do not include the subject in the body of the email.""")

        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=500  # Increase the max_tokens value to allow more space for content
        )

        email_body = response.generations[0].text.strip()

        # Ensure the email ends correctly and remove any content after the closing
        closing = "Looking forward to hearing from you! Best regards, [Your Name]"
        if closing in email_body:
            email_body = email_body.split(closing)[0] + closing

        return email_body
    except Exception as e:
        print(f"Error generating email content for {recipient_name}: {e}")
        return ""

def send_email(recipient_email, subject, body):
    message = f"""From: {sender}
To: {recipient_email}
Subject: {subject}

{body}
"""

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient_email, message.encode('utf-8'))
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Could not send email to {recipient_email}: {e}")
    finally:
        server.quit()

def main():
    name = 'Alisher Aldamzharov'
    email = 'alish19083@gmail.com'
    product = 'Dark Chocolate with Blueberries'
    subject = f"Special Offer for {product}"  # Updated subject
    email_content = generate_email_content(name, product)
    if email_content:
        send_email(email, subject, email_content)
    else:
        print(f"Skipping email to {name} due to content generation failure.")

main()
