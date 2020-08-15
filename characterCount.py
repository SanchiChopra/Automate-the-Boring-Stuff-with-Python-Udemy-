# Count the Number of Characters in a Given String
#myDic = {'key1':'value1', 'key2':'value2','key3':'value3'}
# myDic.get('key2',0)   (if this key exists in dic, return its value else return 0)


import pprint
message = ''' Nature is that natural and physical world that surrounds us and makes life possible on earth.
 Nature is the heart of the earth . Nature heals us . We have a strong bond and emotional connection with nature. 
 The serenity of nature calms our heart. the stillness and movement in nature both have a hypnotizing effect. 
 The unfolding creativity of nature is an art. 
 The practice of devoting ourselves to the bliss of nature is soothing and reviving. 
 Everyone loves to escape away in the mysteries of nature . Nature is an god's gift.
'''
count = {}

for characters in message:
    count.setdefault(characters, 0)  # set a value if the key doesn't exist
    count[characters] = count[characters] + 1
# OR print(pprint.pformat(count)) if we want the output as a string
pprint.pprint(count)
