import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('eoin.g08@gmail.com', 'ronejztdqhhdjdki')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search('SINCE 20-Jan-2018')
print(UIDs)

rawMessage = conn.fetch([14441], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[14441][b'BODY[]'])
print(message.get_subject())
print(message.text_part.get_payload().decode('UTF-8'))