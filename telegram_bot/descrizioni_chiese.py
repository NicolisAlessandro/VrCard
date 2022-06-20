
def scegli_chiesa():
    print("stampa 1 : Chiesa di San Lorenzo \n 2 : complesso del Duomo \n 3 : Basilica di Santa Anastasia \n 4 : Chiesa di San Fermo \n 5 : Basilica di San Zeno \n 6 : Chiesa di San Bernardino \n 7 : Chiesa di San Giorgio in Braida \n 8 :Chiesa di Santa Maria in Organo \n 9 : Chiesa di Santa Maria Antica \n 10 : torna indietro ")

    num = int(input("Scegliere funzione: "))
    if num == 1:
        chiesa_san_lorenzo()
    elif num == 2:
        complesso_duomo()
    elif num == 3:
        basilica_santa_anastasia()
    elif num == 4:
        chiesa_san_fermo()
    elif num == 5:
        basilica_san_zeno()
    if num == 6:
        chiesa_san_bernardino()
    elif num == 7:
        chiesa_san_giorgio()
    elif num == 8:
        chiesa_santa_maria_organo()
    elif num == 9:
        chiesa_santa_maria_antica()
    elif num == 10:
        return
    

def chiesa_san_lorenzo():
    print("""Chiesa romanica dell'inizio del XII sec., fu costruita sul luogo di una precedente basilica paleocristiana (frammenti di decorazioni nel cortile d'accesso). Subì pesanti interventi di restauro nel 1877 e nel secondo dopoguerra.
             L'edificio presenta il tipico paramento delle costruzioni romaniche veronesi, a fasce alternate di tufo giallo-ocra e mattoni rossi, con alcuni filari di ciottoli disposti a spina di pesce. La facciata è compresa fra due insolite torri scalari cilindriche,
              attraverso le quali si aveva accesso ai matronei. Il protiro pensile e il campanile (ricostruito in epoca recente) risalgono alla seconda metà del XV sec.\n L’interno è a tre navate; sopra quelle laterali si trovano i matronei, con logge che si affacciano sulla navata centrale.\n Sull'altare maggiore è posto il dipinto Madonna con Bambino che appare ai santi di Domenico Brusasorci (1566).
             Notevoli i frammenti di affreschi del XIII e XIV sec. raffiguranti angeli e santi e, nella cappella della navata sinistra, il David di Nicolò Giolfino.""")

def complesso_duomo():
    print("""Più che un singolo edificio la Cattedrale, dedicata a Santa Maria Assunta, risulta essere un complesso architettonico articolato di cui fanno parte San Giovanni in Fonte,
     Santa Elena, il chiostro dei Canonici, la biblioteca Capitolare, il museo Canonicale, l'antistante piazza e il Vescovado.\n Nella zona dove sorge oggi il Duomo si trovavano, in epoca romana,
      delle ville con balnea privati e, probabilmente, dei tempietti per il culto.
    La prima basilica paleocristiana fu costruita nell'area occupata attualmente dalla chiesa di Santa Elena. Consacrata da San Zeno, vescovo di Verona tra il 362 e il 380, risultò presto troppo piccola e, qualche decennio più tardi, si provvide all'edificazione di una basilica più ampia. Ampi resti di pavimento a mosaico delle due basiliche paleocristiane sono visibili sotto la chiesa di Santa Elena e nel chiostro canonicale.\n La seconda basilica paleocristiana crollò, verosimilmente nel VII secolo,
     a causa di un violento incendio o, forse, di un terremoto. La ricostruzione fu guidata dall'arcidiacono Pacifico, tra VIII e IX secolo. La Cattedrale, menzionata come Santa Maria Matricolare, venne spostata a sud, nell'area sulla quale insiste l'attuale edificio.\n La chiesa fu gravemente danneggiata dal terremoto del 1117. Il cantiere di restauro si protrasse per almeno un ventennio: l'edificio acquistò l'ampiezza attuale e vennero realizzati i due protiri romanici.\n L'interno venne completamente
      rinnovato tra la metà del XV e la metà del XVI secolo, con la costruzione di cappelle laterali e l'inserimento del tornacoro semicircolare. All'esterno: la facciata d’impianto romanico, il doppio protiro di Nicolò (1138), il portale con rilievi e lunetta, lo splendido protiro laterale e la zona absidale. All'interno: il tornacoro di Sanmicheli, opere di Falconetto, Liberale, Giolfino, Torbido e l’Assunzione della Vergine di Tiziano (1530).	""")

