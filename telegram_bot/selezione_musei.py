def scegli_museo():
    print("""stampa 1: Museo Africano \n 2 : Museo di Storia Naturale \n 3 : Museo degli Affreschi 'G.B. Cavalcaselle' e Tomba di Giulietta \n 
    4 : Galleria d'Arte Moderna 'Achille Forti' \n 5 : Museo archeologico al teatro romano \n 6: Sito archeologico degli scavi Scaligeri \n 
    7:Casa di Giulietta \n 8: Museo di Castelvecchio \n 9: Museo Lapidario Maffeiano \n""")
    num = int(input("Scegliere museo: "))
    
    if num == 1:
        museo_africano()
    elif num == 2:
        storia_naturale()
    elif num == 3:
        museo_affreschi()
    elif num == 4:
        arte_moderna()
    elif num == 5:
        teatro_romano()
    elif num == 6:
        scavi_scaligeri()
    elif num == 7:
        casa_giulietta()
    elif num == 8:
        museo_castelvecchio()
    elif num == 9:
        museo_lapidario()
        return
    
def museo_africano():
    print ("mappa")
    print("""Allestito dai Padri Comboniani, è stato fondato nel 1938 con lo scopo di valorizzare le realtà culturali delle popolazioni africane
     presso cui vivono i missionari.\n Sono presenti pannelli descrittivi che ripercorrono le vicende storiche africane, una vastissima raccolta
      di oggetti etnografici (soprattutto strumenti musicali, giochi e suppellettili) provenienti da Egitto, Sudan, Congo, Togo, Burkina Faso e altri 
      stati africani e una biblioteca specializzata.\n Nel 1996 una radicale ristrutturazione ha permesso di riqualificare la funzione del Museo, attraverso
       l'introduzione di nuove tecniche multimediali. Ora, accanto alla funzione etnografica, il Museo ha assunto il ruolo di centro di dialogo
        interculturale per l'educazione allo scambio con le culture e le tradizioni dei popoli dei Paesi del Sud del Mondo. Periodicamente è sede di 
        mostre temporanee a tema.""")

def storia_naturale():
    print ("mappa")
    print("""Il Museo Civico di Storia Naturale di Verona, che trova sede nel prestigioso palazzo Pompei, ospita varie sezioni scientifiche dedicate
     allo studio di minerali e rocce, paleontologia e zoologia.\n Le sezioni di preistoria e botanica sono state trasferite alla Palazzina Comando dell'ex 
     Arsenale Militare Austriaco. Il materiale scientifico raccolto dai ricercatori del Museo e da tanti naturalisti, nel corso di ormai quasi cinque secoli,
      viene oggi meticolosamente preparato e catalogato, prima di essere studiato e quindi conservato nelle collezioni o esposto nelle sale.\n Il Museo 
      svolge quindi un ruolo attivo e determinante nella ricerca scientifica e nella pubblicazione di saggi e testi divulgativi.\n Il fiore all’occhiello 
      del museo è senza dubbio la sezione dedicata ai fossili di Bolca, esemplari di oltre 250 specie animali e 200 vegetali provenienti dai monti Lessini a
       50 chilometri da Verona portavoce di quella che era la vita sulla Terra 50 milioni di anni fa e di come si sia evoluta.""")

def museo_affreschi():
    print ("mappa")
    print("""Il complesso conventuale di S. Francesco al Corso risale al XIII secolo.\n Nel 1935 Antonio Avena, allora Direttore dei Musei Civici, apriva 
    al pubblico la cosiddetta “Tomba di Giulietta”, cioè il luogo in cui era stata posta l’arca che secondo la leggenda accolse i corpi di Romeo e Giulietta, 
    facendone punto di attrazione turistica.\n Nell'annesso Museo degli Affreschi “G.B. Cavalcaselle” (inaugurato nel 1975) sono esposti cicli di affreschi 
    provenienti da edifici veronesi dal Medioevo al Cinquecento e sculture dell’Ottocento, mentre la chiesa di S. Francesco ospita opere su tela di grandi 
    dimensioni dal Cinquecento al Settecento.\n Nel sotterraneo è collocato un deposito di anfore romane del I secolo d.C. rinvenute in scavi della zona.
     Nel cortile è depositato materiale lapideo (architettonico e scultoreo) medievale e moderno in previsione dell’allestimento di un lapidario.""")

