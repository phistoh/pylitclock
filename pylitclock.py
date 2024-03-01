from datetime import datetime
import csv
import random
import os
import textwrap

def get_current_quote():
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    suitable_quotes = []

    # quotes from https://github.com/lbngoc/literature-clock/blob/master/litclock_annotated.csv
    with open('quotes.csv', newline='', encoding='utf-8') as csvfile:
        quote_reader = csv.DictReader(csvfile, fieldnames=['time','time_string','quote','title','author','sfw'], delimiter='|')
        for row in quote_reader:
            if row['time'] == current_time:
                time_string = row['time_string']
                quote_with_color = row['quote'].replace(time_string, '\033[33m{}\033[0m'.format(time_string))
                quote_with_color = textwrap.fill(quote_with_color.replace('<br/>','\n'), width=72, initial_indent=' ' * 4, subsequent_indent=' ' * 4)
                caption = ('- {t}, {a}'.format(q = quote_with_color, t = row['title'], a = row['author'])).rjust(68)
                suitable_quote = '\n{q}\n\n{c}'.format(q = quote_with_color, c = caption)
                suitable_quotes.append(suitable_quote)

    quote = ''
    if len(suitable_quotes) != 0:
        quote = random.choice(suitable_quotes)

    return quote

if __name__ == "__main__":
    os.system('')
    print(get_current_quote())