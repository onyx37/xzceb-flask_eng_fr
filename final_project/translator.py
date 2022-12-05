import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Function to translate english text into french

def englishToFrench(englishText):
    #write the code here
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3
    authenticator=authenticator

    language_translator.set_service_url(url)

    frenchText = language_translator.identify('Language translator translates text from one language to another').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    return englishText

englishToFrench("hello")
