"""Arma las doce clases de A2 a C2 y el vocabulario que les falta."""

from course_upper import A2_NEW, B1_NEW, B2_NEW, L, w

C1_NEW = [
    w("sottile", "sotile", "sutil", "È una differenza sottile.", "e una diferentsa sotile", "Es una diferencia sutil."),
    w("sarcastico", "sarkastiko", "sarcástico", "Il tono è sarcastico.", "il tono e sarkastiko", "El tono es sarcástico."),
    w("letterale", "leterale", "literal", "Non prenderlo alla lettera.", "non prenderlo ala letera", "No lo tomes al pie de la letra."),
    w("prolisso", "proliso", "prolijo; largo de más", "Il testo è prolisso.", "il testo e proliso", "El texto es demasiado largo."),
    w("conciso", "konchiso", "conciso", "Sii conciso.", "si konchiso", "Sé conciso."),
    w("campione", "kampione", "muestra", "Il campione è piccolo.", "il kampione e pikolo", "La muestra es chica."),
    w("statistica", "statistika", "estadística", "La statistica conferma.", "la statistika konfirma", "La estadística confirma."),
    w("percentuale", "perchentuale", "porcentaje", "La percentuale sale.", "la perchentuale sale", "El porcentaje sube."),
    w("variabile", "variabile", "variable", "C'è un'altra variabile.", "che unaltra variabile", "Hay otra variable."),
    w("correlazione", "korelatsione", "correlación", "Non c'è correlazione.", "non che korelatsione", "No hay correlación."),
    w("sondaggio", "sondayo", "encuesta", "Il sondaggio è recente.", "il sondayo e rechente", "La encuesta es reciente."),
    w("bozza", "botsa", "borrador", "Ti mando la bozza.", "ti mando la botsa", "Te mando el borrador."),
    w("revisione", "revisione", "revisión", "Serve una revisione.", "serve una revisione", "Hace falta una revisión."),
    w("sintesi", "sintesi", "síntesis", "Fai una sintesi.", "fai una sintesi", "Hacé una síntesis."),
    w("saggio", "sayo", "ensayo", "Scrivo un saggio.", "skrivo un sayo", "Escribo un ensayo."),
    w("paragrafo", "paragrafo", "párrafo", "Leggi il paragrafo.", "leyi il paragrafo", "Leé el párrafo."),
    w("citazione", "chitatsione", "cita", "Manca la citazione.", "manka la chitatsione", "Falta la cita."),
    w("normativa", "normativa", "normativa", "La normativa è chiara.", "la normativa e kiara", "La normativa es clara."),
    w("ricorso", "rikorso", "recurso", "Presento ricorso.", "presento rikorso", "Presento un recurso."),
    w("sentenza", "sententsa", "sentencia", "La sentenza è definitiva.", "la sententsa e definitiva", "La sentencia es definitiva."),
    w("tribunale", "tribunale", "tribunal", "Il tribunale decide.", "il tribunale dechide", "El tribunal decide."),
    w("avvocato", "avokato", "abogado", "Parla con l'avvocato.", "parla kon lavokato", "Hablá con el abogado."),
    w("mediazione", "mediatsione", "mediación", "Propongo una mediazione.", "propongo una mediatsione", "Propongo una mediación."),
    w("negoziato", "negotsiato", "negociación", "Il negoziato continua.", "il negotsiato kontinua", "La negociación sigue."),
    w("algoritmo", "algoritmo", "algoritmo", "L'algoritmo sbaglia.", "lalgoritmo sbalia", "El algoritmo se equivoca."),
    w("piattaforma", "piataforma", "plataforma", "La piattaforma è nuova.", "la piataforma e nuova", "La plataforma es nueva."),
    w("privacy", "praivasi", "privacidad", "Rispetta la privacy.", "rispeta la praivasi", "Respetá la privacidad."),
    w("brevetto", "breveto", "patente", "Hanno il brevetto.", "ano il breveto", "Tienen la patente."),
    w("innovazione", "inovatsione", "innovación", "L'innovazione costa.", "linovatsione kosta", "La innovación cuesta."),
    w("etica", "etika", "ética", "È una questione di etica.", "e una kwestione di etika", "Es una cuestión de ética."),
    w("dilemma", "dilemma", "dilema", "È un dilemma.", "e un dilemma", "Es un dilema."),
    w("principio", "principio", "principio", "È una questione di principio.", "e una kwestione di princhipio", "Es una cuestión de principio."),
    w("responsabilità", "responsabilitá", "responsabilidad", "Di chi è la responsabilità?", "di ki e la responsabilitá", "¿De quién es la responsabilidad?"),
    w("empatia", "empatia", "empatía", "Manca empatia.", "manka empatia", "Falta empatía."),
    w("resilienza", "resilientsa", "resiliencia", "Serve resilienza.", "serve resilientsa", "Hace falta resiliencia."),
    w("consapevolezza", "konsapevoletsa", "conciencia", "Prendi consapevolezza.", "prendi konsapevoletsa", "Tomá conciencia."),
    w("diplomazia", "diplomatsia", "diplomacia", "Ci vuole diplomazia.", "chi vole diplomatsia", "Hace falta diplomacia."),
    w("trattato", "tratato", "tratado", "Firmano il trattato.", "firmano il tratado", "Firman el tratado."),
    w("sanzione", "santsione", "sanción", "Arriva una sanzione.", "arriva una santsione", "Llega una sanción."),
    w("efficace", "efikache", "eficaz", "Il metodo è efficace.", "il metodo e efikache", "El método es eficaz."),
    w("oscuro", "oskuro", "oscuro", "Il passaggio è oscuro.", "il pasayo e oskuro", "El pasaje es oscuro."),
    w("trasparente", "trasparente", "transparente", "Il processo è trasparente.", "il procheso e trasparente", "El proceso es transparente."),
    w("bibliografia", "bibliografia", "bibliografía", "Controlla la bibliografia.", "kontrol a la bibliografia", "Revisá la bibliografía."),
    w("nota", "nota", "nota", "Vedi la nota.", "vedi la nota", "Mirá la nota."),
    w("capitolo", "kapitolo", "capítulo", "Il capitolo è lungo.", "il kapitolo e lungo", "El capítulo es largo."),
    w("indice", "indiche", "índice", "Guarda l'indice.", "guarda lindiche", "Mirá el índice."),
    w("dibattito", "dibattito", "debate", "Il dibattito è acceso.", "il dibattito e acheso", "El debate está picante."),
    w("moderatore", "moderatore", "moderador", "Il moderatore interviene.", "il moderatore interviene", "El moderador interviene."),
    w("intervento", "intervento", "intervención", "Un intervento breve.", "un intervento breve", "Una intervención breve."),
    w("replica", "replika", "réplica", "Ha diritto di replica.", "a dirito di replika", "Tiene derecho a réplica."),
    w("consenso", "konsenso", "consenso", "Manca il consenso.", "manka il konsenso", "Falta el consenso."),
    w("dissenso", "disenso", "disenso", "Esprimi il dissenso.", "esprimi il disenso", "Expresá el disenso."),
]

