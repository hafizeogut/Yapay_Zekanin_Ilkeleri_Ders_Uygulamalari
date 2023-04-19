# Durumlar ve geçiş fonksiyonları tanımlanır
durumlar = ["A", "B", "C"]
gecisler = {
    "A": {"B": 1, "C": 2},
    "B": {"A": 3, "C": 4},
    "C": {"A": 5, "B": 6}
}

# Hedef fonksiyonu tanımlanır

def hedef(durum):
    if durum=="C":
        return True
    
    else:
        return False
    
#Problem çözme ajanı tamamlanır
def problem_cozme_ajani(durum,gecis,hedef):
    yol=[]
    while True:
        yol.append(durum)
        print("yol",yol)
        if hedef(durum):
            return yol
        
        elif not gecisler.get(durum):
            return None
        
        else:
            gecis=max(gecisler[durum],key=gecisler[durum].get)
            print("gecis",gecis)
            durum=gecis
            
#Problem çözme ajanı çalıitırılır
sonuc=problem_cozme_ajani("A",gecisler,hedef)
print(sonuc)