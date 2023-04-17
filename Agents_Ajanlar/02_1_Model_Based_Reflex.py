#https://waymo.com/sf/

import random

class ModelBasedReflexAgent:
    def __init__(self):
        #Ortağı simüle etmek için bir model kullanıyoruz
        # ajanın bir modeli kullanarak ortağın davranışını taklit ettiğini veya simüle ettiğini ifade etmektedir.
        self.model={}
        
        self.last_percept=None
        self.last_action=None
        
    def model_update(self,percept,action,next_percept):
        #Modeli güncelliyoruz
        if percept not in self.model:
            self.model[percept]={}
            
        self.model[percept][action]=next_percept
        
    #Modele bakma işlemi yapıyoruz.
    def model_lookup(self,percept):
        #Modelimizi kullanarak bir sonraki percepti tahmin ediyoruz.
        if percept in self.model and self.last_action in self.model[percept]:
            return self.model[percept][self.last_action]
        
        return None
    
    def action(self,percept):
        #Ortağın aksiyonunu seçiyoruz
        next_percept=self.model_lookup(percept)
        if next_percept is None:
            #Model tahmin edemediği zaman rastgele bir aksiyon seçiyoruz.
            action=random.choice(["Aksiyon 1","Aksiiyon 2"])
            
            
        else:
            #Model tahmin ettiği zaman en uygun alsiyonu seçeriz
            if next_percept<0.5:
                action="Aksiyon 1"
            
            else:
                action="Aksiyon 2"
                
        
        self.model_update(self.last_percept,self.action,percept)
        self.last_percept=percept
        self.last_action=action
        return action
    
#simüle etmek için, bir aha ve ortamı  simüle edebileceğimiz bir döngü olıuşturuluyor.
agent=ModelBasedReflexAgent()
for i in range(10):
    percept=random.random()
    action=agent.action(percept)
    print(f"Girdi: {percept:.2f}, Aksiyon: {action}")
