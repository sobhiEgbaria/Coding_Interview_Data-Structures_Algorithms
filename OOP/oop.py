# class StarCookies:
#   def __init__(self,color,price) -> None:
#     self.color = color
#     self.price = price

# starCookie1 = StarCookies("red",21)
# print(starCookie1.color, starCookie1.price)

class Youtube:
  def __init__(self,username,subscribe = 0) -> None:
    self.username = username
    self.subscribe = subscribe

  def subscription(self):
    self.subscribe += 1




user1 = Youtube("sobhi")
user1.subscription()
user1.subscription()

user2 = Youtube("sobhi",9)
print(user1.username,user1.subscribe)
print(user2.username,user2.subscribe)
    
