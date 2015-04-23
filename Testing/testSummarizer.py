from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import sumy 
#from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers.czech import stem_word
from sumy.utils import get_stop_words
#from utils import load_resource
 


if __name__ == "__main__":
    #url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    #url="http://www.astm.org/Standards/D4231.htm"
    #parser = HtmlParser.from_url(url, Tokenizer("english"))
   	
    parser=PlaintextParser.from_string(,
            Tokenizer("english"))
    summarizer = LsaSummarizer(stem_word) # initation input
    summarizer.stop_words = get_stop_words("english") # configureate stop words 

    for sentence in summarizer(parser.document, 20):
        print(sentence)