def basilica_santa_anastasia():
    print("""La chiesa di Sant'Anastasia è uno splendido esempio di gotico italiano. Fu eretta a partire dal 1290 con il contributo della famiglia che governava la città, gli Scaligeri, e di altre famiglie veronesi.
     Prima dell'attuale edificio qui esistevano due chiese dedicate, una a Sant'Anastasia e l'altra a San Remigio.\n Nel 1290 i domenicani chiamati a custodirle, decisero di costruire al loro posto un'unica chiesa dedicata a San Pietro da Verona detto anche San Pietro Martire,
      ma il popolo continuò a chiamarla Sant'Anastasia. Accanto alla chiesa i monaci domenicani avevano un grande convento.\n L'opera di costruzione del sacro edificio continuò per tutto il 1300 e il 1400 e finalmente nel 1500 si ebbe l'ultima fase dei lavori per il suo completamento.
       La facciata è l'unico elemento mai portato a termine.\n Sant'Anastasia è la chiesa più grande di Verona. La basilica si sviluppa in tre grandi navate sorrette da 12 imponenti colonne di marmo rosso di Verona. Sul transetto si aprono 5 cappelle. Sul lato sinistro si apre l'antico oratorio del convento, Cappella Giusti.
        La chiesa, ricchissima di opere d'arte, custodisce anche il celebre affresco del Pisanello San Giorgio e la Principessa, tornato nella sua collocazione originaria sopra la Cappella Pellegrini.\n All'esterno la facciata incompiuta con lo splendido portale gotico e la zona absidale, posta sulla riva del fiume Adige. All'interno: gli altari con le cappelle con opere di Pietro da Porlezza, Cattaneo, Michele da Firenze, Liberale da Verona, Girolamo Dai Libri, Giolfino, Brusasorzi, Altichiero, e Pisanello. All'ingresso i singolari gobbi che reggono l'acquasantiera.	""")

def chiesa_san_fermo():
    print("""Nel luogo in cui nel 304, secondo l'antica tradizione, subirono il martirio i santi Fermo e Rustico, il popolo di Verona costruì, nel V secolo, una chiesa in loro onore. Tra il 755 il 759, il vescovo di Verona Annone recuperò a Trieste le reliquie dei Martiri e le depose nella chiesa paleocristiana.
    \n Dal 1065 al 1143 circa, i Benedettini demolirono fino al pavimento la chiesa paleocristiana e, per conservare le reliquie dove le aveva poste Annone, costruirono una chiesa romanica su due piani: quella inferiore per custodirvi le reliquie e quella superiore per le celebrazioni con il popolo.\n Nel 1261 i Francescani 
    sostituirono i Benedettini a San Fermo e trasformarono la chiesa superiore e l'atrio antistante nella forma attuale: l'opera poteva dirsi conclusa verso il 1350. Lungo i secoli vi aggiunsero altari, cappelle e monumenti funebri.\n Nel 1759 per preservare le reliquie dei Martiri dalle alluvioni dell'Adige, il sarcofago, con la cassa di piombo e le reliquie,
     fu posto al centro del nuovo altare maggiore della chiesa superiore. Nel 1807 i Francescani, a seguito dell'occupazione napoleonica, furono costretti a lasciare San Fermo.\n All'esterno: il portale con le arche poste ai lati e la zona absidale. All'interno: il superbo soffitto ligneo a carena multipla di nave e affreschi del XIV e XV secolo, opere di Turone, Torbido, Stefano e Liberale da Verona,
      Caroto e affresco di Pisanello; la chiesa inferiore, rarissima per le quattro navate, è un gioiello del romanico.	""")

