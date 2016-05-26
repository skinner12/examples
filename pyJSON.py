from osconfeed import osconfeed

osconfeed1 = osconfeed()

print(osconfeed1.ultimeName('http://www.oreilly.com/pub/sc/osconfeed', 'data/osconfeed.json'))
print(osconfeed1.getCount('http://www.oreilly.com/pub/sc/osconfeed', 'data/osconfeed.json'))