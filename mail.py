import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail():
    #smtp
    smtpHost = "irvine.sakura.ne.jp"
    smtpPort = 587
    smtpUser = "abe@irvine.jp"
    smtpPasswd = "kqoWn4tZBsw4T_yT"

    #header
    mailFrom = "test@hoge.com"
    mailTo = "abe@irvinesystems.co.jp"
    text = "mailTestdesu"
    subject = "mailTest"

    #body
    msg = MIMEMultipart()
    msg["From"] = mailFrom
    msg["To"] = mailTo
    msg["Subject"] = subject
    msg.attach(MIMEText(text,"plain","utf-8"))
    
    try:
        smtpObj = smtplib.SMTP(smtpHost,smtpPort)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(smtpUser,smtpPasswd)
        smtpObj.sendmail(smtpUser,mailTo,msg.as_string())
        smtpObj.quit()
    except Exception as e:
        print(e)

def main():
    sendMail()


if __name__ == "__main__":
    main()