from datetime import datetime
import random
import os
import textwrap
import json

def random_ansi_color(str):
    random.seed(str)
    c_1 = random.randrange(0, 100)
    c_2 = random.randrange(100, 255)
    c_3 = random.randrange(0, 255)
    C = [c_1, c_2, c_3]
    random.shuffle(C)
    r,g,b = C
    ansi_color = '\033[38;2;{R};{G};{B}m'.format(R = r, B = b, G = g)
    
    colored_string = ansi_color + str + '\033[0m'
    return colored_string

def get_quote_from_file():
    # json files from https://github.com/JohannesNE/literature-clock
    now = datetime.now()
    current_time = now.strftime('%H_%M.json')
    dirname = os.path.dirname(__file__)
    quotes_file = os.path.join(dirname, 'quotes', current_time)
    annotated_quote = {}
    if os.path.isfile(quotes_file):
        with open(quotes_file, encoding="utf8") as quote_json:
            annotated_quote = json.load(quote_json)[0]
    else:
        annotated_quote['quote_first'] = '“What time is it?’\n‘'
        annotated_quote['quote_time_case'] = 'Whatever time you want it to be'
        annotated_quote['quote_last'] = (',’ she gave him a cheeky wink. ‘Now be honest, did you ask for free will?’\n'
        '‘How did you—?’\n'
        'Amanita joined Mario beneath the covers. The ethereal Threads tethering her wrists phased through the thick wool blankets like sunlight through a windowpane.\n'
        '‘The bird that acknowledges its cage only ever sings of freedom,’ she said dreamily.”')
        annotated_quote['author'] = 'Louise Blackwick'
        annotated_quote['title'] = 'The Underworld Rhapsody'
        annotated_quote['time'] = None
        
    return annotated_quote

def format_quote(annotated_quote):
    formatted_quote = annotated_quote.get('quote_first', '')
    
    # color time in quote
    if annotated_quote.get('quote_time_case', None) is not None:
        time_string = annotated_quote.get('quote_time_case', None)
        formatted_quote = formatted_quote + '{t}'.format(t = random_ansi_color(time_string))
    if annotated_quote.get('quote_last', None) is not None:
        time_string = annotated_quote.get('quote_last', None)
        formatted_quote = formatted_quote + annotated_quote.get('quote_last', None)
    formatted_quote = formatted_quote.replace('<br/>', '\n')
    
    # limit line lengths and keep existing new lines
    formatted_quote_lines = formatted_quote.splitlines()
    formatted_quote = "\n".join([
        textwrap.fill(l, width=72, initial_indent=' ' * 4, subsequent_indent=' ' * 4, replace_whitespace=False) for l in formatted_quote_lines
    ])
    
    # generate caption
    if annotated_quote.get('title', None) is not None:
        caption = ('- \033[3m{t}\033[23m, {a}'.format(t = annotated_quote.get('title', ''), a = annotated_quote.get('author', ''))).rjust(68)
    else:
        caption = ('- {a}'.format(a = annotated_quote.get('author', 'Unknown'))).rjust(68)
    formatted_quote = '\n{q}\n\n{c}'.format(q = formatted_quote, c = caption)
    
    return formatted_quote

if __name__ == "__main__":
    os.system('')
    quote = get_quote_from_file()
    print(format_quote(quote))