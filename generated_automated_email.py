import openai
import smtplib

openai.api_key = 'my_api_key'

sender = 'my_email' 
password = 'my_password'

def generate_email_content(recipient_name, product_name):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",  "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Write a friendly email promoting {product_name} to {recipient_name}."}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
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
        server.sendmail(sender, recipient_email, message)
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Could not send email to {recipient_email}: {e}")
    finally:
        server.quit()

def main():
    name = 'Alisher Aldamzharov'
    email = 'alish19083@gmail.com'
    product = 'Dark Chocolate with Blueberries'
    email_content = generate_email_content(name, product)
    if email_content:  
        send_email(email, f"Special Offer for {product}", email_content)
    else: 
        print(f"Skipping email to {name} due to content generation failure.")

main()



# hi my hame is alisher and this is project made by shrrrrrrrrrrrrrrrrrrrt