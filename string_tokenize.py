import re
from collections import namedtuple


class Tokenizer:
    Token = namedtuple('Token', 'name text span')
    TOKENS = [
        ('NUMBER', r'\d+'),
        ('SYMBOL', r'[!@#$%^&*()-=+;\'\"]{1}'),
        ('WHITESPACE', r'\s+'),
        ('NORMAL_WORD', r'[A-Za-z0-9]+'),
        ('KEY_WORD', r'\{(.*?)\}'),
    ]

    def __init__(self, tokens=None):
        if not tokens:
            self.tokens = self.TOKENS
        else:
            self.tokens = tokens
        pat_list = []
        for tok, pat in self.tokens:
            pat_list.append('(?P<%s>%s)' % (tok, pat))
        self.re = re.compile('|'.join(pat_list))

    def iter_tokens(self, input, ignore_ws=True):
        for match in self.re.finditer(input):
            if ignore_ws and match.lastgroup == 'WHITESPACE':
                continue
            yield Tokenizer.Token(match.lastgroup, match.group(0), match.span(0))

    def tokenize(self, input, ignore_ws=True):
        return list(self.iter_tokens(input, ignore_ws))

    def format_string(self, template, params: dict):
        output = []
        max_kw = len(params.keys()) + 1
        match_times = 0
        for t in Tokenizer(self.TOKENS).iter_tokens(template, ignore_ws=False):
            if t.name == 'KEY_WORD':
                # get keyword inside brackets
                kw_name = re.findall(r'\{(.*?)\}', t.text)[0]
                if kw_name not in params.keys():
                    # raise if params doesn't have such key
                    raise ValueError('Error keyword %s' % kw_name)
                # Enrich output
                output.append(params[kw_name])
                # Check if number of params equals inputted template's param
                if match_times < max_kw:
                    match_times = match_times + 1
                else:
                    raise ValueError('Insufficient number of params')

            else:
                output.append(t.text)
        return ''.join(output)