def basilica_san_zeno():
    print("""La basilica di San Zeno è senza dubbio una delle più belle chiese romaniche esistenti in Italia. L'intenso cromatismo è dato dall’impiego della pietra di tufo usata sola o alternata a mattoni.\n L'origine del primitivo nucleo di San Zeno è da ricondurre alla chiesa e al cenobio eretti nell'area cimiteriale romana e paleocristiana vicina alla Via Gallica, sorti sul luogo di sepoltura del Vescovo Zeno per conservarne la memoria e le reliquie.
     San Zeno, di origine africana, fu l'ottavo vescovo di Verona (362-380 circa) e convertì la città al cristianesimo.\n Il primitivo nucleo subì nel VI secolo dei rifacimenti. Con l'espandersi del culto del Santo, fra l'805 e l'806, venne realizzata una basilica più vasta con annesso monastero, consacrata nell'806.\n Alla fine dell'XI secolo la chiesa fu oggetto di un grande ampliamento e rinnovamento: la quasi totalità della struttura attuale è da riferire a questa fase dei lavori. 
     Il terremoto del 1117 compromise gran parte dell'opera già eseguita. I lavori, ripresi subito dopo il terremoto, si protrassero fino al 1138.\n Altri importanti interventi si susseguirono nei secoli XII, XIV e XIX. Il complesso di San Zeno, cessò di esistere come monastero per volere della Repubblica Veneta nel 1770.\n All'esterno: la facciata con il grande rosone detto “Ruota della fortuna”, i bassorilievi marmorei ai lati del protiro, le famose porte bronzee, il campanile e la Torre dell'Abbazia (XII sec.).
     \n All'interno: affreschi dal XII al XIV sec, il fonte battesimale, il soffitto a carena di nave, la cripta con le spoglie di San Zeno, la statua policroma detta “San Zen che ride” e il celebre trittico di Andrea Mantegna (1457-59).	""")

def chiesa_san_bernardino():
    print("""Il complesso conventuale di san Bernardino è stato iniziato due anni dopo la canonizzazione del santo senese, nel 1452, su esplicita richiesta dei veronesi. Sopravvisse a stento alle soppressioni e spoliazioni del secolo XIX. 
    Il convento servì, di volta in volta, sotto i francesi, gli austriaci e il Regno d'Italia come ospedale, cimitero cittadino, magazzino e collegio.\n Il luogo per la fondazione della chiesa e dell'annesso convento fu scelto da san Giovanni da Capestrano, compagno e amico di san Bernardino da Siena, dopo la canonizzazione di quest'ultimo nel 1450. San Bernardino, propugnatore del movimento dell'Osservanza all'interno dell'Ordine Francescano e celebre predicatore, fu a Verona nel 1422 e nel 1443.
    \n Con la sua predicazione diffondeva la venerazione del nome di Gesù, che raffigurava nel monogramma IHS (Iesus Hominum Salvator) contornato da un sole di dodici raggi (i dodici apostoli).\n Il complesso comprende quattro chiostri. Il maggiore (chiostro di Sant'Antonio, dalle raffigurazioni delle lunette) serve da sagrato della chiesa. La chiesa, interamente costruita in mattoni, è un edificio tipico, per sobrietà formale e semplicità strutturale, dell'architettura degli ordini mendicanti.	""")

def chiesa_san_giorgio():
    print("""Fondato come monastero dei Benedettini nel 1046, fu completamente rinnovato in forme rinascimentali dopo che il cenobio fu ceduto alla congregazione di San Giorgio in Alga, nel 1441.\n L'edificio è dominato dalla grande cupola di Michele Sanmicheli, per la cui realizzazione fu mozzata la torre romanica in tufo, sul fianco della chiesa. La facciata in marmo bianco è a due ordini e presenta nicchie con statue di santi. 
    L'interno è a navata unica, fiancheggiata da cappelle cinquecentesche.\n Di grande pregio le opere pittoriche qui conservate. Oltre ai dipinti di Domenico Tintoretto, Domenico e Felice Brusasorci, Bernardino India, Giovan Francesco e Francesco Caroto, Paolo Farinati e Moretto da Brescia, sono da segnalare il Battesimo di Cristo di Jacopo Tintoretto, le portelle dell'organo dipinte da Girolamo Romanino e la Sacra Conversazione di Girolamo dai Libri.
     Nell'abside, l'altare di scuola sanmicheliana inquadra lo splendido Martirio di San Giorgio, capolavoro di Paolo Veronese, la sua più grande e bella opera conservata a Verona.	""")