def arte_moderna():
    print ("mappa")
    print("""Dopo varie campagne di restauro, uno degli edifici più significativi e centrali della città, Palazzo della Ragione, dal 12 aprile 2014 è la
     nuova sede della Galleria d'Arte Moderna Achille Forti.\n Da sempre cuore pulsante del centro cittadino, il Palazzo ospita le collezioni comunali per 
     la prima volta unite a quelle della Fondazione Cariverona e della Fondazione Domus.\n Il complesso monumentale che comprende la Torre dei Lamberti, la 
     Cappella dei Notai e la Scala della Ragione, viene quindi restituito alla città e ai suoi visitatori, che nelle quattro magnifiche sale allestite con i
      capolavori delle collezioni possono riscoprire opere straordinarie, dal 1840 al 1940, che raccontano la storia di Verona, delle sue collezioni e del 
      loro rapporto con la città. Tra queste, la Meditazione di Francesco Hayez e i dipinti di Giovanni Fattori, Angelo Morbelli, Felice Casorati, Guido
       Trentini, Giacomo Balla, Umberto Boccioni, Gino Rossi, Filippo de Pisis, Giorgio Morandi e le sculture di Medardo Rosso e Arturo Martini.\n La nuova
        Galleria perpetua il nome del grande mecenate Achille Forti (1878-1937): botanico di origine borghese, questo illustre cittadino lasciò al comune di
         Verona la maggior parte del suo vasto patrimonio, il palazzo dove risiedeva, e la sua collezione d’arte.\n Grazie a molteplici donazioni e a un 
         programma di acquisizioni che hanno ampliato questo nucleo originario, oggi la Galleria d’Arte Moderna a Palazzo della Ragione si presenta ai 
         cittadini di Verona e al vasto pubblico internazionale ulteriormente arricchita confermandosi uno dei luoghi di grande varietà e qualità del 
         patrimonio visivo e artistico italiano.""")

def teatro_romano():
    print ("mappa")
    print("""Il Museo Archeologico totalmente rinnovato ed ampliato è situato nell'eccezionale contesto paesaggistico del teatro romano, che si estendeva 
    dalla riva del fiume alla sommità del colle di San Pietro.\n Sui resti dell'edificio da spettacolo, nel Quattrocento fu costruito un convento dai
     Gesuati, una confraternita specializzata nella preparazione di medicine per gli infermi, che prediligeva per le proprie sedi i luoghi ricchi di acqua.\n
      L'ingresso all'area archeologica è situato nel palazzetto Fontana, che ingloba tratti di murature della grande costruzione della scena del teatro, alta
       in origine circa 30 metri.\n In vari luoghi del monumento sono visibili lapidi e rilievi romani, mentre in alto nella splendida cornice del monastero
        si snoda con passaggi all'aperto neglia antichi chiostri, l'esposizione di una ricca collezione di reperti di notevolissimo valore legati anche alle
         decorazioni scultoree del Teatro Romano e dell'Arena.\n La particolarissima collocazione costituisce un elemento fondamentale ed eccezionale della 
         visita all'intero complesso: lo splendido panorama del teatro e della città dall'alto consente infatti di mettere immediatamente in relazione ciò 
         che è esposto nel Museo con il contesto esterno e fa di questo luogo una delle mete imperdibili di Verona.""")

def scavi_scaligeri():
    print ("mappa")
    print("""Verso la fine degli anni settanta, il Comune di Verona iniziò i lavori di restauro del complesso del Palazzo del Capitanio, in Piazza dei 
    Signori. Gli scavi eseguiti in questa occasione hanno portato alla luce numerosi resti archeologici romani e medievali, ora lasciati in vista.\n L’area
     interessata è costituita dalla zona del cortile del palazzo, da Via Dante e da una parte del Palazzo della Ragione o del Comune ed è una delle aree 
     archeologiche urbane più estese del Nord Italia.\n In età romana, la zona era occupata da case più volte ristrutturate, fino al V sec. d.C. Nel secolo
      successivo le abitazioni vennero abbandonate, dopo un lungo periodo di decadenza urbana (come indicato dal progressivo impoverimento dei materiali 
      edilizi utilizzato per le costruzioni successive al V sec.) e fino al X sec. l’area fu adibita ad orto.\n Dall’XI sec. nella zona venne impiantato il
       cimitero della chiesa di S. Maria Antica, abbandonato alla fine del XII sec., quando sull’area ricominciano ad essere costruiti nuovi edifici. Nel
        XIII sec. Alberto I della Scala si appropria di tutta l’area e vi comincia a edificare i palazzi della famiglia scaligera. Le tracce di queste 
        differenti epoche sono state ritrovate durante le ricerche archeologiche.\n L’ingresso agli Scavi è situato in Cortile del Tribunale, verso Piazza
         Viviani. Scesa la scala, il visitatore segue un suggestivo percorso nella storia che non presenta un preciso ordine cronologico in un susseguirsi di
          testimonianze di epoche diverse.\n All’epoca romana appartengono un mosaico pavimentale, con motivi geometrici e animali, e i resti di una casa, di
           edifici pubblici, di una strada lastricata in calcare e di una fognatura a volta in mattoni, della metà del I sec.\n Risalgono all’epoca medievale
            due tombe che facevano parte del cimitero di S. Maria Antica, una cantina appartenente al palazzo di Alberto I della Scala (fine XIII sec.), le
             fondamenta di una casa-torre quadrata, esempi di muratura appartenenti a periodi diversi.\n Di epoca longobarda è invece una tomba per due 
             individui, rinvenuta con alcuni oggetti di corredo.\n Questo interessante percorso, restaurato e reso visitabile grazie al lavoro dell’architetto
              veronese Libero Cecchini è stato adibito nel 1996 dal Comune di Verona a spazio espositivo per iniziative di carattere fotografico. È così 
              diventato sede del Centro Internazionale di Fotografia Scavi Scaligeri, nato per contribuire alla divulgazione, allo studio e allo sviluppo 
              dell’arte fotografica.""")