C2_NEW = [
    w("invero", "invero", "en verdad", "Invero non è così.", "invero non e kosi", "En verdad no es así."),
    w("nonché", "nonke", "así como", "Il testo, nonché la nota.", "il testo, nonke la nota", "El texto, así como la nota."),
    w("anzitutto", "antsituto", "ante todo", "Anzitutto, chiariamo.", "antsituto, kiariamo", "Ante todo, aclaremos."),
    w("fuorviante", "fuorviante", "engañoso", "Il titolo è fuorviante.", "il titolo e fuorviante", "El título es engañoso."),
    w("capzioso", "kapsioso", "capcioso", "Un argomento capzioso.", "un argomento kapsioso", "Un argumento capcioso."),
    w("stringato", "stringato", "escueto", "Uno stile stringato.", "uno stile stringato", "Un estilo escueto."),
    w("ampolloso", "ampoloso", "ampuloso", "Uno stile ampolloso.", "uno stile ampoloso", "Un estilo ampuloso."),
    w("sobrio", "sobrio", "sobrio", "Un tono sobrio.", "un tono sobrio", "Un tono sobrio."),
    w("solenne", "solene", "solemne", "Un tono solenne.", "un tono solene", "Un tono solemne."),
    w("dimesso", "dimesso", "apagado", "Uno stile dimesso.", "uno stile dimesso", "Un estilo apagado."),
    w("ricercato", "richerkato", "rebuscado", "Un lessico ricercato.", "un lesiko richerkato", "Un léxico rebuscado."),
    w("pungente", "punyente", "punzante", "Un'ironia pungente.", "unironia punyente", "Una ironía punzante."),
    w("blando", "blando", "blando", "Un giudizio blando.", "un yuditsio blando", "Un juicio blando."),
    w("tagliente", "taliente", "cortante", "Una replica tagliente.", "una replika taliente", "Una réplica cortante."),
    w("allusivo", "alusivo", "alusivo", "Un tono allusivo.", "un tono alusivo", "Un tono alusivo."),
    w("ellittico", "elitiko", "elíptico", "Uno stile ellittico.", "uno stile elitiko", "Un estilo elíptico."),
    w("iperbole", "iperbole", "hipérbole", "È un'iperbole.", "e uniperbole", "Es una hipérbole."),
    w("sineddoche", "sinedoke", "sinécdoque", "«Vela» per nave è una sineddoche.", "vela per nave e una sinedoke", "«Vela» por barco es una sinécdoque."),
    w("metonimia", "metonimia", "metonimia", "È una metonimia.", "e una metonimia", "Es una metonimia."),
    w("antitesi", "antitezi", "antítesis", "L'antitesi è netta.", "lantitezi e neta", "La antítesis es neta."),
    w("chiasmo", "kiasmo", "quiasmo", "La frase ha un chiasmo.", "la frase a un kiasmo", "La frase tiene un quiasmo."),
    w("anacoluto", "anakoluto", "anacoluto", "Qui c'è un anacoluto.", "kui che un anakoluto", "Acá hay un anacoluto."),
    w("ellissi", "elisi", "elipsis", "L'ellissi è voluta.", "lelisi e voluta", "La elipsis es deliberada."),
    w("paradosso", "paradoso", "paradoja", "Sembra un paradosso.", "sembra un paradoso", "Parece una paradoja."),
    w("sarcasmo", "sarkasmo", "sarcasmo", "Il sarcasmo è pesante.", "il sarkasmo e pesante", "El sarcasmo es pesado."),
    w("neologismo", "neoloyismo", "neologismo", "È un neologismo.", "e un neoloyismo", "Es un neologismo."),
    w("arcaismo", "arkaismo", "arcaísmo", "È un arcaismo.", "e un arkaismo", "Es un arcaísmo."),
    w("regionalismo", "reyionalismo", "regionalismo", "È un regionalismo.", "e un reyionalismo", "Es un regionalismo."),
    w("calco", "kalko", "calco", "È un calco dallo spagnolo.", "e un kalko dalo spañolo", "Es un calco del español."),
    w("prestito", "prestito", "préstamo lingüístico", "È un prestito dall'inglese.", "e un prestito dalinglese", "Es un préstamo del inglés."),
    w("norma", "norma", "norma", "Rispetta la norma.", "rispeta la norma", "Respetá la norma."),
    w("deviazione", "deviatsione", "desvío", "È una deviazione voluta.", "e una deviatsione voluta", "Es un desvío deliberado."),
    w("variante", "variante", "variante", "È una variante regionale.", "e una variante reyionale", "Es una variante regional."),
    w("idiomatico", "idiomatiko", "idiomático", "Un uso idiomatico.", "un uso idiomatiko", "Un uso idiomático."),
    w("figurato", "figurato", "figurado", "In senso figurato.", "in senso figurato", "En sentido figurado."),
    w("prosa", "prosa", "prosa", "Una prosa limpida.", "una prosa limpida", "Una prosa límpida."),
    w("verso", "verso", "verso", "Il verso è lungo.", "il verso e lungo", "El verso es largo."),
    w("strofa", "strofa", "estrofa", "La strofa chiude.", "la strofa kiude", "La estrofa cierra."),
    w("marca", "marka", "marca", "È una marca di registro.", "e una marka di registro", "Es una marca de registro."),
    w("standard", "standard", "estándar", "L'italiano standard.", "litaliano standard", "El italiano estándar."),
    w("limpido", "limpido", "límpido", "Un ragionamento limpido.", "un rayonamento limpido", "Un razonamiento límpido."),
    w("lambiccato", "lambikato", "rebuscado", "Uno stile lambiccato.", "uno stile lambikato", "Un estilo rebuscado."),
    w("icasticità", "ikastichitá", "fuerza expresiva", "Ha icasticità.", "a ikastichitá", "Tiene fuerza expresiva."),
    w("pregnanza", "preñantsa", "densidad de sentido", "La pregnanza dell'immagine.", "la preñantsa delimayine", "La densidad de la imagen."),
    w("sfumato", "sfumato", "matizado", "Un confine sfumato.", "un konfine sfumato", "Un límite matizado."),
    w("perentorietà", "perentorietá", "tono tajante", "La perentorietà infastidisce.", "la perentorietá infastidishe", "Lo tajante molesta."),
    w("understatement", "anderstatement", "atenuación", "È un understatement.", "e un anderstatement", "Es una atenuación."),
]

