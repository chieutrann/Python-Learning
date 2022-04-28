class CD:
    def __init__ (self,name,singer,NumofSong ,price):
        self.name= name
        self.singer = singer
        self.NumofSong = NumofSong
        self.price = price

    def show_info(self):
        print(f'#{self.name}-- {self.singer}--{self.NumofSong}--{self.price}#')

def add_CD():
    name =input('Enter song name:')
    singer = input('Enter Singer:')
    NumofSong = input("Enter number of songs:")
    price = input("Enter the price:")
    return CD(name=name, singer=singer,NumofSong=NumofSong, price=price)



tt=1
DSCD=[]
while tt==1:
    cd_new= add_CD()
    DSCD.append(cd_new)
    tt=int(input('Type 1 to continue or 0 to end'))
total=0
for cd in DSCD:
    cd.show_info()
    total+= (int)(cd.price)* (int)(cd.NumofSong)
print("Total Amount : " + str(total))





