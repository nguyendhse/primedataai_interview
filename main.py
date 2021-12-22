from string_tokenize import Tokenizer


def format_string(template: str, parameters: dict):
    keys = parameters.keys()
    for key in keys:
        template = template.replace('{' + key + '}', parameters[key])

    return template


if __name__ == '__main__':
    template = 'Hi {name}, welcome to {company}!.'
    params = {"name": "Nguyen", "company": "PrimeData"}

    output = Tokenizer().format_string(template, params)

    print(output)