def chiesa_santa_maria_organo():
    print("""La chiesa, in prossimità della porta Organa, esisteva già in epoca longobarda e in seguito diventò un importante monastero benedettino.\n Durante la metà del XV secolo, vennero edificati la sagrestia ("la più bella d'Italia" per G.Vasari) e il presbiterio, entrambi impreziositi dalle tarsie lignee di Fra' Giovanni da Verona; negli stessi anni Francesco Da Castello edificava il chiostro e il campanile.\n L'interno, vivacemente affrescato, è ricco di im­portanti dipinti di artisti rinascimentali veronesi.
     Nella cripta (VI - VIII sett.) sono presenti elementi romani di spoglio.\n La facciata incompiuta è opera di Mi­chele Sanmicheli.\n\n CORO DI SANTA MARIA IN ORGANO\n Nelle pareti del presbiterio, dietro l'altare maggiore, è addossato il coro in legno di noce che si compone di 41 stalli, 27 nel registro superiore e 14 in quello inferiore. Sul fregio, sopra la cattedra centrale, è intarsiata la data 1499. L'opera, che ha subito nel corso dei secoli vari rimaneggiamenti e restauri, venne realizzata a partire dal 1494 da fra Giovanni da Verona (1457-1525) insieme ad alcuni allievi.
     \n In ogni stallo, con i braccioli decorati da grifoni con volto umano, lo schienale è suddiviso in pilastrini variamente intarsiati e inquadrato da un arco sostenuto da lesene. Le 27 tarsie rappresentano un sunto dell'arte prospettica italiana nella quale si cristallizza la formula dei “falsi armadi” con vedute di città o paesaggi. Vi sono riferimenti precisi alla città di Verona, al patrono S.Zeno e alla chiesa di S.Maria in organo.\n Il coro venne completato con il leggio realizzato tra il 1500 e il 1501.	""")

def chiesa_santa_maria_antica():
    print("""Santa Maria Antica è una chiesa in stile romanico situata nel centro storico di Verona, a lato delle gotiche arche scaligere.\n Sorge sul luogo di una precedente chiesetta dell'VIII secolo; venne distrutta dal terremoto del 1117 e poi ricostruita. Il nuovo tempio venne consacrato nel 1185 dal patriarca d'Aquileia, mentre Papa Alessandro III, nel 1177, ne avrebbe consacrato l'altare maggiore. Nel periodo scaligero divenne la “cappella privata” della famiglia Della Scala, che fece costruire, a fianco, le Arche scaligere, ovvero il cimitero di famiglia.
    \n Modificata, soprattutto all'interno, più volte nel corso dei secoli, fu riportata all'essenza originale grazie ai restauri tardo-ottocenteschi. Si accede alla chiesa dall'ingresso laterale, sovrastato dall'arca di Cangrande I della Scala. Il sarcofago è situato entro un arco trilobato e sovrastato da una statua equestre del principe, fedele riproduzione dell'originale custodita nel museo di Castelvecchio.\n L'interno della chiesa è a tre navate, divise da due serie di sette colonne in pietra rossa con capitelli squadrati e archi a sesto rialzato, che terminano in altrettante piccole absidi ricavate nello spessore del muro.
     Un mosaico con decorazioni a tessere bianche e nere, riferibile al pavimento originale della chiesa di Santa Maria Antica (circa metà dell'VIII secolo) è stato rinvenuto nel secolo XIX.\n Le recenti ricerche archeologiche hanno tra l'altro attestato l'esistenza, nei pressi della chiesa, di un'area cimiteriale abbastanza vasta. Sono state qui, infatti, rinvenute una cinquantina di sepolture, tutte d'età successiva alla fondazione della chiesa e probabilmente attribuibili in buona parte al secolo XI.	""")


    
scegli_chiesa()
