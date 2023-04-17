import random


#Robot sınıfını tanımlanıyor. Bu sınıf, robotun pozisyonunu ve sense() ve act() adlı iki yöntemini içermektedir.
class Robot:
    #init yoüntemi Robot nesnesi oluiturulduğunda cağırılır ve robotun baslangıç pozisyonunu  alıyor.
    def __init__(self,position):
        self.position=position
        
    #sense() yöntemi, robotun hedefe doğru hareket etmesine karar vermek için çevre durumunu analiz ediliyor.
    def sense(self,envoirment):
        if self.position<envoirment:
            return "left"
        
        elif self.position>envoirment:
            return "right"
        
        else:
            return "stop"
        
    #act() yöntemi, robotun hareketini günceller ve hareket yönüne göre pozisyonunu artırır veya azaltır.
    def act(self,action):
        if action=="left":
            self.position-=1
            
        if action=="right":
            self.position+=1
            
        else:
            pass


#Environment sınıfını tanımlanıyor. Bu sınıf, robotun hareket ettiği çevreyi temsil eder.
class Environment:
        
    #__init__ yöntemi, self.target adlı bir değişken oluşturarak random.randint(0, 100)
    # kullanarak 0 ile 100 arasında rastgele bir hedef pozisyon oluşturuyor.
    def __init__(self):
        self.tareget=random.randint(0,100)
            
    #run yöntemi, bir Robot nesnesi oluşturarak random.randint(0, 100) 
    # kullanarak 0 ile 100 arasında rastgele bir başlangıç pozisyonu belirliyor
    def run(self):
         
        robot=Robot(random.randint(0,100))
            
        #Daha sonra bir sonsuz döngü içinde robot.sense(self.target) kullanarak robotun hareket yönünü 
        # belirliyor ve robot.act(action) yöntemiyle robotun hareketini güncelliyor. 
        while True:
            
            #Robot sınıfının sense() yöntemi, robotun hedefe olan uzaklığını hesaplar ve bir hareket yönü belirler.
            action=robot.sense(self.tareget)
            robot.act(action)
            print ("position",robot.position,"Action:",action)
                
            if action=="stop":
                break
            
            elif robot.position == 0 or robot.position == 100:
                print("Robot kenara ulaştı, durdu.")
                break
    
if __name__ == '__main__':
    env = Environment()
    env.run() 
    
    
#bir kişi bir şehirdeki bir kafede oturuyor ve arkadaşını bekliyor. Arkadaşı hedef konumundadır. 
# Bu durumda, kişi arkadaşına ne kadar yakın olduğunu hissederek arkadaşını bekleyebilir. 
# Yakınlaştıkça arkadaşının pozisyonunu kontrol eder. 
# Eğer arkadaşı solundaysa, kişi sağa doğru hareket ederek yaklaşmaya çalışabilir. 
# Eğer arkadaşı sağındaysa, kişi sola doğru hareket ederek yaklaşmaya çalışabilir. 
# Eğer kişi arkadaşının tam karşısında ise, kişi hareketsiz kalabilir.

#Benzer şekilde, robotun hedefe yaklaştıkça hareket yönünü belirlemesi ve
# hedefe doğru ilerlemesi gibi sense() ve act() işlemleri, günlük hayatta da kullanılır. 
# Örneğin, bir araba navigasyon sistemi, aracın bulunduğu konumu ve hedef konumunu alarak 
# aracı hedefe yönlendirmek için benzer işlemleri yapabilir