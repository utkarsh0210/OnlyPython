from instabot import Bot
bot=Bot()
bot.login(username="",password="")
inp = input("Enter the Username : ")
bot.follow(inp)
bot.upload_photo()
bot.unfollow()
bot.send_message("heyy !!!",[])
followers = bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("username")
for Following in following:
    print(bot.get_user_info(Following))
