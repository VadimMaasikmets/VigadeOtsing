#1
name= input("sissestage eesnimi: ")
age = int(input("vanus: "))
if name.upper()== "JUKU":
    if age >=1 and age <6:
        print("pilet on tasuta")
    elif age >=6 and age <14:
        print("lastepilet")
    elif age >=15 and age <=65:
        print("täispilet")
    elif age >65:
        print("sooduspilet")
    elif age <0 and age >100:
        print("viga")
    print("Lähme kinno")
else:
    print("sorry, ainult Juku läheb kinno")

#2
print("Kirjutage teie nimed")
a= input("nimi 1: ")
b= input("nimi 2: ")
if a=="vadim" and b=="nikita" or a=="nikita" and b=="vadim":
    print("Pinginaabrid")
else:
    print("Nad ei ole naabrid")
#3
pikkus= float(input("sisesta toa pikkus meetrites: "))
laius= float(input("sisesta toa laius meetrites: "))
ppindala= pikkus * laius
print(f"toa põranda pindala: {ppindala} ruutmeetrit.")
remont= input("kas soovite teha remonti (jah/ei)?").lower()
if remont== "jah":
    ruutmeetri= float(input("sisesta ruutmeetri põranda hind: "))
    koguhind= ppindala * ruutmeetri
    print(f"põranda vahetamise koguhind: {koguhind} eurot.")
else:
    print("Tänan. Edu teile.")
#4
alghind= float(input("sisesta alghind: "))
if alghind > 700:
    soodustus = 0.3 * alghind
    soodustusega= alghind - soodustus
    print(f"30% soodustusega hind: {soodustusega}")
else:
    print("alghind ei ole suurem kui 700, soodustust ei kohaldata.")
#5
temp= float(input("sisesta temperatuur kraadides: "))
if temp > 18:
    print("temperatuur on üle kaheksateistkümne kraadi, see on soovitatav toassoojus talvel.")
else:
    print("temperatuur ei ole üle kaheksateistkümne kraadi.")
#6
pikkus= float(input("sisesta oma pikkus meetrites: "))
lpiik= 1.60
ppiik= 1.80
if pikkus < lpiik:
    print("Sa oled lühike")
elif lpiik <= pikkus <= ppiik:
    print("sa oled keskmise pikkusega")
else:
    print("sa oled pikk")
#7
pikkus=float(input("Sisesta oma pikkus meetrites."))
sugu=input("sisesta sugu mees/naine")
kraj_korot=1.60
kraj_vqsok=1.80
if sugu.lower()=="mees":
    if pikkus<kraj_korot:
        print("mees on lühike")
    elif kraj_korot<=pikkus<=kraj_vqsok:
        print("mees on keskmise pikkusega")
    else:
        print("mees on pikk")
elif sugu.lower()=="naine":
    if pikkus<kraj_korot:
        print("naine on lühike")
    elif kraj_korot<=pikkus<=kraj_vqsok:
        print("naine on keskmise pikkusega")
    else:
        print("naine on pikk")
else:
    print("sisesta sugu (mees/naine).")
#8
import random
tooted=["piim","sai","leib","juust","vorst"]
hinnad={toode: round(random.uniform(1, 5), 2) for toode in tooted}
ostukorv ={}
for toode in tooted:
    kogus=int(input(f"mitu tükki {toode} soovid osta? (0 kui ei soovi): "))
    if kogus>0:
        ostukorv[toode]=kogus
summa=sum(ostukorv[toode]*hinnad[toode] for toode in ostukorv)
print("\n----------- TŠEKK -----------")
for toode, kogus in ostukorv.items():
    hind=hinnad[toode]
    toote_summa=kogus*hind
    print(f"{toode.capitalize()}x{kogus}:{hind:.2f}€/tk ={toote_summa:.2f} €")
print("-----------------------------")
print(f"Kokku: {summa:.2f} €")
print("-------------------------------")
#11
dr=input("Когда др? (YYYY-MM-DD): ")
god=int(dr[:5])
if(god%4)==0:
    print("С др, это юбилей!")
else:
    print("Это не юбилей.")
#12
toote_hind=float(input("Hind euros: "))
if toote_hind<=10:
    soodustus_protsent=10
else:
    soodustus_protsent=20
soodustatud_hind=toote_hind*(1-soodustus_protsent/100)
print(f"Lõppu hind {soodustus_protsent}% soodustus {soodustatud_hind:.2f} euro.")
#13
pol=input("missugune sugu (mees/naine): ")
if pol=="naine":
   print("ainult mehed!")
if pol.lower()=="mees":
    vanus=int(input("Mis vanus?: "))
    if 16<=vanus<=18:
        print("Ok!")
    else:
        print("NO.")
#14
inimeste_arv=int(input("Inimeste kogus: "))
bussi_suurus=int(input("Bussi suurus: "))
busside_arv=inimeste_arv//bussi_suurus
viimase_bussi_inimesed=inimeste_arv%bussi_suurus
print(f"vaja on {busside_arv} bussi.")
print(f"viimases bussis on {viimase_bussi_inimesed} inimest.")