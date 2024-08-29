letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "shahid").replace("<|Date|>", "24 september"))
# relace chaining is possible one after another