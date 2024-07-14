# Selenium-Django Form Submission

## Overview

This project automates the submission of a Google Form using Selenium and sends a confirmation screenshot via email using Django. It demonstrates proficiency in web automation, web scraping, and Django's email functionality.

## Prerequisites

1. Python 3.x
2. Django
3. Selenium
4. ChromeDriver

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/fredrick273/form_submission.git
    cd form_submission
    ```

2. **Install the required packages:**
    ```bash
    pip install django selenium python-dotenv
    ```

3. **Download ChromeDriver:**
    Download the appropriate version of ChromeDriver for your system from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable) and update the path in `send_email.py` if necessary.

## Usage

1. **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

2. **Run the management command to submit the form and send the email:**
    ```bash
    python manage.py send_email
    ```

## Notes

- The Google Form URL used in this script is `https://forms.gle/WT68aV5UnPajeoSc8`. If the form fields change, you might need to update the script accordingly.
- Ensure that the `chromedriver.exe` path in the script is correct.
