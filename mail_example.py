import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('eoin.g08@gmail.com', 'ronejztdqhhdjdki')
conn.sendmail('eoin.g08@gmail.com', 'eoin.g08@gmail.com', 'Subject: Test python script\n\nDear Eoin,\nTesting python script\n\n-Eoin')
conn.quit()