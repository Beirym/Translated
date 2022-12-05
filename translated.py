from googletrans import Translator
import re


class Translated():

    def __init__(self):
        self.translating = Translator().translate

    def translate(self, text: str, from_lang: str, to_lang: str, exceptions=None, slash_space=True) -> str:
        '''translating - function for texts translation.

        :: text - the text which will be translated;
        :: from_lang* - the language from which the translation will be made;
        :: to_lang* - the language to be translated into;
        :: exceptions - list of word which don't will be translated;
        :: slash_space - availability spaces after slashes ( True - to leave / False - remove ).

        * - The language is specified as lang_code ( for get land_codes use - Translating.languages ).'''

        if from_lang != to_lang:

            if exceptions == None or len(exceptions) == 0:
                translation = self.translating(text, src=from_lang, dest=to_lang).text  # translation process

            else:
                # Create exceptions which don't will be translated

                initial, temp = re.compile(f'{exceptions}'), re.compile(r'__(\d+)__')  # replace exception words to not-translates-chars

                variables_list = []

                def replace(matchobj):
                    variables_list.append(matchobj.group())
                    return "__%d__" % (len(variables_list) - 1)

                def restore(matchobj):
                    return variables_list[int(matchobj.group(1))]

                # /. Create exceptions which don't will be translated

                # Translation process

                text = initial.sub(replace, text)
                translation = self.translating(text, src=from_lang, dest=to_lang).text
                translation = temp.sub(restore, translation)

                # /. Translation process

            if slash_space == False:
                if '/ ' in translation:
                    # replace auto-space after slashes
                    return translation.replace('/ ', '/')

            else:
                return translation

        else:
            return text

    def languages(self):
        '''languages - this is a function that returns a list of languages available for translation.'''

        lang_codes = {
            "Русский": "ru",
            "English": "en",
            "Français": "fr",
            "Український": "uk",
            "Deutsch": "de",
            "Italiano": "it",
            "Polski": "pl",
            "Беларускі": "be",
            "Català": "ca",
            "Nederlands": "nl",
            "한국어": "ko",
            "Español": "es",
            "Melayu": "ms",
            "Português": "pt",
            "Türkçe": "tr",
        }

        return lang_codes