B1_EXTRA = [
    w("sintomo", "sintomo", "síntoma", "Qual è il sintomo?", "kual e il sintomo", "¿Cuál es el síntoma?"),
    w("ricovero", "rikovero", "internación", "Serve un ricovero.", "serve un rikovero", "Hace falta una internación."),
    w("ambulanza", "ambulantsa", "ambulancia", "Chiama l'ambulanza.", "kiama lambulantsa", "Llamá a la ambulancia."),
    w("analisi", "analisi", "análisis", "Domani ho le analisi.", "domani o le analisi", "Mañana tengo los análisis."),
    w("referto", "referto", "informe médico", "Il referto è pronto.", "il referto e pronto", "El informe está listo."),
    w("prescrizione", "preskritsione", "receta médica", "Leggi la prescrizione.", "leyi la preskritsione", "Leé la receta."),
]


def _num(specs):
    out = []
    for i, spec in enumerate(specs, 1):
        item = L(spec["title"], spec["summary"], spec["body"], spec["pins"], spec.get("dialogue"), spec.get("quiz"))
        item["number"] = i
        out.append(item)
    return out


A2_LESSONS = _num([
    {"title": "La casa", "summary": "Habitaciones, muebles y el alquiler.", "body": ["En A1 viste casa y porta. Acá se entra: cucina, bagno, camera, letto, y lo que hay adentro.", "Il divano, la lampada, lo specchio y l'armadio. L'affitto se dice cada mes. La chiave abre la porta."], "pins": ["cucina", "bagno", "camera", "letto", "finestra", "porta", "chiave", "tavolo", "sedia", "affitto", "armadio", "divano", "specchio", "lampada"]},
    {"title": "El edificio", "summary": "Piso, ascensor, consorcio y facturas.", "body": ["El edificio tiene piano, ascensore, cortile y balcone. El condomino es quien vive ahí.", "Il condominio se reúne. El citofono avisa. Riscaldamento y bolletta llegan juntos. Si algo se rompe, sirve una riparazione. Rumore y silenzioso describen el barrio."], "pins": ["rumore", "silenzioso", "condomino", "ascensore", "piano", "cortile", "condominio", "citofono", "balcone", "riscaldamento", "bolletta", "riparazione"]},
    {"title": "El día", "summary": "De la alarma al horario, con siempre, nunca y a menudo.", "body": ["La sveglia abre el día. Colazione, pranzo y el pomeriggio parten la jornada. Presto y tardi dicen cuándo.", "Sempre, spesso y mai miden la costumbre. Stasera cierra el plan. L'orario y l'abitudine ordenan la semana."], "pins": ["presto", "tardi", "sempre", "spesso", "mai", "stasera", "orario", "sveglia", "colazione", "pranzo", "pomeriggio", "abitudine"]},
    {"title": "El trabajo", "summary": "Oficina, jefe, sueldo y horas extra.", "body": ["Ufficio, collega y capo arman el día laboral. Lo stipendio llega, las ferie se piden con un permesso.", "La pausa corta el compito. El computer y el messaggio son el canal. Occupato avisa que no podés. Lo straordinario alarga la jornada."], "pins": ["ufficio", "collega", "stipendio", "ferie", "capo", "pausa", "compito", "computer", "straordinario", "occupato", "messaggio", "permesso"]},
    {"title": "La ropa", "summary": "Lo que te ponés, del pantalón a la bufanda.", "body": ["Maglia, vestito, scarpe y cappello ya alcanzan para entrar a un negocio. Sumá pantaloni, giacca y gonna.", "Calze, occhiali, cintura y sciarpa cierran el look. Il costume es la malla."], "pins": ["maglia", "scarpe", "cappello", "vestito", "pantaloni", "giacca", "gonna", "calze", "occhiali", "cintura", "sciarpa", "costume"]},
    {"title": "El cuerpo", "summary": "Dónde duele y a quién se lo decís.", "body": ["Occhio ya estaba. Testa, mano, bocca, dente, stomaco, schiena y gola nombran el resto.", "Il dolore se dice con mi fa male. Il dottore y la medicina están en la farmacia."], "pins": ["occhio", "dottore", "medicina", "testa", "mano", "bocca", "dente", "stomaco", "schiena", "dolore", "farmacia", "gola"]},
    {"title": "El pasado próximo", "summary": "Ho y sono más el participio.", "body": ["Con avere: ho mangiato, ho visto, ho fatto, ho detto, ho preso, ho bevuto, ho dormito.", "Con essere, el participio concuerda: sono andato, sono uscita, sono tornato, è arrivato, è partito. El auxiliar no se elige al azar: el movimiento y el cambio de estado suelen ir con essere."], "pins": ["mangiato", "andato", "visto", "fatto", "detto", "preso", "bevuto", "dormito", "uscito", "tornato", "arrivato", "partito"]},
    {"title": "Moverse", "summary": "Subte, tren, taxi y la demora.", "body": ["Metropolitana, aeroporto y valigia cubren el viaje largo. Taxi, fermata y binario cubren el corto.", "Il ritardo y la coincidenza explican por qué llegás tarde. Mappa, ponte, centro y museo orientan cuando ya bajaste."], "pins": ["metropolitana", "aeroporto", "valigia", "taxi", "fermata", "binario", "ritardo", "coincidenza", "mappa", "ponte", "centro", "museo"]},
    {"title": "El mercado", "summary": "Puesto, kilo, caja y el vuelto.", "body": ["Il mercato abre temprano. El banco es el puesto. Pedís un chilo y lo pesan en la bilancia.", "Pagás alla cassa. El resto es el vuelto. Scontrino, busta y offerta cierran la compra. Fresco elogia. Prenotare reserva la mesa, no el kilo."], "pins": ["mercato", "prenotare", "banco", "chilo", "cassa", "resto", "scontrino", "busta", "offerta", "fresco", "bilancia", "cesto"]},
    {"title": "Gustos", "summary": "Me encanta, lo detesto, demasiado y bastante.", "body": ["Preferire ya arma la elección. Adorare sube y detestare baja.", "Abbastanza, troppo, poco y molto gradúan. Sapore, salato, dolce y amaro describen el plato. Goloso confiesa el vicio."], "pins": ["preferire", "adorare", "detestare", "abbastanza", "troppo", "poco", "molto", "sapore", "goloso", "salato", "dolce", "amaro"]},
    {"title": "Tiempo libre", "summary": "Deporte, música y una salida.", "body": ["Sport y palestra son el cuerpo. Nuotare, ballare y suonare son hacer.", "Film y concerto son la salida. L'invito llega, la partita tiene squadra. L'hobby gusta. La noia avisa que el plan falló."], "pins": ["sport", "palestra", "nuotare", "ballare", "suonare", "film", "concerto", "invito", "partita", "squadra", "hobby", "noia"]},
    {"title": "El fin de semana", "summary": "Campo, lago y una excursión en auto.", "body": ["La gita sale el domingo. Campagna, lago y montagna son el destino. El picnic va en el zaino.", "Il sentiero sube hasta el panorama. Tramonto y alba marcan la luz. La macchina pide benzina.", "Proponé con andiamo y cerrá con ci vediamo."], "pins": ["gita", "campagna", "lago", "montagna", "picnic", "sentiero", "panorama", "tramonto", "alba", "zaino", "macchina", "benzina"], "dialogue": [
        {"zh": "Domenica facciamo una gita?", "py": "domenika fachamo una yita", "es": "¿El domingo hacemos una excursión?"},
        {"zh": "Sì, in montagna. Porto lo zaino.", "py": "si, in montaña. porto lo tsaino", "es": "Sí, a la montaña. Llevo la mochila."},
        {"zh": "Prendiamo la macchina?", "py": "prendiamo la makina", "es": "¿Llevamos el auto?"},
        {"zh": "Sì, ma manca la benzina.", "py": "si, ma manka la bentsina", "es": "Sí, pero falta nafta."},
        {"zh": "Allora passo io. Ci vediamo all'alba.", "py": "alora paso io. chi vediamo alalba", "es": "Entonces paso yo. Nos vemos al amanecer."},
    ], "quiz": [
        {"prompt": "Lo zaino es…", "options": ["la mochila", "el ascensor", "el sueldo", "el vuelto"], "correct": 0},
        {"prompt": "Manca la benzina quiere decir…", "options": ["falta nafta", "falta pan", "está cerrado", "llegué tarde"], "correct": 0},
        {"prompt": "La gita es…", "options": ["una excursión", "una factura", "un dolor", "un permiso"], "correct": 0},
        {"prompt": "Il tramonto es…", "options": ["el atardecer", "el desayuno", "el andén", "el jefe"], "correct": 0},
        {"prompt": "In montagna significa…", "options": ["a la montaña", "en la oficina", "en la caja", "en ayunas"], "correct": 0},
    ]},
])

