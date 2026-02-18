from django import template
register = template.Library()



@register.filter()
def censor(text, bad_words):
   if not isinstance(text , str):
      raise ValueError ('Должно быть строкой!!!!!!!!')

   for word in bad_words:
      censored_word = word[0] + '*' * (len(word) - 1)
      text = text.replace(word, censored_word)

   return text

