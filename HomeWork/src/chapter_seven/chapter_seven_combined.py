# 7.1.1: Slice a rhyme.
#
start_index = 4
end_index = 7
rhyme_lyric = 'The cow jumped over the moon.'
sub_lyric = rhyme_lyric[start_index:end_index]
print(sub_lyric)
# 7.2.1: Format temperature output.
#
air_temperature = 36.4158102
print("%.1f" % air_temperature + "C")

# 7.3.1: Find abbreviation.
#
user_tweet = 'I was LOL during the whole movie!'

if "LOL" in user_tweet:
    print('LOL means laughing out loud.')
else:
    print('No abbreviation.')
# 7.3.2: Replace abbreviation.
#
user_tweet = 'Gotta go. I will TTYL.'
decoded_tweet = user_tweet.replace('TTYL', 'talk to you later')

print(decoded_tweet)
# 7.4.1: Extract area code.
#
phone_number = '977-555-3221'
number_segments = phone_number.split("-")
area_code = number_segments[0]
print('Area code:', area_code)