B1_LESSONS = _num([
    {"title": "Unir ideas", "summary": "Pero, así que, mientras y ojalá.", "body": ["Però frena. Quindi concluye. Mentre superpone. Appena marca el instante.", "Allora retoma. Invece contrasta. Poi ordena. Intanto, anzi, oppure, magari y ecco afinan la frase."], "pins": ["però", "quindi", "mentre", "appena", "allora", "invece", "poi", "intanto", "anzi", "oppure", "magari", "ecco"]},
    {"title": "El viaje", "summary": "Hostel, guía, aduana y el seguro.", "body": ["Il viaggio y l'esperienza se cuentan al volver. L'ospite duerme en casa. La prenotazione confirma.", "Ostello, guida y souvenir son el viaje corto. Cambio, frontiera, imbarco, dogana y assicurazione son el cruce."], "pins": ["viaggio", "esperienza", "ospite", "prenotazione", "ostello", "guida", "souvenir", "cambio", "frontiera", "imbarco", "dogana", "assicurazione"]},
    {"title": "Cuando algo falla", "summary": "Daño, culpa, queja y reembolso.", "body": ["Il problema pide una soluzione. Decidere no se posterga si es urgente.", "Guasto y danno nombran el desperfecto. La colpa no siempre es tuya. La lamentela y el rimborso se piden con pazienza."], "pins": ["problema", "soluzione", "decidere", "guasto", "danno", "colpa", "lamentela", "rimborso", "urgente", "pazienza"]},
    {"title": "El proyecto", "summary": "Reunión, plazo, rol y resultado.", "body": ["Riunione, progetto y scadenza ordenan la semana laboral. L'aumento y l'obiettivo miran más arriba.", "La promozione cambia el ruolo. Carico y priorità dicen qué va primero. Delegare alivia. Il risultato entra en el bilancio."], "pins": ["riunione", "progetto", "scadenza", "aumento", "obiettivo", "promozione", "ruolo", "carico", "priorità", "delegare", "risultato", "bilancio"]},
    {"title": "En la cocina", "summary": "Receta, alergia y los verbos del fuego.", "body": ["Ricetta, ingrediente y allergia ya evitan un mal plato.", "Forno, pentola y padella son los útiles. Bollire, friggere y mescolare son el gesto. Porzione y spezia cierran."], "pins": ["ricetta", "ingrediente", "allergia", "forno", "pentola", "padella", "bollire", "friggere", "mescolare", "porzione", "spezia"]},
    {"title": "Salud", "summary": "Fiebre, turno, análisis y la receta.", "body": ["Salute se brinda y se cuida. Febbre y tosse son el aviso. El sintomo se describe en el turno: l'appuntamento.", "Si hace falta, llaman l'ambulanza o hay un ricovero. Las analisi dan un referto. La prescrizione es la receta que te llevás."], "pins": ["salute", "febbre", "tosse", "appuntamento", "sintomo", "ricovero", "ambulanza", "analisi", "referto", "prescrizione"]},
    {"title": "El ambiente", "summary": "Basura, plástico y la sequía.", "body": ["Ambiente, inquinamento, riciclare y risparmiare arman la base.", "Rifiuti, plastica, vetro y raccolta son el día a día. Spreco y energia se miden. Siccità y alluvione son el clima cuando se pasa de largo."], "pins": ["ambiente", "inquinamento", "riciclare", "risparmiare", "rifiuti", "plastica", "vetro", "raccolta", "spreco", "energia", "siccità", "alluvione"]},
    {"title": "Verbos de decisión", "summary": "Esperar, parecer, lograr, olvidar.", "body": ["Sperare desea. Sembrare opina. Diventare cambia de estado. Riuscire logra. Dimenticare pierde y ricordare recupera.", "Promettere ata. Scegliere corta. Evitare esquiva. Consigliare recomienda. Permettere abre y vietare cierra."], "pins": ["sperare", "sembrare", "diventare", "riuscire", "dimenticare", "ricordare", "promettere", "scegliere", "evitare", "consigliare", "permettere", "vietare"]},
    {"title": "La opinión", "summary": "De acuerdo, en contra y la duda.", "body": ["Opinione y cultura dan el marco. Sono d'accordo o sono contrario cierran la posición.", "Dubbio y certezza miden la seguridad. L'impressione es más blanda. Ragione y punto ordenan el argumento."], "pins": ["opinione", "cultura", "accordo", "contrario", "dubbio", "certezza", "impressione", "ragione", "punto"]},
    {"title": "Papeles", "summary": "Alquiler, multa y formulario.", "body": ["El mutuo, el inquilino y el proprietario arman el contrato de vivienda. Il deposito y le spese se pagan aparte.", "Avviso, multa, modulo, firma y documento son el mostrador."], "pins": ["mutuo", "inquilino", "proprietario", "deposito", "spese", "avviso", "multa", "modulo", "firma", "documento"]},
    {"title": "Contar lo que pasó", "summary": "De repente, al final, por suerte.", "body": ["Improvvisamente corta la calma. Nel frattempo pasa otra cosa. All'inizio y alla fine enmarcan.", "Finalmente alivia. Purtroppo y per fortuna evalúan. Raccontare pide estos marcadores para que el relato no sea una lista."], "pins": ["improvvisamente", "frattempo", "fine", "inizio", "finalmente", "purtroppo", "fortuna", "raccontare"]},
    {"title": "Un plan que cambia", "summary": "Decidir, avisar y volver a armar el día.", "body": ["Juntá un conector, un problema y un verbo de decisión. Así se cuenta un cambio de planes sin quedarse en el A2.", "Però y quindi alcanzan si el resto de la frase ya está claro."], "pins": ["però", "quindi", "problema", "decidere"], "dialogue": [
        {"zh": "Volevo venire, però ho un problema.", "py": "volevo venire, peró o un problema", "es": "Quería ir, pero tengo un problema."},
        {"zh": "Che succede?", "py": "ke suchede", "es": "¿Qué pasa?"},
        {"zh": "Il treno è in ritardo. Quindi arrivo tardi.", "py": "il treno e in ritardo. kuindi arrivo tardi", "es": "El tren está demorado. Así que llego tarde."},
        {"zh": "Non è un problema. Ti aspetto.", "py": "non e un problema. ti aspeito", "es": "No es un problema. Te espero."},
        {"zh": "Grazie. Appena arrivo ti chiamo.", "py": "gratsie. apena arrivo ti kiamo", "es": "Gracias. Apenas llego te llamo."},
    ], "quiz": [
        {"prompt": "Quindi significa…", "options": ["así que", "aunque", "nunca", "arriba"], "correct": 0},
        {"prompt": "Il rimborso es…", "options": ["el reembolso", "la fiebre", "el balcón", "el verso"], "correct": 0},
        {"prompt": "Sono d'accordo quiere decir…", "options": ["estoy de acuerdo", "estoy ocupado", "me duele", "falta nafta"], "correct": 0},
        {"prompt": "La dogana es…", "options": ["la aduana", "la sartén", "la bufanda", "el despertador"], "correct": 0},
        {"prompt": "Purtroppo se usa para…", "options": ["una mala noticia", "un brindis", "pedir la cuenta", "decir la hora"], "correct": 0},
    ]},
])

