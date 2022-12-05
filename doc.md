# Documentation

Documentation about using the library for text translation - Translated



# Classes

### Translated

   The main class of the library, which contains all its functions.

   **Import**
```python
from translated.translated import Translated
```

   **Class functions**

    translate
    languages
    
# Functions

### translate

   Function of text translation
   
   **text**
   
    Text which will be translated.
    
   **from_lang**

    Language code of language from which will be completed translate
    
   **to_lang**

    Language code of language for which will be completed translate
    
   **exceptions**
   
    List with words which don't will be translated
    
   **slash_space**
   
     The presence of auto-spaces in slashes
     
     True - leave spaces;
     False - remove spaces.
    
   ### Example
   
```python
from translated.translated import Translated
    
translated = Translated()
    
print( translated.translate(text='This feature is very cool and very useful', from_lang='en', to_lang='ru', exceptions=['very']) ) 
# 'Эта функция very крутая и very полезная'
```

    
### languages

   Function which returns dict with languages and their languages codes.
   
   **Does not accept arguments**
   
   ### Example
   
```python
from translated.translated import Translated
    
translated = Translated()
    
print( translated.languages() ) # {'Русский': 'ru', 'English': 'en', ...}
```
   
   
  

    
    
