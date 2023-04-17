#1-> Random modülü içe aktarılıyor.
import random

#2->Reflex tabanlı ajanı sınıfı tanımlanıyor.
class ModelBasedReflexAgent:
    
    #3->def__init__(self) Sınıfın yapıcı metodu. Ajanın modelini,son perceptini ve son aksiyonunu saklamak için değişkneler Oluşturuluyıor.
    def __init__(self):
        #4->Ajnın kullanılacağı modeli boş bir sözlük olaraj bailatılıyor.
        self.model = {}  # Ortağı simüle etmek için bir model kullanıyoruz.
        self.last_percept = None
        self.last_action = None
       
    #-5-> Modeli güncellemek için bir metot tanımlanıyor. 
    def model_update(self, percept, action, next_percept): 
        
        #6-> Eüer modelde percept yok ise 
        if percept not in self.model:
            
            #7-> Yeni bir girdi (percept) ekleyerek, bu girdiye karşılık gelen boş bir sözlük oluşturuyoruz.
            self.model[percept] = {}
            
        #8->Bu girdi-aksiyon çiftini, bir sonraki percept ile eşleştirerek modeli güncelliyoruz.
        self.model[percept][action] = next_percept
        print(next_percept)
    #9-> Modeli kullanarak bir sonraki percepti tahmin etmek için bir metot tanımlıyoruz.
    def model_lookup(self, percept):
        
        # 10->Eğer modelde bu percept ve son aksiyon varsa...
        if percept in self.model and self.last_action in self.model[percept]:
            
            #11-> Bu percept-aksiyon çiftine karşılık gelen sonraki percepti döndürüyoruz.
            return self.model[percept][self.last_action]
        
        #12->- Model tahmin edemediği zaman None döndürüyoruz
        return None
        
    #13->- Aksiyon üretmek için bir metot tanımlıyoruz.
    def action(self, percept):
        # 14->Modeli kullanarak bir sonraki percepti tahmin ediyoruz.
        next_percept = self.model_lookup(percept)
        
        #15->- Eğer model tahmin edemediyse...
        if next_percept is None:
            
            # 16->Rastgele bir aksiyon seçiyoruz.
            action = random.choice(["Aksiyon 1", "Aksiyon 2"])
            
        
        else:
            #17->- Eğer model tahmini 0.5'den küçükse...
            if next_percept < 0.5:
                #18-> Aksiyon 1 i seçiyoruz
                action = "Aksiyon 1"
                
            #1-> Aksi halde, Aksiyon 2'yi seçiyoruz.
            else:
                action = "Aksiyon 2"
                
        #20-> Modeli güncelliyoruz.
        self.model_update(self.last_percept, self.last_action, percept)
        
        # 21-> Son percepti güncelliyoruz.
        self.last_percept = percept
        
        #22-> Son actionu güncelliyoruz.
        self.last_action = action
        
        #23->Seçilen aksiyonu döndürüyoruz.
        return action


agent = ModelBasedReflexAgent()
for i in range(10):
    percept = random.random()  # Rastgele bir girdi üretiyoruz.
    action = agent.action(percept)
    print(f"Girdi: {percept:.2f}, Aksiyon: {action}")