B2_LESSONS = _num([
    {"title": "Aunque y con tal de que", "summary": "Concesión, condición y el matiz de «más bien».", "body": ["Sebbene y benché piden subjuntivo: sebbene piova, esco. Nonostante y ciononostante no lo exigen. Tuttavia corrige sin negar.", "Purché pone la condición: vengo, purché sia breve. Qualora es el si formal. Piuttosto baja el tono: no es caro, es più tosto caro."], "pins": ["sebbene", "nonostante", "tuttavia", "piuttosto", "benché", "purché", "qualora", "ciononostante"]},
    {"title": "Probablemente, de hecho", "summary": "Certeza, añadido y el por lo tanto.", "body": ["Probabilmente deja la puerta abierta. Sicuramente la cierra. Addirittura sube la apuesta.", "Infatti y difatti confirman. Inoltre suma. Pertanto concluye. Ovvero reformula. Perlomeno salva un mínimo."], "pins": ["addirittura", "probabilmente", "sicuramente", "infatti", "inoltre", "pertanto", "ovvero", "difatti", "perlomeno"]},
    {"title": "Leer el diario", "summary": "Fuente, título, entrevista y redacción.", "body": ["L'argomento es el tema. La fonte se cita. L'articolo sale al giornale con un titolo.", "L'intervista da la voz. La redazione es quien cierra el texto."], "pins": ["argomento", "fonte", "articolo", "giornale", "titolo", "intervista", "redazione"]},
    {"title": "La noticia", "summary": "Crónica, investigación y el título inflado.", "body": ["La cronaca cuenta el hecho. L'editoriale opina. L'inchiesta investiga y el testimone declara.", "La notizia informa. La bufala miente. El titolone grita más de lo que el texto sostiene."], "pins": ["cronaca", "editoriale", "inchiesta", "testimone", "notizia", "bufala", "titolone"]},
    {"title": "La economía", "summary": "Inflación, desempleo, PBI y el sueldo.", "body": ["L'economia se lee en la inflazione y la disoccupazione. Il pil resume el país.", "Il salario es el sueldo en la nota. Il precariato es el trabajo inestable. Le tasse son los impuestos."], "pins": ["economia", "inflazione", "disoccupazione", "pil", "salario", "precariato", "tasse"]},
    {"title": "El contrato", "summary": "Cláusula, negociación y el currículum.", "body": ["Il contratto se firma. La clausola se lee antes. La trattativa es la mesa. La strategia es el plan.", "La competenza se muestra en el colloquio. El curriculum se adjunta. Affidabile es el adjetivo que buscás que te pongan."], "pins": ["contratto", "clausola", "trattativa", "strategia", "competenza", "colloquio", "curriculum", "affidabile"]},
    {"title": "El conflicto laboral", "summary": "Sindicato, huelga, despido y la firma.", "body": ["El feedback se pide. Firmare y allegare cierran el trámite. Rallentare describe el freno.", "L'assunzione entra. Il licenziamento sale. Il sindacato convoca lo sciopero."], "pins": ["feedback", "firmare", "allegare", "rallentare", "assunzione", "licenziamento", "sindacato", "sciopero"]},
    {"title": "La política", "summary": "Voto, parlamento, decreto y mayoría.", "body": ["La società cambia cuando il cittadino vota. Il voto es secreto. L'elezione tiene fecha.", "Parlamento y governo deciden. L'opposizione discute. Legge y decreto no son lo mismo. Il referendum consulta. Maggioranza y minoranza cuentan los votos."], "pins": ["società", "cittadino", "voto", "elezione", "parlamento", "governo", "opposizione", "legge", "decreto", "referendum", "maggioranza", "minoranza"]},
    {"title": "El mail formal", "summary": "Condicional, cortesía y el adjunto.", "body": ["El condizionale pide: vorrei. El congiuntivo entra en las subordinadas formales. La cortesia se nota en el tono, no en los adjetivos vacíos.", "La richiesta tiene un oggetto. El allegato va nombrado. Distinti saluti cierra. Spettabile abre a una empresa. Il sollecito es el segundo mail, cuando no contestaron. Il diritto nombra lo que corresponde."], "pins": ["condizionale", "congiuntivo", "cortesia", "richiesta", "allegato", "oggetto", "distinti", "spettabile", "sollecito", "diritto"]},
    {"title": "Cultura", "summary": "Muestra, novela, escenario y reseña.", "body": ["La mostra se visita. Il romanzo se lee. L'autore firma. Il pubblico aplaude o se va.", "La recensione juzga. Palcoscenico, copione, trama y personaggio arman la obra."], "pins": ["mostra", "romanzo", "autore", "pubblico", "recensione", "palcoscenico", "copione", "trama", "personaggio"]},
    {"title": "La sociedad", "summary": "Brecha, salud, vivienda y prejuicio.", "body": ["Il divario y la disuguaglianza miden la distancia. Welfare, sanità, istruzione y pensioni son la red.", "L'alloggio es la vivienda. L'integrazione se discute. Pregiudizio y stereotipo son el atajo que el texto serio evita."], "pins": ["divario", "disuguaglianza", "welfare", "sanità", "istruzione", "pensioni", "alloggio", "integrazione", "pregiudizio", "stereotipo"]},
    {"title": "La objeción", "summary": "Ventaja, límite y un acuerdo que no es rendición.", "body": ["La sfida abre. L'opportunità tienta. Il limite frena. Vantaggio y svantaggio se ponen en la misma frase.", "L'equilibrio se busca. Il compromesso no es derrota. La proposta se escucha. L'obiezione se responde."], "pins": ["sfida", "opportunità", "limite", "vantaggio", "svantaggio", "equilibrio", "compromesso", "proposta", "obiezione"], "dialogue": [
        {"zh": "La proposta è interessante, tuttavia ho un'obiezione.", "py": "la proposta e interesante, tuttavia o unobiezione", "es": "La propuesta es interesante, sin embargo tengo una objeción."},
        {"zh": "Quale?", "py": "kuale", "es": "¿Cuál?"},
        {"zh": "Il vantaggio è chiaro, ma c'è un limite di tempo.", "py": "il vantayo e kiaro, ma che un limite di tempo", "es": "La ventaja es clara, pero hay un límite de tiempo."},
        {"zh": "Cerchiamo un compromesso.", "py": "cherkiamo un kompromeso", "es": "Busquemos un acuerdo."},
        {"zh": "D'accordo, purché sia scritto.", "py": "dakordo, purke sia skrito", "es": "De acuerdo, con tal de que quede por escrito."},
    ], "quiz": [
        {"prompt": "Tuttavia significa…", "options": ["sin embargo", "por favor", "nunca", "arriba"], "correct": 0},
        {"prompt": "Lo sciopero es…", "options": ["la huelga", "el título", "el escenario", "el impuesto"], "correct": 0},
        {"prompt": "Purché introduce…", "options": ["una condición", "un saludo", "una hora", "un color"], "correct": 0},
        {"prompt": "Il titolone es…", "options": ["un título inflado", "un sindicato", "un contrato", "un verso"], "correct": 0},
        {"prompt": "Allegare quiere decir…", "options": ["adjuntar", "votar", "ahorrar", "toser"], "correct": 0},
    ]},
])

