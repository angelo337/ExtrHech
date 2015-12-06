###########################################################################
#                 REGULAR EXPRESSIONS 
###########################################################################

###################################################
#   COORDINATIVE CONJUNCTIONS AND COMMA (y, o, ',')
###################################################

Y =  r'(?:\s+\w+\^\w+\^CC)'
COMMA = r'(?:\s+,\^,\^Fc)'

COORD = Y+'|(?:'+COMMA+Y+'?)'


################
#   VERB PHRASE 
################

'''
V|VP|VW*P 

V = VERB PARTICLE? ADV?
W = (NOUN|ADJ|ADV|PRON|DET)
P = (PREP|PARTICLE|INF. MARKER)
'''


#V = r'(?:\w+\^\w+\^P0000000\s+)?(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'

#takes into account dative case pronouns infront of a verb 
#V = 
#V = r'(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'
#V = r'(?:\w+\^\w+\^R[GN]\s+)?(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'
#cambio 09 julio 2013 
V = r'(?:\w+\^\w+\^R[GN]\s+)?(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VM[P|G]....))(?:\s+\w+\^\w+\^RG)?'

#V_WITH_PARTICIP = r'(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S][IP]....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'
#V_WITH_PARTICIP = r'(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S][I]....)|(?:\w+\^\w+\^V[M|S]P....\s+\w+\^\w+\^SP...)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'
V_WITH_PARTICIP = r'(?:\w+\^\w+\^R[GN]\s+)?(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S][I]....)|(?:\w+\^\w+\^V[M|S]P....\s+\w+\^\w+\^SP...)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'

#W = r'(?:\s+(?:\w+\^\w+\^N......)|(?:\w+\^\w+\^A.....)|(?:\w+\^\w+\^R.)|(?:\w+\^\w+\^P.......)|(?:\w+\^\w+\^D.....)|(?:\w+\^\w+\^VMN....(?:\s+\w+\^\w+\^PP...000)?))'
W = r'(?:(?:\s+\w+\^\w+\^N......)|(?:\s+\w+\^\w+\^A.....)|(?:\s+\w+\^\w+\^R.)|(?:\s+\w+\^\w+\^P.......)|(?:\s+\w+\^\w+\^D.....)|(?:\s+\w+\^\w+\^VMN....(?:\s+\w+\^\w+\^PP...000)?))'
#W = r'(?:\s+(?:\w+\^\w+\^N......)|(?:\w+\^\w+\^A.....)|(?:\w+\^\w+\^R.)|(?:\w+\^\w+\^P.......)|(?:\w+\^\w+\^D.....))'

#no se usa actualmente 
I = r'(?:\s+\w+\^\w+\^V.N....(?:\s+\w+\^\w+\^PP...000)?)'

#P = r'(?:\s+\w+\^\w+\^SP...)'
#P = r'(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.N....)'
#P = r'(?:(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.N....))'
#P = r'(?:(?:\s+\w+\^\w+\^SP...\s+\w+\^\w+\^V.N....)|(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.N....))'
P = r'(?:(?:\s+\w+\^\w+\^SP...\s+\w+\^\w+\^V.N....(?:(?:'+COORD+')'+I+')*)|(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.[N|G]....))'

#REGEX_REL = '('+V+'(?:\s+'+W+')*'+P+')|('+V+P+')|('+V+')'   
#REGEX_REL = '('+V+ W+'*'+P+')|('+V+P+')|('+V+')'   
#REGEX_REL = '('+V+P+')|('+V+ W+'*'+P+')|('+V+')'   
VREL = '('+V+ W+'*'+P+')|('+V+')'   


# saca bien las relaciones verbales de 1-68 COMO SON EN CORPUS_HUMANO.XLS : 
#REGEX_REL = r'((?:\w+\^\w+\^P0000000)?\s+(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^VAI....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?(?:\s+(?:\w+\^\w+\^VMN....))*)'#\s+(?:\w+\^\w+\^SP...)?)'

###################
#     NOUN PHRASE 
###################

##noun with no participle clause 
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:\w+\^\w+\^N......)(?:\s+\w+\^\w+\^A.....)?'

##noun with a participle clause 
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:\w+\^\w+\^N......)(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'

##noun or numeral 
##200^200^Z
#NUM = r'(?:\d+\^\d+\^Z)'
NUM = r'(?:\d\w+\^\d+\^Z)'

## centuries 
## siglo_V_a.C.^[s:-v]^W (?:[\w\.]+\^\[.{3, 25}\]\^W)
SIG = r'(?:[\w\.]+\^\[.{3,25}\]\^W)'

NPROP = r'(?:\s+\w+\^\w+\^NP00000)'
#NPROPS = r'(?:'+COORD+')'+NPROP

#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:(?:\w+\^\w+\^N......)|(?:\d+\^\d+\^Z))(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:\d+\^\d+\^Z)?(?:(?:\w+\^\w+\^N......)|(?:\d+\^\d+\^Z))(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'

#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?(?:\s+\w+\^\w+\^A.....)*'
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......(?:'+NPROP+'(?:'+NPROPS+')*)?)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?(?:\s+\w+\^\w+\^A.....)*'
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......'+NPROP+'?)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?(?:(?:\s+\w+\^\w+\^RG)?\s+\w+\^\w+\^A.....)*'
# with relative pronouns 'cual', 'cuando', etc. Added 15-aug-2013
N = r'(?:\w+\^\w+\^D[^TE]....\s+)?((?:\w+\^\w+\^A.....\s+)|(?:\w+\^\w+\^PR0.....\s+))?'+NUM+'?(?:(?:\w+\^\w+\^N......'+NPROP+'?)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?(?:(?:\s+\w+\^\w+\^RG)?\s+\w+\^\w+\^A.....)*'

## this regex works very badly for spanish 
N_WITH_PRONOUN =  r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......)|(?:\w+\^\w+\^PP......)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'

PREP = r'(?:\s+\w+\^\w+\^SP...\s+'+N+')' 

#PARTICIP = r'(?:\s+\w+\^\w+\^VMP....\s+\w+\^\w+\^SP...\s+'+N+')' 
PARTICIP = r'(?:\s+\w+\^\w+\^VMP....\s+\w+\^\w+\^SP...\s+'+N+PREP+'?)' 

#NP = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^N......)(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^SP...\s+'+N+')?' 
#NP = N+r'(?:\s+\w+\^\w+\^SP...\s+'+N+')?' 
NP = N+'(?:'+PREP+'|'+PARTICIP+')?'


#########################################
#   RELATIVE PRONOUNS (que, cual, quien)
#########################################

QUE = r'(?:\s+\w+\^\w+\^PR0C....)'

