def museo_castelvecchio():
    print ("mappa")
    print("""Nel 1928 una parte del complesso di Castelvecchio venne adibita a sede museale.\n Danneggiato dai bombardamenti nel corso della seconda guerra
     mondiale, rimase vuoto per una decina d'anni.\n Nel 1957 l'architetto Carlo Scarpa e il direttore del Museo, Licisco Magagnato, avviarono una radicale
      opera di ristrutturazione e riallestimento museale. I lavori, terminati nel 1964, riportarono alla luce l'antica Porta del Morbio, che si apriva nella 
      cinta muraria del XII sec., e restituirono alla città una sede museale universalmente riconosciuta come uno dei capolavori della museografia italiana.
      \n Esprime infatti la genialità dell'architetto veneziano nell'integrare le strutture del passato con l'innovazione del presente e nel rendere 
      l'esperienza di visita al Museo ricca di emozioni e di suggestioni.\n Il Museo di Castelvecchio espone importanti collezioni di arte medievale, 
      rinascimentale e moderna (fino al XVIII secolo); 29 sono le sale dedicate all'esposizione di dipinti, sculture, reperti archeologici e armi. Il museo 
      ospita inoltre un Gabinetto Disegni e Stampe, un Gabinetto Numismatico, e sala Boggian, dedicata ad esposizioni temporanee.""")

def museo_lapidario():
    print ("mappa")
    print("""Fra i più antichi musei pubblici europei, il Lapidario vanta una collezione epigrafica greca, etrusca, paleoveneta e romana, ma anche araba di 
    grande pregio. Fu istituito nel 1745 grazie soprattutto all'appassionata opera di raccolta di Scipione Maffei, insigne uomo di cultura veronese.\n Il 
    museo sorge nel luogo compreso fra le antiche mura che congiungevano piazza Bra e Castelvecchio e fu originariamente pensato come giardino di accesso al
     teatro dell'Accademia Filarmonica. Oggi possiamo ammirare al suo interno le epigrafi che, a partire dal 1612, la stessa Accademia filarmonica ha 
     acquistato, esponendole successivamente al pubblico.\n Il museo fu originariamente allestito da Scipione Maffei, fu poi acquistato dal Comune nel 
     1883 e infine riorganizzato secondo criteri moderni nel 1982.""")

def casa_giulietta():
    print ("mappa")
    print("""L'edificio, risalente al XIII sec., fu a lungo proprietà della famiglia Cappello, il cui stemma è scolpito sull'arco interno del cortile. 
    L'identificazione dei Cappello con i Capuleti ha dato origine alla convinzione che lì sorgesse la casa di Giulietta, eroina della tragedia di 
    Shakespeare.\n La dimora medievale restaurata pittorescamente da Antonio Avena a metà degli anni '30, è stata nel recente passato adibita a mostre
     temporanee.\n L'edificio presenta una bella facciata interna in mattoni a vista, un portale in stile gotico, finestre trilobate, una balaustra che 
     mette in comunicazione dall'esterno i vari corpi della casa e, ovviamente, il famoso balcone.\n Nel cortile è collocata la statua in bronzo di 
     Giulietta, opera dello scultore Nereo Costantini.\n La casa di Giulietta è una delle suggestive sedi che la città mette a disposizione degli sposi per
      la celebrazione del loro matrimonio.""")