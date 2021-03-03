def search4vowels(word:str):
    
    '''Return a boolean based on any vowels found'''
    vowle = set('aeiou')
    return vowle.intersection(set(word))
    '''결과값으로 셋이 나올수도 있어요!!!'''

search4vowels('hitch-hiker')

search4vowels('galaxy')

search4vowels('life, the universe and everything')

search4vowels('sky')

l = list()
l

d = dict()
d

t = tuple()
t