C1_LESSONS = _num([
    {"title": "Registro y matiz", "summary": "Implícito, irónico, sutil y demasiado largo.", "body": ["La sfumatura es el matiz. Il registro dice si el texto es formal o no. Implicito se infiere. Esplicito se dice.", "Il tono puede ser de ironia o sarcastico. La metafora no se lee al pie de la letra: letterale es otra cosa. Sottile casi no se ve. Prolisso sobra. Conciso alcanza."], "pins": ["sfumatura", "registro", "implicito", "esplicito", "tono", "ironia", "metafora", "sottile", "sarcastico", "letterale", "prolisso", "conciso"]},
    {"title": "El argumento", "summary": "Premisa, hipótesis, contradicción y tesis.", "body": ["Il presupposto se da por sentado. Si es falso, cae todo. La premessa se enuncia. L'ipotesi se pone a prueba. La tesi se sostiene.", "Coerenza mantiene el hilo. La contraddizione lo corta. L'ambiguità lo nubla. La conclusione cierra, y si llega antes de tiempo se nota."], "pins": ["presupposto", "coerenza", "contraddizione", "ambiguità", "premessa", "conclusione", "ipotesi", "tesi"]},
    {"title": "Método", "summary": "Criterio, contexto y la muestra.", "body": ["La verifica comprueba. Il criterio justifica la elección. La metodologia se puede repetir.", "Il contesto cambia el sentido. La prospettiva es desde dónde se mira. Il campione es la muestra, no el ganador."], "pins": ["verifica", "criterio", "metodologia", "contesto", "prospettiva", "campione"]},
    {"title": "Los datos", "summary": "Porcentaje, variable y encuesta.", "body": ["La statistica no habla sola. La percentuale sube o baja. La variabile es lo que se mueve.", "La correlazione no es causa. Il sondaggio pregunta, y la fecha importa."], "pins": ["statistica", "percentuale", "variabile", "correlazione", "sondaggio"]},
    {"title": "Qué está pasando", "summary": "Tendencia, fenómeno, riesgo y juicio.", "body": ["La tendenza se observa en el tiempo. Il fenomeno se describe. La conseguenza se acepta o se discute.", "Recente ubica el hecho. Il rischio se nombra. Il giudizio se puede suspender."], "pins": ["tendenza", "fenomeno", "conseguenza", "recente", "rischio", "giudizio"]},
    {"title": "Verbos del debate", "summary": "Argumentar, refutar, precisar y atenuar.", "body": ["Argomentare construye. Confutare desmonta. Sostenere mantiene una posición, incluso la contraria.", "Precisare achica el blanco. Attenuare baja el juicio. Enfatizzare sube el riesgo."], "pins": ["argomentare", "confutare", "sostenere", "precisare", "attenuare", "enfatizzare"]},
    {"title": "El texto", "summary": "Borrador, ensayo, cita y párrafo.", "body": ["Formalizzare deja por escrito. Adeguare el tono al lector. Approfondire es ir más adentro, no alargar.", "La bozza se manda. La revisione la corrige. La sintesi achica. Il saggio argumenta. Il paragrafo se lee. La citazione se atribuye."], "pins": ["formalizzare", "adeguare", "approfondire", "bozza", "revisione", "sintesi", "saggio", "paragrafo", "citazione"]},
    {"title": "El derecho", "summary": "Norma, recurso, sentencia y mediación.", "body": ["La normativa manda. El ricorso se presenta. La sentenza cierra. Il tribunale decide. L'avvocato representa.", "La mediazione busca una salida. Il negoziato sigue mientras haya margen."], "pins": ["normativa", "ricorso", "sentenza", "tribunale", "avvocato", "mediazione", "negoziato"]},
    {"title": "Tecnología", "summary": "Algoritmo, plataforma, privacidad y patente.", "body": ["L'algoritmo decide sin explicar, y a veces se equivoca. La piattaforma es el lugar. La privacy es el límite.", "Il brevetto protege. L'innovazione cuesta y se vende."], "pins": ["algoritmo", "piattaforma", "privacy", "brevetto", "innovazione"]},
    {"title": "Ética", "summary": "Dilema, principio y responsabilidad.", "body": ["L'etica pregunta qué corresponde. Il dilemma no tiene una salida limpia. Il principio no se negocia fácil.", "La responsabilità tiene un sujeto. Empatia y resilienza no reemplazan el argumento. La consapevolezza es darse cuenta."], "pins": ["etica", "dilemma", "principio", "responsabilità", "empatia", "resilienza", "consapevolezza"]},
    {"title": "Claridad", "summary": "Eficaz, oscuro, índice y bibliografía.", "body": ["Efficace logra el efecto. Oscuro obliga a releer. Trasparente se puede seguir.", "La bibliografia y la nota sostienen. Il capitolo ordena. L'indice orienta."], "pins": ["efficace", "oscuro", "trasparente", "bibliografia", "nota", "capitolo", "indice"]},
    {"title": "El debate", "summary": "Consenso, disenso y la réplica.", "body": ["Il dibattito se modera. Il moderatore da la palabra. L'intervento es breve. La replica responde.", "Il consenso se construye. Il dissenso se expresa. Diplomazia, trattato y sanzione son el mismo gesto en grande: hablar, firmar, o cortar."], "pins": ["dibattito", "moderatore", "intervento", "replica", "consenso", "dissenso", "diplomazia", "trattato", "sanzione"], "dialogue": [
        {"zh": "La tesi non regge: c'è una contraddizione.", "py": "la tezi non reye: che una kontraditsione", "es": "La tesis no se sostiene: hay una contradicción."},
        {"zh": "Preciso. Era un'ipotesi, non una conclusione.", "py": "prechiso. era unipotesi, non una konklusione", "es": "Preciso. Era una hipótesis, no una conclusión."},
        {"zh": "Allora manca la verifica.", "py": "alora manka la verifika", "es": "Entonces falta la verificación."},
        {"zh": "D'accordo. La facciamo prima del dibattito.", "py": "dakordo. la fachamo prima del dibattito", "es": "De acuerdo. La hacemos antes del debate."},
        {"zh": "Il moderatore dà la parola.", "py": "il moderatore da la parola", "es": "El moderador da la palabra."},
    ], "quiz": [
        {"prompt": "Confutare significa…", "options": ["refutar", "citar", "firmar", "ahorrar"], "correct": 0},
        {"prompt": "La bozza es…", "options": ["el borrador", "la sentencia", "la encuesta", "el índice"], "correct": 0},
        {"prompt": "Implicito quiere decir…", "options": ["implícito", "reciente", "tajante", "literal"], "correct": 0},
        {"prompt": "Il ricorso se presenta ante…", "options": ["un tribunal", "una receta", "un andén", "un mercado"], "correct": 0},
        {"prompt": "La sintesi es…", "options": ["una síntesis", "una huelga", "una bufanda", "un alquiler"], "correct": 0},
    ]},
])

