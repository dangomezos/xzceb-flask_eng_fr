""" translater """

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ Function that translate from english to french """
    text = english_text
    french_text = MyMemoryTranslator(source = 'english', target = 'french').translate(text)          
    return french_text        
def french_to_english(french_text):
    """ Function that translate from french to english """
    text = french_text
    english_text = MyMemoryTranslator(source = 'french', target = 'english').translate(text)
    return english_text
