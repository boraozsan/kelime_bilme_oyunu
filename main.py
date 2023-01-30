import random
import kelime_listesi
kelime = random.choice(kelime_listesi.kelime_listesi)
print(f"şşşşt kelime {kelime}")
bos_cevap=[]
oyun_sonu=False
hak=6
for _ in range(len(kelime)):
 bos_cevap.append("_")
while not oyun_sonu:
 tahmin=input("Bir Harf Yazın.\n").lower()
 if tahmin not in kelime:
  hak-=1
 for sira in range(len(kelime)):
  if tahmin == kelime[sira]:
      bos_cevap[sira]=tahmin
 print(f"{hak} hakkınız kaldı.")
 print(bos_cevap)
 if "_" not in bos_cevap:
   oyun_sonu=True
   print("Kazandınız!")
 if hak==0:
   oyun_sonu=True
   print(f"Kaybettiniz!\nDoğru cevap: {kelime}")