C2_LESSONS = _num([
    {"title": "Conectores de registro alto", "summary": "No obstante, o sea, sino y ante todo.", "body": ["Nondimeno no niega: suma una reserva. Ossia reformula. Pressoché casi cierra la puerta. Bensì corrige: no es pereza, sino cautela.", "Quantunque concede en registro alto. Tuttora dice que sigue. Oramai marca que ya es tarde para otra cosa. Invero afirma. Nonché suma un segundo término. Anzitutto ordena el primero."], "pins": ["nondimeno", "ossia", "pressoché", "bensì", "quantunque", "tuttora", "oramai", "invero", "nonché", "anzitutto"]},
    {"title": "Matizar el sentido", "summary": "Dar a entender, reforzar y la densidad.", "body": ["Sfumare desdibuja el límite. Sottintendere no lo dice. Palesare lo deja a la vista. Avvalorare refuerza la tesis con datos.", "Ridondante sobra. Pregnante carga sentido. Perentorio no admite réplica. Forbito está pulido. Icasticità, pregnanza y perentorietà nombran esas cualidades."], "pins": ["sfumare", "sottintendere", "palesare", "avvalorare", "ridondante", "pregnante", "perentorio", "forbito", "icasticità", "pregnanza", "perentorietà"]},
    {"title": "El registro", "summary": "Coloquial, áulico, descuidado y solemne.", "body": ["Colloquiale baja. Aulico sube. Sciatto se descuida. Pedante corrige de más. Cristallino se entiende de una. Sfuggente esquiva. Lapidario cierra en una frase.", "Sobrio no adorna. Solenne pesa. Dimesso se apaga. Stringato es escueto. Ampolloso se infla."], "pins": ["colloquiale", "aulico", "sciatto", "pedante", "cristallino", "sfuggente", "lapidario", "sobrio", "solenne", "dimesso", "stringato", "ampolloso"]},
    {"title": "El tono", "summary": "Capcioso, punzante, límpido y rebuscado.", "body": ["Fuorviante desvía. Capzioso atrapa en la forma. Ricercato elige de más. Pungente pincha. Blando no corta. Tagliente sí.", "Allusivo no nombra. Ellittico salta. Limpido se sigue. Lambiccato se enreda."], "pins": ["fuorviante", "capzioso", "ricercato", "pungente", "blando", "tagliente", "allusivo", "ellittico", "limpido", "lambiccato"]},
    {"title": "Figuras", "summary": "Lítote, oxímoron, hipérbole y quiasmo.", "body": ["El eufemismo tapa. La litote niega lo contrario: non male. El ossimoro junta opuestos. El pleonasmo repite.", "Iperbole exagera. Sineddoche toma la parte. Metonimia toma lo contiguo. Antitesi opone. Chiasmo cruza. Anacoluto rompe la sintaxis. Ellissi omite. Paradosso parece imposible y se sostiene."], "pins": ["eufemismo", "litote", "ossimoro", "pleonasmo", "iperbole", "sineddoche", "metonimia", "antitesi", "chiasmo", "anacoluto", "ellissi", "paradosso"]},
    {"title": "Ironía y atenuación", "summary": "Sarcasmo, lítote inglesa y el límite matizado.", "body": ["Il sarcasmo pesa. El understatement dice menos de lo que hay. Sfumato deja el borde sin línea.", "No hace falta un adjetivo más si la figura ya hizo el trabajo."], "pins": ["sarcasmo", "understatement", "sfumato"]},
    {"title": "De dónde viene la palabra", "summary": "Neologismo, arcaísmo, calco y préstamo.", "body": ["Il lessico se elige. La connotazione carga valor. La denotazione se queda en el diccionario.", "Neologismo acaba de llegar. Arcaismo se quedó. Regionalismo marca el lugar. Calco traduce la estructura. Prestito toma la palabra. Idiomatico no se traduce pieza por pieza. Figurato no es el sentido recto."], "pins": ["lessico", "connotazione", "denotazione", "neologismo", "arcaismo", "regionalismo", "calco", "prestito", "idiomatico", "figurato"]},
    {"title": "Norma y variante", "summary": "Estándar, desvío y marca de registro.", "body": ["La norma es el uso que se enseña. La deviazione puede ser un error o una elección. La variante convive.", "Standard nombra el italiano de referencia. La marca avisa el registro antes de que el lector se confunda."], "pins": ["norma", "deviazione", "variante", "standard", "marca"]},
    {"title": "Prosa y verso", "summary": "Estrofa, malestar y cautela.", "body": ["La prosa avanza. Il verso mide. La strofa agrupa.", "Il disagio se percibe sin que el texto lo grite. La cautela es no cerrar antes de tiempo."], "pins": ["prosa", "verso", "strofa", "disagio", "cautela"]},
    {"title": "El razonamiento", "summary": "Límite lábil y silencio ensordecedor.", "body": ["Il ragionamento se sostiene o no. Il confine puede ser labile: se corre.", "Assordante, puesto junto a silencio, arma el oxímoron que ya viste. Acá el trabajo es reconocerlo, no solo traducirlo."], "pins": ["ragionamento", "confine", "labile", "assordante"]},
    {"title": "Leer el efecto", "summary": "Qué hace la frase, no solo qué dice.", "body": ["Una frase forbita puede ser vacía. Una colloquiale puede ser precisa. El nivel C2 se juega en ese juicio.", "Preguntate: ¿atenúa, exagera, da a entender o cierra? El nombre de la figura viene después."], "pins": ["forbito", "colloquiale", "sfumare"]},
    {"title": "Una frase que se sostiene", "summary": "Elegir el conector y no adornar de más.", "body": ["Nondimeno no es però con otra ropa si no cambia el peso de la frase. Bensì corrige. Ossia aclara.", "Si el adjetivo no cambia el sentido, sobra. Eso es ridondante."], "pins": ["nondimeno", "bensì", "ossia", "ridondante"], "dialogue": [
        {"zh": "Il tono è perentorio, nondimeno il ragionamento regge.", "py": "il tono e perentorio, nondimeno il rayonamento reye", "es": "El tono es tajante, no obstante el razonamiento se sostiene."},
        {"zh": "È forbito, ossia curato, ma un po' ridondante.", "py": "e forbito, osia kurato, ma un po ridondante", "es": "Está pulido, o sea cuidado, pero un poco redundante."},
        {"zh": "Non è pigrizia, bensì cautela.", "py": "non e pigrizia, bensí kautela", "es": "No es pereza, sino cautela."},
        {"zh": "Il confine è labile.", "py": "il konfine e labile", "es": "El límite es lábil."},
        {"zh": "Appunto. Non va palesato tutto.", "py": "apunto. non va palesato tuto", "es": "Exacto. No hace falta dejar todo a la vista."},
    ], "quiz": [
        {"prompt": "Bensì equivale a…", "options": ["sino", "aunque", "nunca", "arriba"], "correct": 0},
        {"prompt": "Una litote es…", "options": ["negar lo contrario para atenuar", "un título de diario", "una multa", "un participio"], "correct": 0},
        {"prompt": "Pressoché significa…", "options": ["casi", "ayer", "debajo", "juntos"], "correct": 0},
        {"prompt": "Un calco es…", "options": ["una traducción de la estructura", "un ascensor", "una receta", "un andén"], "correct": 0},
        {"prompt": "Ridondante describe algo…", "options": ["redundante", "gratis", "temprano", "cerrado"], "correct": 0},
    ]},
])


def _clean(lessons):
    cleaned = []
    for item in lessons:
        cleaned.append({key: value for key, value in item.items() if value is not None})
    return cleaned


def extra_words():
    return {
        2: A2_NEW,
        3: B1_NEW + B1_EXTRA,
        4: B2_NEW,
        5: C1_NEW,
        6: C2_NEW,
    }


def extra_lessons():
    return {
        2: _clean(A2_LESSONS),
        3: _clean(B1_LESSONS),
        4: _clean(B2_LESSONS),
        5: _clean(C1_LESSONS),
        6: _clean(C2_LESSONS),
    }
