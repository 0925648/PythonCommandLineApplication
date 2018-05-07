from random import randint

def RandomInteger():
    return randint(0, 9)

strings1 = ["Het proces ","De factor mens ","Het management ","De communicatie ","De kerncompetentie ","Human capital ","De organisatie-ontwikkeling ","De missie ","Kennismanagement ","De eerste aanzet "]
strings2 = ["moet meerwaarde leveren bij ","stelt eisen aan ","dient te faciliteren bij ","is uitgangspunt bij ","Is onlosmakelijk verbonden met ","schept voorwaarden voor ","dient te focussen op ","stuurt ","hangt nauw samen met ","moet een opstap bieden voor "]
strings3 = ["de implementatie van ","de terugkoppeling van ","het aftimmeren van ","het aansturen van ","de ontwikkeling van ","de flexibilisering van ","de integratie van ","de inventarisatie van ","de definitie van ","de insteek van "]
strings4 = ["complexe ","optimale ","in elkaar grijpende ","eenduidige ","onderling afhankelijke ","structurele ","pro-actieve ","resultaatgerichte ","efficiënte ","consistente "]
strings5 = ["supply chain processen ","business architecture ","mijlpalen ","targets ","business units ","organisatie-onderdelen ","scenario's ","best practices ","business models ","conceptplannen "]
strings6 = ["waarbij het belang van ","waarbij de feedback van ","waarbij het kader voor ","waarbij afstemming met ","waarbij de structuur van ","waarbij de synergie met ","waarbij de interface met ","waarbij input van ","waarbij commitment van ","waarbij klankborden met "]
strings7 = ["strategisch beleid ","de taskforce ","de communicatie ","de werkgroepen ","new business development ","de systeemintegratie ","de markt ","de stakeholders ","het management ","de projectorganisatie "]
strings8 = ["moet uitkristalleren.","voorop staat.","wordt aangestuurd.","leading is.","toegevoegde waarde levert.","win-win situaties kan veroorzaken.","moet worden gemanaged.","voldoende draagvlak heeft.","doorslaggevend is.","cruciaal is."]

print(strings1[RandomInteger()] + strings2[RandomInteger()] + strings3[RandomInteger()] + strings4[RandomInteger()] + strings5[RandomInteger()] + strings6[RandomInteger()] + strings7[RandomInteger()] + strings8[RandomInteger()])
