if __name__ == "__main__":
    alien0 = {"color":"green","points":5}
    alien1 = {"color":"yellow","points":10}
    alien2 = {"color":"red","points":8}

    #字典的嵌套
    aliens = [alien0,alien1,alien2]
    print(aliens)

    for alien in aliens:
        print(alien)

    #把集合放进字典
    pizza = {
        "crust":"thick",
        "topping":["mushrooms","extra cheese"]
    }

    print(pizza)
    for topping in pizza["topping"]:
        print(topping)


    #字典中嵌套字典
    users = {
        "aeinstein":{
            "fisrt":"albert",
            "last":"einstein",
            "location":"priceton"
        },

        "mcruie":{
            "fisrt":"marie",
            "last":"curie",
            "location":"paris"
        }
    }

    for username,userinfo in users.items():
        #print("username:"+ username)
        print("fullname:"+ (userinfo["fisrt"] + " " + userinfo["last"]))