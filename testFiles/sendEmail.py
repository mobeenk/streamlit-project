import smtplib
conn =smtplib.SMTP('smtp-mail.outlook.com',587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('mobeen-k@hotmail.com','WhatId0ntkn0w?')
conn.sendmail('mobeen-k@hotmail.com','moubien.kayali@gmail.com','Subject:')
conn.quit()