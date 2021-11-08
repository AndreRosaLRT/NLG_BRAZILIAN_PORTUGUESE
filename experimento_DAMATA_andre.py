# from nlg.train import parse
# import nlg.ordering as ordering
# import nlg.structuring as structuring
# import nlg.lexicalization as lexicalization
# import nlg.reference as reference
#
# from nlg.generation import Generation
# from nlg.realization import Realization
# from inpe_deter.content import content
# from datetime import datetime
#
# from db.model import DeforestationDeterINPE, CoronaVirus
# #
#
# # from googletrans import Translator
#
# structuring_path = 'inpe_deter/data/pt-br/month_grammar/structuring.json'
# lexicalization_path = 'inpe_deter/data/pt-br/month_grammar/lexicalization.json'
# reference_path = 'inpe_deter/data/pt-br/month_grammar/references.json'
# lexicon_path = 'nlg/lexicons/pt-br'
# gen = Generation(structuring_path, lexicalization_path, reference_path, lexicon_path)
#
# visited = []

for date in DeforestationDeterINPE.objects().distinct('date'):
    # month, year = date.month, date.year
    year = 2020
    for month in range(3, 7):
        if (month, year) not in visited:
            visited.append((month, year))
            messages, date = content(month, year)
            try:
                entry, template, paragraphs = gen.generate(messages, strategy='random')

                text = []
                for p in paragraphs:
                    text.append(' '.join(p))
                text = '\n\n'.join(text)

                # print("Portuguese:")
                print(text)
                print()

            except:
                print('ERROR')
            print(10 * '*', '\n')
