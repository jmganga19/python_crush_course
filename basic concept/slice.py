# slice is the specific group of items in a list.
# Python stops one item before the second index you specify
# to work(generate a slice you specify the index of) first and last element you wants

players = ['mbape','neymar','kimpembe','messi','buffon']
print(players[0:1])

print(players[0:2])
print(players[1:3])
print(players[2:4])

message = 'Here are first three players in my team:'
print(message) 

for player  in players[0:3]:
    print(player.title())


# copy a list

movie = ['Die Hard','Fast X','Warrior 10','John Wick']
friend_movies = movie[:]
print(friend_movies)