import requests
from bs4 import BeautifulSoup
import time
import smtplib
import smtplib
from Config import EMAIL_ADDRESS, EMAIL_PASSWORD, HEADERS, URL, WANTED_PRICE


def trackPrice():
      price = float(getPrice())
      if price > WANTED_PRICE:
          print("It's still too expensive.")
          pass
      else: 
            print("Cheaper!")
            sendEmail()

def getPrice():
      page = requests.get(URL, headers=HEADERS)
      soup = BeautifulSoup(page.content, features='lxml')
      title = soup.select("#productTitle")[0].get_text().strip() #soup.find(id='productTitle').get_text().strip()
      price = soup.find(id='priceblock_ourprice').get_text().strip()[1:]
      availability = soup.find(id='availability').get_text().strip()
      review_count = int(soup.select("#acrCustomerReviewText")[0].get_text().split()[0])
      return price

def sendEmail():
      server = smtplib.SMTP(host='smtp.gmail.com', port=587)
      server.ehlo()
      server.starttls()
      server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

      subject = 'Amazon Price Has Dropped!'
      body = f"Click the link: {URL}"
      mailtext = f"Subject: {subject} \n\n {body}"

      server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
      print('Sent Email!')

      server.quit()
      pass


if __name__ == "__main__":
      while True:
            trackPrice()
            time.sleep(3600)
 

