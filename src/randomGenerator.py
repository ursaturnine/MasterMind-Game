import src.constant as constant
import requests

def generateNumber():
    query = {'num': constant.LENGTH_OF_ANSWER, 'min': constant.MIN_VALUE , 'max': constant.MAX_VALUE, 'col': constant.NUM_OF_COLUMNS, 'base': constant.BASE_SYSTEM, 'format': constant.RESPONSE_FORMAT, 'rnd': constant.RANDOMIZATION}
    response = requests.get("https://www.random.org/integers", params=query)

    # parse & reformat
    textFormat = response.text
    strFormat = "".join(textFormat.split())


    return strFormat