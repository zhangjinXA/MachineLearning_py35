import itchat

class get_SeqID:

    def __init__(self):
        itchat.auto_login(hotReload=True)
        self.friends = itchat.get_friends(update=True)



    def get_seqID(self,HeadImgUrl):
        temp = HeadImgUrl.split('seq=')[1]
        temp = temp.split('&')[0]
        return temp


    def get_dic_ofAllFriends(self):
        NickName_ID = {}
        for i in self.friends:
            # print(i.HeadImgUrl)
            temp = self.get_seqID(i.HeadImgUrl)

            NickName_ID[i.NickName] = temp
        # print(NickName_ID)
        return NickName_ID

#····test····
# a = get_SeqID()
# b = a.get_dic_ofAllFriends()
#
# for k in b.keys():
#     print(k,b[k])


