from django.core.mail import EmailMessage
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Submit the Google Form and send a confirmation email'

    def handle(self, *args, **kwargs):

        self.take_screenshot('https://forms.gle/WT68aV5UnPajeoSc8')
        self.send_email()


    def take_screenshot(self,url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  
        options.add_argument('--disable-gpu')  
        options.add_argument('--no-sandbox')  
        options.add_argument('--disable-dev-shm-usage')  

        
        driver = webdriver.Chrome('D:\chromedriver-win64\chromedriver-win64\chromedriver.exe', options=options)


        driver.get(url)
        time.sleep(5)
        
        fields = driver.find_elements(By.CLASS_NAME,'zHQkBf')
        fields[0].send_keys('Sam Fredrick')
        fields[1].send_keys('6383536529')
        fields[2].send_keys('samfredrick273@gmail.com')
        
        driver.find_element(By.CLASS_NAME,'tL9Q4c').send_keys('P-42/1, Ahamed colony, Ramalinga Nagar, Woraiyur, Trichy, Tamil Nadu')
        fields[3].send_keys('620003')
        
        fields[4].send_keys('12042004')
        fields[5].send_keys('Male')
        key = driver.find_elements(By.CLASS_NAME, 'M7eMe')
        code = str(key[7].text).split()[-1]
        
        fields[6].send_keys(code)
        
        submit_button = driver.find_element(By.CLASS_NAME, 'RveJvd')
        print(submit_button.text)
        submit_button.click()
        time.sleep(5)
        driver.save_screenshot("confirmation_screenshot.png")
        print('Screenshot saved ')

        driver.quit()

    def send_email(self):
        subject = 'Python (Selenium) Assignment - Sam Fredrick'
        body = 'Please find the attached confirmation screenshot.'
        from_email = settings.EMAIL_HOST_USER

        to_emails = ['tech@themedius.ai']
        cc_emails = ['hr@themedius.ai']
        screenshot_path = 'confirmation_screenshot.png'

        email = EmailMessage(
            subject,
            body,
            from_email,
            to_emails,
            cc=cc_emails,
        )
        email.attach_file(screenshot_path)
        email.send()