def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    '''2번째 함수가 없으면 기본 값 'aeiou'에서 찾아라'''
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

search4letters('hitch-hiker')

search4letters('galaxy', 'xyz')
search4letters(phrase = 'galaxy', letters = 'xyz')
search4letters(letters = 'xyz', phrase = 'galaxy')

search4letters('life, the universe, abd everything', 'o')

import random
random.randint(0, 255)