def snake_to_camel(word):
    new_word = word.replace('_',' ')
    new_word = new_word.title()
    new_word = new_word.replace(' ','') 
    return new_word


word = snake_to_camel('prueba_texto')
print(word == 'PruebaTexto')
