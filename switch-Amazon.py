import requests, re, time
from bs4 import BeautifulSoup
import smtplib
from Config import EMAIL_ADDRESS, EMAIL_PASSWORD, HEADERS, SW_URL


def trackPrice():
      price = float(re.sub(r"[^\d.]", "", getPrice()))
      if price > WANTED_PRICE:
          print("It's still too expensive.")
          pass
      else: 
            print("Cheaper!")
            # sendEmail()

def getAvailability():
      page = requests.get(SW_URL, headers=HEADERS)
      soup = BeautifulSoup(page.content, features='lxml')
      try:
            title = soup.select("#productTitle")[0].get_text().strip() #soup.find(id='productTitle').get_text().strip()
      except:
            title = 'N/A'
            pass
      else: 
            try:
                  availability = soup.find(id='availability').get_text().strip()
            except:
                  print('Product is not available.')
                  pass
            else:
                  try:
                        price = soup.find(id=['priceblock_ourprice', 'priceblock_dealprice']).get_text().strip()[1:] 
                  except:
                        price = 'N/A'
                        print('Price is not available.')
                  else:
                        sendEmail()



      print(price)
      return price

def sendEmail():
      server = smtplib.SMTP(host='smtp.gmail.com', port=587)
      server.ehlo()
      server.starttls()
      server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

      subject = 'But switch now!'
      body = f"Click the link: {URL}"
      mailtext = f"Subject: {subject} \n\n {body}"

      server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
      print('Sent Email!')

      server.quit()
      pass


if __name__ == "__main__":
      while True:
            print("Tracking....") 
            getAvailability()
            time.sleep(3600)
 

