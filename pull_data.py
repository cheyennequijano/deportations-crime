
import pandas
import os
import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Preliminaries ----------------------------------------------------------------

pandas.options.display.max_columns = None
os.chdir("/Users/cheyennequijano/Desktop/grad school/nsf/")

# zipcode to city function -----------------------------------------------------

def zipcode_to_city(zipcode):
    """
    zipcode_to_city returns a zipcode's corresponding city name
    """

    zipcode_dict = {78040: "Laredo, TX", 78041: "Laredo, TX", 78042: "Laredo, TX", 78043: "Laredo, TX", 78044: "Laredo, TX", 78045: "Laredo, TX", 78046: "Laredo, TX", 

    79835: "El Paso, TX", 79901: "El Paso, TX", 79902: "El Paso, TX", 79903: "El Paso, TX", 79904: "El Paso, TX", 79905: "El Paso, TX", 79906: "El Paso, TX", 79907: "El Paso, TX", 79908: "El Paso, TX", 79910: "El Paso, TX", 79911: "El Paso, TX", 79912: "El Paso, TX", 79913: "El Paso, TX", 79914: "El Paso, TX", 79915: "El Paso, TX", 79916: "El Paso, TX", 79917: "El Paso, TX", 79918: "El Paso, TX", 79920: "El Paso, TX", 79922: "El Paso, TX", 79923: "El Paso, TX", 79924: "El Paso, TX", 79925: "El Paso, TX", 79926: "El Paso, TX", 79927: "El Paso, TX", 79928: "El Paso, TX", 79929: "El Paso, TX", 79930: "El Paso, TX", 79931: "El Paso, TX", 79932: "El Paso, TX", 79934: "El Paso, TX", 79935: "El Paso, TX", 79936: "El Paso, TX", 79937: "El Paso, TX", 79938: "El Paso, TX", 79940: "El Paso, TX", 79941: "El Paso, TX", 79942: "El Paso, TX", 79943: "El Paso, TX", 79944: "El Paso, TX", 79945: "El Paso, TX", 79946: "El Paso, TX", 79947: "El Paso, TX", 79948: "El Paso, TX", 79949: "El Paso, TX", 79950: "El Paso, TX", 79951: "El Paso, TX", 79952: "El Paso, TX", 79953: "El Paso, TX", 79954: "El Paso, TX", 79955: "El Paso, TX", 79958: "El Paso, TX", 79960: "El Paso, TX", 79961: "El Paso, TX", 79968: "El Paso, TX", 79976: "El Paso, TX", 79978: "El Paso, TX", 79980: "El Paso, TX", 79995: "El Paso, TX", 79996: "El Paso, TX", 79997: "El Paso, TX", 79998: "El Paso, TX", 79999: "El Paso, TX", 88510: "El Paso, TX", 88511: "El Paso, TX", 88512: "El Paso, TX", 88513: "El Paso, TX", 88514: "El Paso, TX", 88515: "El Paso, TX", 88517: "El Paso, TX", 88518: "El Paso, TX", 88519: "El Paso, TX", 88520: "El Paso, TX", 88521: "El Paso, TX", 88523: "El Paso, TX", 88524: "El Paso, TX", 88525: "El Paso, TX", 88526: "El Paso, TX", 88527: "El Paso, TX", 88528: "El Paso, TX", 88529: "El Paso, TX", 88530: "El Paso, TX", 88531: "El Paso, TX", 88532: "El Paso, TX", 88533: "El Paso, TX", 88534: "El Paso, TX", 88535: "El Paso, TX", 88536: "El Paso, TX", 88538: "El Paso, TX", 88539: "El Paso, TX", 88540: "El Paso, TX", 88541: "El Paso, TX", 88542: "El Paso, TX", 88543: "El Paso, TX", 88544: "El Paso, TX", 88545: "El Paso, TX", 88546: "El Paso, TX", 88547: "El Paso, TX", 88548: "El Paso, TX", 88549: "El Paso, TX", 88550: "El Paso, TX", 88553: "El Paso, TX", 88554: "El Paso, TX", 88555: "El Paso, TX", 88556: "El Paso, TX", 88557: "El Paso, TX", 88558: "El Paso, TX", 88559: "El Paso, TX", 88560: "El Paso, TX", 88561: "El Paso, TX", 88562: "El Paso, TX", 88563: "El Paso, TX", 88565: "El Paso, TX", 88566: "El Paso, TX", 88567: "El Paso, TX", 88568: "El Paso, TX", 88569: "El Paso, TX", 88570: "El Paso, TX", 88571: "El Paso, TX", 88572: "El Paso, TX", 88573: "El Paso, TX", 88574: "El Paso, TX", 88575: "El Paso, TX", 88576: "El Paso, TX", 88577: "El Paso, TX", 88578: "El Paso, TX", 88579: "El Paso, TX", 88580: "El Paso, TX", 88581: "El Paso, TX", 88582: "El Paso, TX", 88583: "El Paso, TX", 88584: "El Paso, TX", 88585: "El Paso, TX", 88586: "El Paso, TX", 88587: "El Paso, TX", 88588: "El Paso, TX", 88589: "El Paso, TX", 88590: "El Paso, TX", 88595: "El Paso, TX", 

    78550: "Harlingen, TX", 78551: "Harlingen, TX", 78552: "Harlingen, TX", 78553: "Harlingen, TX", 

    78840: "Del Rio, TX", 78841: "Del Rio, TX", 78842: "Del Rio, TX", 78843: "Del Rio, TX", 78847: "Del Rio, TX", 

    78520: "Brownsville, TX", 78521: "Brownsville, TX", 78522: "Brownsville, TX", 78523: "Brownsville, TX", 78526: "Brownsville, TX", 

    78201: "San Antonio, TX", 78202: "San Antonio, TX", 78203: "San Antonio, TX", 78204: "San Antonio, TX", 78205: "San Antonio, TX", 78206: "San Antonio, TX", 78207: "San Antonio, TX", 78208: "San Antonio, TX", 78209: "San Antonio, TX", 78210: "San Antonio, TX", 78211: "San Antonio, TX", 78212: "San Antonio, TX", 78213: "San Antonio, TX", 78214: "San Antonio, TX", 78215: "San Antonio, TX", 78216: "San Antonio, TX", 78217: "San Antonio, TX", 78218: "San Antonio, TX", 78219: "San Antonio, TX", 78220: "San Antonio, TX", 78221: "San Antonio, TX", 78222: "San Antonio, TX", 78223: "San Antonio, TX", 78224: "San Antonio, TX", 78225: "San Antonio, TX", 78226: "San Antonio, TX", 78227: "San Antonio, TX", 78228: "San Antonio, TX", 78229: "San Antonio, TX", 78230: "San Antonio, TX", 78231: "San Antonio, TX", 78232: "San Antonio, TX", 78233: "San Antonio, TX", 78234: "San Antonio, TX", 78235: "San Antonio, TX", 78236: "San Antonio, TX", 78237: "San Antonio, TX", 78238: "San Antonio, TX", 78239: "San Antonio, TX", 78240: "San Antonio, TX", 78241: "San Antonio, TX", 78242: "San Antonio, TX", 78243: "San Antonio, TX", 78244: "San Antonio, TX", 78245: "San Antonio, TX", 78246: "San Antonio, TX", 78247: "San Antonio, TX", 78248: "San Antonio, TX", 78249: "San Antonio, TX", 78250: "San Antonio, TX", 78251: "San Antonio, TX", 78252: "San Antonio, TX", 78253: "San Antonio, TX", 78254: "San Antonio, TX", 78255: "San Antonio, TX", 78256: "San Antonio, TX", 78257: "San Antonio, TX", 78258: "San Antonio, TX", 78259: "San Antonio, TX", 78260: "San Antonio, TX", 78261: "San Antonio, TX", 78263: "San Antonio, TX", 78264: "San Antonio, TX", 78265: "San Antonio, TX", 78266: "San Antonio, TX", 78268: "San Antonio, TX", 78269: "San Antonio, TX", 78270: "San Antonio, TX", 78278: "San Antonio, TX", 78279: "San Antonio, TX", 78280: "San Antonio, TX", 78283: "San Antonio, TX", 78284: "San Antonio, TX", 78285: "San Antonio, TX", 78288: "San Antonio, TX", 78289: "San Antonio, TX", 78291: "San Antonio, TX", 78292: "San Antonio, TX", 78293: "San Antonio, TX", 78294: "San Antonio, TX", 78295: "San Antonio, TX", 78296: "San Antonio, TX", 78297: "San Antonio, TX", 78298: "San Antonio, TX", 78299: "San Antonio, TX", 

    77001: "Houston, TX", 77002: "Houston, TX", 77003: "Houston, TX", 77004: "Houston, TX", 77005: "Houston, TX", 77006: "Houston, TX", 77007: "Houston, TX", 77008: "Houston, TX", 77009: "Houston, TX", 77010: "Houston, TX", 77011: "Houston, TX", 77012: "Houston, TX", 77013: "Houston, TX", 77014: "Houston, TX", 77015: "Houston, TX", 77016: "Houston, TX", 77017: "Houston, TX", 77018: "Houston, TX", 77019: "Houston, TX", 77020: "Houston, TX", 77021: "Houston, TX", 77022: "Houston, TX", 77023: "Houston, TX", 77024: "Houston, TX", 77025: "Houston, TX", 77026: "Houston, TX", 77027: "Houston, TX", 77028: "Houston, TX", 77029: "Houston, TX", 77030: "Houston, TX", 77031: "Houston, TX", 77032: "Houston, TX", 77033: "Houston, TX", 77034: "Houston, TX", 77035: "Houston, TX", 77036: "Houston, TX", 77037: "Houston, TX", 77038: "Houston, TX", 77039: "Houston, TX", 77040: "Houston, TX", 77041: "Houston, TX", 77042: "Houston, TX", 77043: "Houston, TX", 77044: "Houston, TX", 77045: "Houston, TX", 77046: "Houston, TX", 77047: "Houston, TX", 77048: "Houston, TX", 77049: "Houston, TX", 77050: "Houston, TX", 77051: "Houston, TX", 77052: "Houston, TX", 77053: "Houston, TX", 77054: "Houston, TX", 77055: "Houston, TX", 77056: "Houston, TX", 77057: "Houston, TX", 77058: "Houston, TX", 77059: "Houston, TX", 77060: "Houston, TX", 77061: "Houston, TX", 77062: "Houston, TX", 77063: "Houston, TX", 77064: "Houston, TX", 77065: "Houston, TX", 77066: "Houston, TX", 77067: "Houston, TX", 77068: "Houston, TX", 77069: "Houston, TX", 77070: "Houston, TX", 77071: "Houston, TX", 77072: "Houston, TX", 77073: "Houston, TX", 77074: "Houston, TX", 77075: "Houston, TX", 77076: "Houston, TX", 77077: "Houston, TX", 77078: "Houston, TX", 77079: "Houston, TX", 77080: "Houston, TX", 77081: "Houston, TX", 77082: "Houston, TX", 77083: "Houston, TX", 77084: "Houston, TX", 77085: "Houston, TX", 77086: "Houston, TX", 77087: "Houston, TX", 77088: "Houston, TX", 77089: "Houston, TX", 77090: "Houston, TX", 77091: "Houston, TX", 77092: "Houston, TX", 77093: "Houston, TX", 77094: "Houston, TX", 77095: "Houston, TX", 77096: "Houston, TX", 77098: "Houston, TX", 77099: "Houston, TX", 77201: "Houston, TX", 77202: "Houston, TX", 77203: "Houston, TX", 77204: "Houston, TX", 77205: "Houston, TX", 77206: "Houston, TX", 77207: "Houston, TX", 77208: "Houston, TX", 77209: "Houston, TX", 77210: "Houston, TX", 77212: "Houston, TX", 77213: "Houston, TX", 77215: "Houston, TX", 77216: "Houston, TX", 77217: "Houston, TX", 77218: "Houston, TX", 77219: "Houston, TX", 77220: "Houston, TX", 77221: "Houston, TX", 77222: "Houston, TX", 77223: "Houston, TX", 77224: "Houston, TX", 77225: "Houston, TX", 77226: "Houston, TX", 77227: "Houston, TX", 77228: "Houston, TX", 77229: "Houston, TX", 77230: "Houston, TX", 77231: "Houston, TX", 77233: "Houston, TX", 77234: "Houston, TX", 77235: "Houston, TX", 77236: "Houston, TX", 77237: "Houston, TX", 77238: "Houston, TX", 77240: "Houston, TX", 77241: "Houston, TX", 77242: "Houston, TX", 77243: "Houston, TX", 77244: "Houston, TX", 77245: "Houston, TX", 77248: "Houston, TX", 77249: "Houston, TX", 77251: "Houston, TX", 77252: "Houston, TX", 77253: "Houston, TX", 77254: "Houston, TX", 77255: "Houston, TX", 77256: "Houston, TX", 77257: "Houston, TX", 77258: "Houston, TX", 77259: "Houston, TX", 77261: "Houston, TX", 77262: "Houston, TX", 77263: "Houston, TX", 77265: "Houston, TX", 77266: "Houston, TX", 77267: "Houston, TX", 77268: "Houston, TX", 77269: "Houston, TX", 77270: "Houston, TX", 77271: "Houston, TX", 77272: "Houston, TX", 77273: "Houston, TX", 77274: "Houston, TX", 77275: "Houston, TX", 77277: "Houston, TX", 77279: "Houston, TX", 77280: "Houston, TX", 77282: "Houston, TX", 77284: "Houston, TX", 77287: "Houston, TX", 77288: "Houston, TX", 77289: "Houston, TX", 77290: "Houston, TX", 77291: "Houston, TX", 77292: "Houston, TX", 77293: "Houston, TX", 77297: "Houston, TX", 77299: "Houston, TX", 

    78557: "Hidalgo, TX", 

    78520: "Brownsville, TX", 78521: "Brownsville, TX", 78522: "Brownsville, TX", 78523: "Brownsville, TX", 78526: "Brownsville, TX", 

    75201: "Dallas, TX", 75202: "Dallas, TX", 75203: "Dallas, TX", 75204: "Dallas, TX", 75205: "Dallas, TX", 75206: "Dallas, TX", 75207: "Dallas, TX", 75208: "Dallas, TX", 75209: "Dallas, TX", 75210: "Dallas, TX", 75211: "Dallas, TX", 75212: "Dallas, TX", 75214: "Dallas, TX", 75215: "Dallas, TX", 75216: "Dallas, TX", 75217: "Dallas, TX", 75218: "Dallas, TX", 75219: "Dallas, TX", 75220: "Dallas, TX", 75221: "Dallas, TX", 75222: "Dallas, TX", 75223: "Dallas, TX", 75224: "Dallas, TX", 75225: "Dallas, TX", 75226: "Dallas, TX", 75227: "Dallas, TX", 75228: "Dallas, TX", 75229: "Dallas, TX", 75230: "Dallas, TX", 75231: "Dallas, TX", 75232: "Dallas, TX", 75233: "Dallas, TX", 75234: "Dallas, TX", 75235: "Dallas, TX", 75236: "Dallas, TX", 75237: "Dallas, TX", 75238: "Dallas, TX", 75240: "Dallas, TX", 75241: "Dallas, TX", 75242: "Dallas, TX", 75243: "Dallas, TX", 75244: "Dallas, TX", 75246: "Dallas, TX", 75247: "Dallas, TX", 75248: "Dallas, TX", 75249: "Dallas, TX", 75250: "Dallas, TX", 75251: "Dallas, TX", 75252: "Dallas, TX", 75253: "Dallas, TX", 75254: "Dallas, TX", 75260: "Dallas, TX", 75261: "Dallas, TX", 75262: "Dallas, TX", 75263: "Dallas, TX", 75264: "Dallas, TX", 75265: "Dallas, TX", 75266: "Dallas, TX", 75267: "Dallas, TX", 75270: "Dallas, TX", 75275: "Dallas, TX", 75277: "Dallas, TX", 75283: "Dallas, TX", 75284: "Dallas, TX", 75285: "Dallas, TX", 75287: "Dallas, TX", 75301: "Dallas, TX", 75303: "Dallas, TX", 75312: "Dallas, TX", 75313: "Dallas, TX", 75315: "Dallas, TX", 75320: "Dallas, TX", 75326: "Dallas, TX", 75336: "Dallas, TX", 75339: "Dallas, TX", 75342: "Dallas, TX", 75354: "Dallas, TX", 75355: "Dallas, TX", 75356: "Dallas, TX", 75357: "Dallas, TX", 75358: "Dallas, TX", 75359: "Dallas, TX", 75360: "Dallas, TX", 75367: "Dallas, TX", 75368: "Dallas, TX", 75370: "Dallas, TX", 75371: "Dallas, TX", 75372: "Dallas, TX", 75373: "Dallas, TX", 75374: "Dallas, TX", 75376: "Dallas, TX", 75378: "Dallas, TX", 75379: "Dallas, TX", 75380: "Dallas, TX", 75381: "Dallas, TX", 75382: "Dallas, TX", 75389: "Dallas, TX", 75390: "Dallas, TX", 75391: "Dallas, TX", 75392: "Dallas, TX", 75393: "Dallas, TX", 75394: "Dallas, TX", 75395: "Dallas, TX", 75397: "Dallas, TX", 75398: "Dallas, TX", 

    78852: "Eagle Pass, TX", 78853: "Eagle Pass, TX", 

    90001: "Los Angeles, CA", 90002: "Los Angeles, CA", 90003: "Los Angeles, CA", 90004: "Los Angeles, CA", 90005: "Los Angeles, CA", 90006: "Los Angeles, CA", 90007: "Los Angeles, CA", 90008: "Los Angeles, CA", 90009: "Los Angeles, CA", 90010: "Los Angeles, CA", 90011: "Los Angeles, CA", 90012: "Los Angeles, CA", 90013: "Los Angeles, CA", 90014: "Los Angeles, CA", 90015: "Los Angeles, CA", 90016: "Los Angeles, CA", 90017: "Los Angeles, CA", 90018: "Los Angeles, CA", 90019: "Los Angeles, CA", 90020: "Los Angeles, CA", 90021: "Los Angeles, CA", 90022: "Los Angeles, CA", 90023: "Los Angeles, CA", 90024: "Los Angeles, CA", 90025: "Los Angeles, CA", 90026: "Los Angeles, CA", 90027: "Los Angeles, CA", 90028: "Los Angeles, CA", 90029: "Los Angeles, CA", 90030: "Los Angeles, CA", 90031: "Los Angeles, CA", 90032: "Los Angeles, CA", 90033: "Los Angeles, CA", 90034: "Los Angeles, CA", 90035: "Los Angeles, CA", 90036: "Los Angeles, CA", 90037: "Los Angeles, CA", 90038: "Los Angeles, CA", 90039: "Los Angeles, CA", 90040: "Los Angeles, CA", 90041: "Los Angeles, CA", 90042: "Los Angeles, CA", 90043: "Los Angeles, CA", 90044: "Los Angeles, CA", 90045: "Los Angeles, CA", 90046: "Los Angeles, CA", 90047: "Los Angeles, CA", 90048: "Los Angeles, CA", 90049: "Los Angeles, CA", 90050: "Los Angeles, CA", 90051: "Los Angeles, CA", 90052: "Los Angeles, CA", 90053: "Los Angeles, CA", 90054: "Los Angeles, CA", 90055: "Los Angeles, CA", 90056: "Los Angeles, CA", 90057: "Los Angeles, CA", 90058: "Los Angeles, CA", 90059: "Los Angeles, CA", 90060: "Los Angeles, CA", 90061: "Los Angeles, CA", 90062: "Los Angeles, CA", 90063: "Los Angeles, CA", 90064: "Los Angeles, CA", 90065: "Los Angeles, CA", 90066: "Los Angeles, CA", 90067: "Los Angeles, CA", 90068: "Los Angeles, CA", 90069: "Los Angeles, CA", 90070: "Los Angeles, CA", 90071: "Los Angeles, CA", 90072: "Los Angeles, CA", 90073: "Los Angeles, CA", 90074: "Los Angeles, CA", 90075: "Los Angeles, CA", 90076: "Los Angeles, CA", 90077: "Los Angeles, CA", 90078: "Los Angeles, CA", 90079: "Los Angeles, CA", 90080: "Los Angeles, CA", 90081: "Los Angeles, CA", 90082: "Los Angeles, CA", 90083: "Los Angeles, CA", 90084: "Los Angeles, CA", 90086: "Los Angeles, CA", 90087: "Los Angeles, CA", 90088: "Los Angeles, CA", 90089: "Los Angeles, CA", 90091: "Los Angeles, CA", 90093: "Los Angeles, CA", 90094: "Los Angeles, CA", 90095: "Los Angeles, CA", 90096: "Los Angeles, CA", 90099: "Los Angeles, CA", 90134: "Los Angeles, CA", 90189: "Los Angeles, CA", 90230: "Los Angeles, CA", 

    92154: "Otay Mesa, CA", 

    94102: "San Francisco", 94103: "San Francisco", 94104: "San Francisco", 94105: "San Francisco", 94107: "San Francisco", 94108: "San Francisco", 94109: "San Francisco", 94110: "San Francisco", 94111: "San Francisco", 94112: "San Francisco", 94114: "San Francisco", 94115: "San Francisco", 94116: "San Francisco", 94117: "San Francisco", 94118: "San Francisco", 94119: "San Francisco", 94120: "San Francisco", 94121: "San Francisco", 94122: "San Francisco", 94123: "San Francisco", 94124: "San Francisco", 94125: "San Francisco", 94126: "San Francisco", 94127: "San Francisco", 94128: "San Francisco", 94129: "San Francisco", 94130: "San Francisco", 94131: "San Francisco", 94132: "San Francisco", 94133: "San Francisco", 94134: "San Francisco", 94137: "San Francisco", 94139: "San Francisco", 94140: "San Francisco", 94141: "San Francisco", 94142: "San Francisco", 94143: "San Francisco", 94144: "San Francisco", 94145: "San Francisco", 94146: "San Francisco", 94147: "San Francisco", 94151: "San Francisco", 94158: "San Francisco", 94159: "San Francisco", 94160: "San Francisco", 94161: "San Francisco", 94163: "San Francisco", 94164: "San Francisco", 94172: "San Francisco", 94177: "San Francisco", 94188: "San Francisco", 

    92143: "San Ysidro, CA", 92173: "San Ysidro, CA", 

    92231: "Calexico, CA", 92232: "Calexico, CA", 

    85621: "Nogales, AZ", 85628: "Nogales, AZ", 85648: "Nogales, AZ", 

    85001: "Phoenix, AZ", 85002: "Phoenix, AZ", 85003: "Phoenix, AZ", 85004: "Phoenix, AZ", 85005: "Phoenix, AZ", 85006: "Phoenix, AZ", 85007: "Phoenix, AZ", 85008: "Phoenix, AZ", 85009: "Phoenix, AZ", 85010: "Phoenix, AZ", 85011: "Phoenix, AZ", 85012: "Phoenix, AZ", 85013: "Phoenix, AZ", 85014: "Phoenix, AZ", 85015: "Phoenix, AZ", 85016: "Phoenix, AZ", 85017: "Phoenix, AZ", 85018: "Phoenix, AZ", 85019: "Phoenix, AZ", 85020: "Phoenix, AZ", 85021: "Phoenix, AZ", 85022: "Phoenix, AZ", 85023: "Phoenix, AZ", 85024: "Phoenix, AZ", 85026: "Phoenix, AZ", 85027: "Phoenix, AZ", 85028: "Phoenix, AZ", 85029: "Phoenix, AZ", 85030: "Phoenix, AZ", 85031: "Phoenix, AZ", 85032: "Phoenix, AZ", 85033: "Phoenix, AZ", 85034: "Phoenix, AZ", 85035: "Phoenix, AZ", 85036: "Phoenix, AZ", 85037: "Phoenix, AZ", 85038: "Phoenix, AZ", 85039: "Phoenix, AZ", 85040: "Phoenix, AZ", 85041: "Phoenix, AZ", 85042: "Phoenix, AZ", 85043: "Phoenix, AZ", 85044: "Phoenix, AZ", 85045: "Phoenix, AZ", 85046: "Phoenix, AZ", 85048: "Phoenix, AZ", 85050: "Phoenix, AZ", 85051: "Phoenix, AZ", 85053: "Phoenix, AZ", 85054: "Phoenix, AZ", 85060: "Phoenix, AZ", 85061: "Phoenix, AZ", 85062: "Phoenix, AZ", 85063: "Phoenix, AZ", 85064: "Phoenix, AZ", 85065: "Phoenix, AZ", 85066: "Phoenix, AZ", 85067: "Phoenix, AZ", 85068: "Phoenix, AZ", 85069: "Phoenix, AZ", 85070: "Phoenix, AZ", 85071: "Phoenix, AZ", 85072: "Phoenix, AZ", 85073: "Phoenix, AZ", 85074: "Phoenix, AZ", 85075: "Phoenix, AZ", 85076: "Phoenix, AZ", 85078: "Phoenix, AZ", 85079: "Phoenix, AZ", 85080: "Phoenix, AZ", 85082: "Phoenix, AZ", 85083: "Phoenix, AZ", 85085: "Phoenix, AZ", 85086: "Phoenix, AZ", 85087: "Phoenix, AZ", 

    85701: "Tucson, AZ", 85702: "Tucson, AZ", 85703: "Tucson, AZ", 85704: "Tucson, AZ", 85705: "Tucson, AZ", 85706: "Tucson, AZ", 85707: "Tucson, AZ", 85708: "Tucson, AZ", 85709: "Tucson, AZ", 85710: "Tucson, AZ", 85711: "Tucson, AZ", 85712: "Tucson, AZ", 85713: "Tucson, AZ", 85714: "Tucson, AZ", 85715: "Tucson, AZ", 85716: "Tucson, AZ", 85717: "Tucson, AZ", 85718: "Tucson, AZ", 85719: "Tucson, AZ", 85720: "Tucson, AZ", 85721: "Tucson, AZ", 85722: "Tucson, AZ", 85723: "Tucson, AZ", 85724: "Tucson, AZ", 85725: "Tucson, AZ", 85726: "Tucson, AZ", 85728: "Tucson, AZ", 85730: "Tucson, AZ", 85731: "Tucson, AZ", 85732: "Tucson, AZ", 85733: "Tucson, AZ", 85734: "Tucson, AZ", 85735: "Tucson, AZ", 85736: "Tucson, AZ", 85737: "Tucson, AZ", 85738: "Tucson, AZ", 85739: "Tucson, AZ", 85740: "Tucson, AZ", 85741: "Tucson, AZ", 85742: "Tucson, AZ", 85743: "Tucson, AZ", 85744: "Tucson, AZ", 85745: "Tucson, AZ", 85746: "Tucson, AZ", 85747: "Tucson, AZ", 85748: "Tucson, AZ", 85749: "Tucson, AZ", 85750: "Tucson, AZ", 85751: "Tucson, AZ", 85752: "Tucson, AZ", 85754: "Tucson, AZ", 85755: "Tucson, AZ", 85756: "Tucson, AZ", 85757: "Tucson, AZ", 85775: "Tucson, AZ", 

    85336: "San Luis, AZ", 85349: "San Luis, AZ", 

    85607: "Douglas, AZ", 85608: "Douglas, AZ", 85655: "Douglas, AZ", 

    85620: "Naco, AZ", 
    
    10001: "New York, NY", 10002: "New York, NY", 10003: "New York, NY", 10004: "New York, NY", 10005: "New York, NY", 10006: "New York, NY", 10007: "New York, NY", 10008: "New York, NY", 10009: "New York, NY", 10010: "New York, NY", 10011: "New York, NY", 10012: "New York, NY", 10013: "New York, NY", 10014: "New York, NY", 10016: "New York, NY", 10017: "New York, NY", 10018: "New York, NY", 10019: "New York, NY", 10020: "New York, NY", 10021: "New York, NY", 10022: "New York, NY", 10023: "New York, NY", 10024: "New York, NY", 10025: "New York, NY", 10026: "New York, NY", 10027: "New York, NY", 10028: "New York, NY", 10029: "New York, NY", 10030: "New York, NY", 10031: "New York, NY", 10032: "New York, NY", 10033: "New York, NY", 10034: "New York, NY", 10035: "New York, NY", 10036: "New York, NY", 10037: "New York, NY", 10038: "New York, NY", 10039: "New York, NY", 10040: "New York, NY", 10041: "New York, NY", 10043: "New York, NY", 10044: "New York, NY", 10045: "New York, NY", 10055: "New York, NY", 10060: "New York, NY", 10065: "New York, NY", 10069: "New York, NY", 10075: "New York, NY", 10080: "New York, NY", 10081: "New York, NY", 10087: "New York, NY", 10090: "New York, NY", 10101: "New York, NY", 10102: "New York, NY", 10103: "New York, NY", 10104: "New York, NY", 10105: "New York, NY", 10106: "New York, NY", 10107: "New York, NY", 10108: "New York, NY", 10109: "New York, NY", 10110: "New York, NY", 10111: "New York, NY", 10112: "New York, NY", 10113: "New York, NY", 10114: "New York, NY", 10115: "New York, NY", 10116: "New York, NY", 10117: "New York, NY", 10118: "New York, NY", 10119: "New York, NY", 10120: "New York, NY", 10121: "New York, NY", 10122: "New York, NY", 10123: "New York, NY", 10124: "New York, NY", 10125: "New York, NY", 10126: "New York, NY", 10128: "New York, NY", 10129: "New York, NY", 10130: "New York, NY", 10131: "New York, NY", 10132: "New York, NY", 10133: "New York, NY", 10138: "New York, NY", 10150: "New York, NY", 10151: "New York, NY", 10152: "New York, NY", 10153: "New York, NY", 10154: "New York, NY", 10155: "New York, NY", 10156: "New York, NY", 10157: "New York, NY", 10158: "New York, NY", 10159: "New York, NY", 10160: "New York, NY", 10162: "New York, NY", 10163: "New York, NY", 10164: "New York, NY", 10165: "New York, NY", 10166: "New York, NY", 10167: "New York, NY", 10168: "New York, NY", 10169: "New York, NY", 10170: "New York, NY", 10171: "New York, NY", 10172: "New York, NY", 10173: "New York, NY", 10174: "New York, NY", 10175: "New York, NY", 10176: "New York, NY", 10177: "New York, NY", 10178: "New York, NY", 10179: "New York, NY", 10185: "New York, NY", 10199: "New York, NY", 10203: "New York, NY", 10211: "New York, NY", 10212: "New York, NY", 10213: "New York, NY", 10242: "New York, NY", 10249: "New York, NY", 10256: "New York, NY", 10258: "New York, NY", 10259: "New York, NY", 10260: "New York, NY", 10261: "New York, NY", 10265: "New York, NY", 10268: "New York, NY", 10269: "New York, NY", 10270: "New York, NY", 10271: "New York, NY", 10272: "New York, NY", 10273: "New York, NY", 10274: "New York, NY", 10275: "New York, NY", 10276: "New York, NY", 10277: "New York, NY", 10278: "New York, NY", 10279: "New York, NY", 10280: "New York, NY", 10281: "New York, NY", 10282: "New York, NY", 10285: "New York, NY", 10286: "New York, NY",
    
    11430: "John F. Kennedy Airport, NY",
    
    70062: "New Orleans International Airport, LA",
    
    71303: "Alexandria International Airport, LA",

    33142: "Miami International Airport, FL",
    
    30320: "Hartsfield International Airport, GA",
    
    7114: "Newark International Airport, NJ",
    
    60666: "Chicago-O'Hare International Airport, IL",
    
    20166: "Dulles International Airport, DC"}

    city = None
    try:
        city = zipcode_dict[zipcode]
    except KeyError:
        pass

    return city

# string to date function ------------------------------------------------------

def string_to_date(string_date):
    """
    string_to_date converts the yyyy-mm string into a date variable (mid-month by default)
    output: date variable of the form yyyy-mm-15
    """
    # extract year & month from string
    year = int(string_date[0:4])
    month = int(string_date[-2:])

    # create date variable
    date = datetime.datetime(year, month, 15)

    return date

# strings to date function -----------------------------------------------------

def strings_to_date(row):
    """
    strings_to_date converts the yyyy-mm string into a date variable (mid-month by default)
    output: date variable of the form yyyy-mm-15
    """
    # extract year & month from string
    year = int(row["year"])
    month = datetime.datetime.strptime(row["month"], "%B").month

    # create date variable
    date = datetime.datetime(year, month, 15)

    return date

# # jump check function ------------------------------------------------------

# def is_jump(row):
#     """
#     is_jump checks if the current level of deportations has doubled since the previous period
#     output: True if deportations have doubled & False otherwise
#     """
#     current_value = row["num_deportations"]
#     previous_value = row["num_deportations_lag"]

#     return ((current_value - previous_value)/previous_value > 2)

# Deportation data -------------------------------------------------------------

## read in file
deportation_data_raw = pandas.read_csv("deportation_data/TRAC/trac_deportation_data_3states_alldates.csv")
deportation_data_raw.rename(columns = {'value':'num_deportations'}, inplace = True)
deportation_data_raw["state"] = deportation_data_raw["location"].str[-2:]
deportation_data_raw = deportation_data_raw[deportation_data_raw["date"] != "All"]
deportation_data_raw["num_deportations"] = pandas.to_numeric(deportation_data_raw["num_deportations"].str.replace(",", ""))

deportation_data_raw = deportation_data_raw[deportation_data_raw["conviction"] != "Illegal entry"]
deportation_data_raw = deportation_data_raw[deportation_data_raw["conviction"] != "Illegal re-entry"]
deportation_data_raw = deportation_data_raw[deportation_data_raw["conviction"] != "No conviction"]

# ## create dataframe that contains reassigned non-city locations
# deportation_data = deportation_data_raw

# ## reassign non-city locations to the city they're in
# deportation_data["city_name_reassigned"] = deportation_data["location"]
# deportation_data["city_name_reassigned"] = deportation_data["city_name_reassigned"].replace({"Valley International Airport, TX": "Harlingen, TX", "Paso del Norte, TX": "El Paso, TX", "Brownsville-Matamor, TX": "Brownsville, TX", "Laredo Columbia Bridge, TX": "Laredo, TX", "Houston Airport, TX": "Houston, TX", "Juarez-Lincoln Bridge, TX": "Laredo, TX"})

# ## aggregate non-city locations to cities in the dataset if they exist
# deportation_data["num_deportations"]

# make date date variable
deportation_data_raw["new_date"] = deportation_data_raw["date"].apply(string_to_date)

files = [f for f in os.listdir("num_crimes_by_type/monthly/all_locations") if not f.startswith('.')]

crime_data = pandas.io.stata.read_stata(f"num_crimes_by_type/monthly/all_locations/{files[0]}")
for file in files[1:]:
    crime_data_cur = pandas.io.stata.read_stata(f"num_crimes_by_type/monthly/all_locations/{file}")
    crime_data = pandas.concat([crime_data, crime_data_cur], ignore_index=True)

crime_data_clean = crime_data[['year','month', 'state', 'address_zip_code','agg_assault_tot_adult','agg_assault_tot_arrests','all_other_tot_adult','all_other_tot_arrests','burglary_tot_adult','burglary_tot_arrests','mtr_veh_theft_tot_adult','mtr_veh_theft_tot_arrests','murder_tot_adult','murder_tot_arrests','oth_assault_tot_adult','oth_assault_tot_arrests','poss_drug_total_tot_adult','poss_drug_total_tot_arrests','poss_heroin_coke_tot_adult','poss_heroin_coke_tot_arrests','poss_other_drug_tot_adult','poss_other_drug_tot_arrests','poss_synth_narc_tot_adult','poss_synth_narc_tot_arrests','rape_tot_adult','rape_tot_arrests','robbery_tot_adult','robbery_tot_arrests','runaways_tot_adult','runaways_tot_arrests','sale_cannabis_tot_adult','sale_cannabis_tot_arrests','sale_drug_total_tot_adult','sale_drug_total_tot_arrests','sale_heroin_coke_tot_adult','sale_heroin_coke_tot_arrests','sale_other_drug_tot_adult','sale_other_drug_tot_arrests','sale_synth_narc_tot_adult','sale_synth_narc_tot_arrests','stolen_prop_tot_adult','stolen_prop_tot_arrests','suspicion_tot_adult','suspicion_tot_arrests','theft_tot_adult','theft_tot_arrests','vandalism_tot_adult','vandalism_tot_arrests','weapons_tot_adult','weapons_tot_arrests']]
crime_data_clean = crime_data_clean[crime_data_clean["state"].isin(["arizona", "california", "texas", "new york", "new jersey", "louisiana", "florida", "virginia"])]
crime_data_clean = crime_data_clean[crime_data_clean["address_zip_code"] != ""]
crime_data_clean = crime_data_clean.astype({'address_zip_code':'int', "agg_assault_tot_adult": "int", "agg_assault_tot_arrests": "int", "all_other_tot_adult": "int", "all_other_tot_arrests": "int", "burglary_tot_adult": "int", "burglary_tot_arrests": "int", "mtr_veh_theft_tot_adult": "int", "mtr_veh_theft_tot_arrests": "int", "murder_tot_adult": "int", "murder_tot_arrests": "int", "oth_assault_tot_adult": "int", "oth_assault_tot_arrests": "int", "poss_drug_total_tot_adult": "int", "poss_drug_total_tot_arrests": "int", "poss_heroin_coke_tot_adult": "int", "poss_heroin_coke_tot_arrests": "int", "poss_other_drug_tot_adult": "int", "poss_other_drug_tot_arrests": "int", "poss_synth_narc_tot_adult": "int", "poss_synth_narc_tot_arrests": "int", "rape_tot_adult": "int", "rape_tot_arrests": "int", "robbery_tot_adult": "int", "robbery_tot_arrests": "int", "runaways_tot_adult": "int", "runaways_tot_arrests": "int", "sale_cannabis_tot_adult": "int", "sale_cannabis_tot_arrests": "int", "sale_drug_total_tot_adult": "int", "sale_drug_total_tot_arrests": "int", "sale_heroin_coke_tot_adult": "int", "sale_heroin_coke_tot_arrests": "int", "sale_other_drug_tot_adult": "int", "sale_other_drug_tot_arrests": "int", "sale_synth_narc_tot_adult": "int", "sale_synth_narc_tot_arrests": "int", "stolen_prop_tot_adult": "int", "stolen_prop_tot_arrests": "int", "suspicion_tot_adult": "int", "suspicion_tot_arrests": "int", "theft_tot_adult": "int", "theft_tot_arrests": "int", "vandalism_tot_adult": "int", "vandalism_tot_arrests": "int", "weapons_tot_adult": "int", "weapons_tot_arrests": "int"})
crime_data_clean["city_name"] = crime_data_clean["address_zip_code"].apply(zipcode_to_city)
crime_data_clean["date"] = crime_data_clean.apply(strings_to_date, axis=1)

## categorize by crime type
crime_data_clean['Theft-related crime'] = crime_data_clean[['burglary_tot_arrests','mtr_veh_theft_tot_arrests','robbery_tot_arrests','stolen_prop_tot_arrests','theft_tot_arrests']].sum(axis=1)

crime_data_clean['Violent-related crime'] = crime_data_clean[['murder_tot_arrests','oth_assault_tot_arrests','rape_tot_arrests']].sum(axis=1)

crime_data_clean['Drug-related crime'] = crime_data_clean[['sale_cannabis_tot_arrests','sale_heroin_coke_tot_arrests','sale_other_drug_tot_arrests','sale_synth_narc_tot_arrests']].sum(axis=1)

#sale_drug_total_tot_arrests

# plot data

states_short = ["AZ", "CA", "TX", "NY", "NJ", "LA", "FL", "DC"]
states_long = ["arizona", "california", "texas", "new york", "new jersey", "louisiana", "florida", "virginia"]

##### aggregate by city
# for index in enumerate(states_short):
#     curr_dep_df = deportation_data_raw[deportation_data_raw["state"] == states_short[index[0]]]
#     dep_cities = curr_dep_df["location"].unique()
#     curr_crime_df = crime_data_clean[crime_data_clean["state"] == states_long[index[0]]]
#     curr_crime_df['sum'] = curr_crime_df.iloc[:, 6:50].sum(axis=1)
#     crime_cities = curr_crime_df["city_name"].unique()
    
#     cities = list(set(dep_cities) & set(crime_cities))
#     curr_dep_sub_df = curr_dep_df
#     curr_crime_sub_df = curr_crime_df
#     for city in cities:
#         curr_dep_sub_df = curr_dep_df[curr_dep_df["location"] == city]
#         curr_dep_sub_df = curr_dep_sub_df.groupby(['location', 'conviction', 'new_date'], as_index=False).agg({'num_deportations':'sum'})

#         curr_crime_sub_df = curr_crime_df[curr_crime_df["city_name"] == city]
#         curr_crime_sub_df = curr_crime_sub_df.groupby(['date'], as_index=False).agg({'sum':'sum'})

#         # check jumps
#         # curr_df_indexed = curr_df.set_index("new_date")
#         # lag_df = curr_df_indexed.groupby(["location"]).shift(freq=pandas.DateOffset(months=1))
#         # curr_df.merge(lag_df, on=["location", "new_date"], how="left")
        
#         # curr_df.set_index(["location", "new_date"], inplace = True)
#         # lag_df = curr_df.rename(columns={"num_deportations": "num_deportations_lag"})
#         # lag_df = lag_df.groupby(level="location")["num_deportations_lag"].shift(1)
#         # curr_df = curr_df.join(lag_df)
        
#     #    curr_df["jump"] = curr_df.apply(is_jump, axis=1)

#     #    jump_date_list = curr_df[curr_df["jump"]]
#     #idea: remove the indexing, then create a dictionary of location-list of dates key-value pairs
#         curr_chart = make_subplots(specs=[[{"secondary_y": True}]])

#         # Add traces
#         curr_chart.add_trace(
#             go.Scatter(x=curr_dep_sub_df['new_date'], y=curr_dep_sub_df['num_deportations'], name="Number of deportations",
#             mode='lines'),
#             secondary_y=False,
#         )

#         curr_chart.add_trace(
#             go.Scatter(x=curr_crime_sub_df['date'], y=curr_crime_sub_df['sum'], name="Number of crimes",
#             mode='lines'),
#             secondary_y=True,
#         )

#         # Add figure title
#         curr_chart.update_layout(
#             title_text=f"Deportations and crime in {city}"
#         )

#         # Set y-axes titles
#         curr_chart.update_yaxes(title_text="Number of deportations", secondary_y=False)
#         curr_chart.update_yaxes(title_text="Number of crimes", secondary_y=True)

#         curr_chart.show()

agg_dep_df = deportation_data_raw.groupby(['new_date'], as_index=False).agg({'num_deportations':'sum'})
agg_dep_df.to_csv("deportations.csv", index=False, header=True)
agg_crime_df = crime_data_clean.groupby(['date'], as_index=False).agg({'Theft-related crime':'sum', 'Violent-related crime':'sum', 'Drug-related crime':'sum'})
agg_crime_df.to_csv("crime.csv", index=False, header=True)

# #### total aggregate

# agg_dep_df = deportation_data_raw.groupby(['new_date'], as_index=False).agg({'num_deportations':'sum'})

# agg_crime_df = crime_data_clean.groupby(['date'], as_index=False).agg({'Theft-related crime':'sum', 'Violent-related crime':'sum', 'Drug-related crime':'sum'})


# curr_chart = make_subplots(specs=[[{"secondary_y": True}]])

# # Add traces
# curr_chart.add_trace(
#     go.Scatter(x=agg_dep_df['new_date'], y=agg_dep_df['num_deportations'], name="Number of deportations",
#     mode='lines'),
#     secondary_y=False,
# )

# curr_chart.add_trace(
#     go.Scatter(x=agg_crime_df['date'], y=agg_crime_df['Theft-related crime'], name="Number of theft-related crimes",
#     mode='lines'),
#     secondary_y=True,
# )

# # Add figure title
# curr_chart.update_layout(
#     title_text="Criminal deportations and theft-related crime"
# )

# # Set y-axes titles
# curr_chart.update_yaxes(title_text="Number of deportations", secondary_y=False)
# curr_chart.update_yaxes(title_text="Number of crimes", secondary_y=True)

# curr_chart.show()
# ###

# curr_chart = make_subplots(specs=[[{"secondary_y": True}]])

# # Add traces
# curr_chart.add_trace(
#     go.Scatter(x=agg_dep_df['new_date'], y=agg_dep_df['num_deportations'], name="Number of deportations",
#     mode='lines'),
#     secondary_y=False,
# )

# curr_chart.add_trace(
#     go.Scatter(x=agg_crime_df['date'], y=agg_crime_df['Violent-related crime'], name="Number of violent-related crimes",
#     mode='lines'),
#     secondary_y=True,
# )

# # Add figure title
# curr_chart.update_layout(
#     title_text="Criminal deportations and violent-related crime"
# )

# # Set y-axes titles
# curr_chart.update_yaxes(title_text="Number of deportations", secondary_y=False)
# curr_chart.update_yaxes(title_text="Number of crimes", secondary_y=True)

# curr_chart.show()
# ####
# curr_chart = make_subplots(specs=[[{"secondary_y": True}]])

# # Add traces
# curr_chart.add_trace(
#     go.Scatter(x=agg_dep_df['new_date'], y=agg_dep_df['num_deportations'], name="Number of deportations",
#     mode='lines'),
#     secondary_y=False,
# )

# curr_chart.add_trace(
#     go.Scatter(x=agg_crime_df['date'], y=agg_crime_df['Drug-related crime'], name="Number of drug-related crimes",
#     mode='lines'),
#     secondary_y=True,
# )

# # Add figure title
# curr_chart.update_layout(
#     title_text="Criminal deportations and drug-related crime"
# )

# # Set y-axes titles
# curr_chart.update_yaxes(title_text="Number of deportations", secondary_y=False)
# curr_chart.update_yaxes(title_text="Number of crimes", secondary_y=True)

# curr_chart.show()


# #### aggregate all states

# for index in enumerate(states_short):
#     curr_dep_df = deportation_data_raw[deportation_data_raw["state"] == states_short[index[0]]]
#     dep_cities = curr_dep_df["location"].unique()
#     curr_crime_df = crime_data_clean[crime_data_clean["state"] == states_long[index[0]]]
#     curr_crime_df['sum'] = curr_crime_df.iloc[:, 6:50].sum(axis=1)
#     crime_cities = curr_crime_df["city_name"].unique()
    
#     curr_dep_sub_df = curr_dep_df.groupby(['new_date'], as_index=False).agg({'num_deportations':'sum'})

#     curr_crime_sub_df = curr_crime_df.groupby(['date'], as_index=False).agg({'sum':'sum'})

#         # check jumps
#         # curr_df_indexed = curr_df.set_index("new_date")
#         # lag_df = curr_df_indexed.groupby(["location"]).shift(freq=pandas.DateOffset(months=1))
#         # curr_df.merge(lag_df, on=["location", "new_date"], how="left")
        
#         # curr_df.set_index(["location", "new_date"], inplace = True)
#         # lag_df = curr_df.rename(columns={"num_deportations": "num_deportations_lag"})
#         # lag_df = lag_df.groupby(level="location")["num_deportations_lag"].shift(1)
#         # curr_df = curr_df.join(lag_df)
        
#     #    curr_df["jump"] = curr_df.apply(is_jump, axis=1)

#     #    jump_date_list = curr_df[curr_df["jump"]]
#     #idea: remove the indexing, then create a dictionary of location-list of dates key-value pairs
#     curr_chart = make_subplots(specs=[[{"secondary_y": True}]])

#     # Add traces
#     curr_chart.add_trace(
#         go.Scatter(x=curr_dep_sub_df['new_date'], y=curr_dep_sub_df['num_deportations'], name="Number of deportations",
#         mode='lines'),
#         secondary_y=False,
#     )

#     curr_chart.add_trace(
#         go.Scatter(x=curr_crime_sub_df['date'], y=curr_crime_sub_df['sum'], name="Number of crimes",
#         mode='lines'),
#         secondary_y=True,
#     )

#     # Add figure title
#     curr_chart.update_layout(
#         title_text=f"Deportations and crime in {states_long[0]}"
#     )

#     # Set y-axes titles
#     curr_chart.update_yaxes(title_text="Number of deportations", secondary_y=False)
#     curr_chart.update_yaxes(title_text="Number of crimes", secondary_y=True)

#     curr_chart.show()

        # curr_chart = px.line(curr_sub_df, x = "new_date", y = "num_deportations", color = "conviction",
        #                      title=f"Deportations in {city}")
        # # curr_chart.add_vline(x=2.5, line_width=3, line_dash="dash", line_color="green")
        # curr_chart.show()
        # curr_chart.write_image(f"figures/deportations_by_city/{city.lower()}_chart.png")

# az_df = deportation_data_raw[deportation_data_raw["state"] == "AZ"]
# az_df = az_df.groupby(['new_date', 'location', 'citizenship'], as_index=False).agg({'num_deportations':'sum'})
# ca_df = deportation_data_raw[deportation_data_raw["state"] == "CA"]
# ca_df = ca_df.groupby(['new_date', 'location', 'citizenship'], as_index=False).agg({'num_deportations':'sum'})
# tx_df = deportation_data_raw[deportation_data_raw["state"] == "TX"]
# tx_df = tx_df.groupby(['new_date', 'location', 'citizenship'], as_index=False).agg({'num_deportations':'sum'})

# print("apple")

# Crime data -------------------------------------------------------------------

# files = [f for f in os.listdir("num_crimes_by_type/monthly/all_locations") if not f.startswith('.')]

# crime_data = pandas.io.stata.read_stata(f"num_crimes_by_type/monthly/all_locations/{files[0]}")
# for file in files[1:]:
#     crime_data_cur = pandas.io.stata.read_stata(f"num_crimes_by_type/monthly/all_locations/{file}")
#     crime_data = pandas.concat([crime_data, crime_data_cur], ignore_index=True)

# crime_data_clean = crime_data[['year','month', 'state', 'address_zip_code','agg_assault_tot_adult','agg_assault_tot_arrests','all_other_tot_adult','all_other_tot_arrests','burglary_tot_adult','burglary_tot_arrests','mtr_veh_theft_tot_adult','mtr_veh_theft_tot_arrests','murder_tot_adult','murder_tot_arrests','oth_assault_tot_adult','oth_assault_tot_arrests','poss_drug_total_tot_adult','poss_drug_total_tot_arrests','poss_heroin_coke_tot_adult','poss_heroin_coke_tot_arrests','poss_other_drug_tot_adult','poss_other_drug_tot_arrests','poss_synth_narc_tot_adult','poss_synth_narc_tot_arrests','rape_tot_adult','rape_tot_arrests','robbery_tot_adult','robbery_tot_arrests','runaways_tot_adult','runaways_tot_arrests','sale_cannabis_tot_adult','sale_cannabis_tot_arrests','sale_drug_total_tot_adult','sale_drug_total_tot_arrests','sale_heroin_coke_tot_adult','sale_heroin_coke_tot_arrests','sale_other_drug_tot_adult','sale_other_drug_tot_arrests','sale_synth_narc_tot_adult','sale_synth_narc_tot_arrests','stolen_prop_tot_adult','stolen_prop_tot_arrests','suspicion_tot_adult','suspicion_tot_arrests','theft_tot_adult','theft_tot_arrests','vandalism_tot_adult','vandalism_tot_arrests','weapons_tot_adult','weapons_tot_arrests']]
# crime_data_clean = crime_data_clean[crime_data_clean["state"].isin(["arizona", "california", "texas", "new york", "new jersey", "louisiana", "florida", "virginia"])]
# crime_data_clean = crime_data_clean[crime_data_clean["address_zip_code"] != ""]
# crime_data_clean = crime_data_clean.astype({'address_zip_code':'int', "agg_assault_tot_adult": "int", "agg_assault_tot_arrests": "int", "all_other_tot_adult": "int", "all_other_tot_arrests": "int", "burglary_tot_adult": "int", "burglary_tot_arrests": "int", "mtr_veh_theft_tot_adult": "int", "mtr_veh_theft_tot_arrests": "int", "murder_tot_adult": "int", "murder_tot_arrests": "int", "oth_assault_tot_adult": "int", "oth_assault_tot_arrests": "int", "poss_drug_total_tot_adult": "int", "poss_drug_total_tot_arrests": "int", "poss_heroin_coke_tot_adult": "int", "poss_heroin_coke_tot_arrests": "int", "poss_other_drug_tot_adult": "int", "poss_other_drug_tot_arrests": "int", "poss_synth_narc_tot_adult": "int", "poss_synth_narc_tot_arrests": "int", "rape_tot_adult": "int", "rape_tot_arrests": "int", "robbery_tot_adult": "int", "robbery_tot_arrests": "int", "runaways_tot_adult": "int", "runaways_tot_arrests": "int", "sale_cannabis_tot_adult": "int", "sale_cannabis_tot_arrests": "int", "sale_drug_total_tot_adult": "int", "sale_drug_total_tot_arrests": "int", "sale_heroin_coke_tot_adult": "int", "sale_heroin_coke_tot_arrests": "int", "sale_other_drug_tot_adult": "int", "sale_other_drug_tot_arrests": "int", "sale_synth_narc_tot_adult": "int", "sale_synth_narc_tot_arrests": "int", "stolen_prop_tot_adult": "int", "stolen_prop_tot_arrests": "int", "suspicion_tot_adult": "int", "suspicion_tot_arrests": "int", "theft_tot_adult": "int", "theft_tot_arrests": "int", "vandalism_tot_adult": "int", "vandalism_tot_arrests": "int", "weapons_tot_adult": "int", "weapons_tot_arrests": "int"})
# crime_data_clean["city_name"] = crime_data_clean["address_zip_code"].apply(zipcode_to_city)
# crime_data_clean["date"] = crime_data_clean.apply(strings_to_date, axis=1)

# # columns we're interested in: ['year','month','address_zip_code','agg_assault_tot_adult','agg_assault_tot_arrests','all_other_tot_adult','all_other_tot_arrests','burglary_tot_adult','burglary_tot_arrests','mtr_veh_theft_tot_adult','mtr_veh_theft_tot_arrests','murder_tot_adult','murder_tot_arrests','oth_assault_tot_adult','oth_assault_tot_arrests','poss_drug_total_tot_adult','poss_drug_total_tot_arrests','poss_heroin_coke_tot_adult','poss_heroin_coke_tot_arrests','poss_other_drug_tot_adult','poss_other_drug_tot_arrests','poss_synth_narc_tot_adult','poss_synth_narc_tot_arrests','rape_tot_adult','rape_tot_arrests','robbery_tot_adult','robbery_tot_arrests','runaways_tot_adult','runaways_tot_arrests','sale_cannabis_tot_adult','sale_cannabis_tot_arrests','sale_drug_total_tot_adult','sale_drug_total_tot_arrests','sale_heroin_coke_tot_adult','sale_heroin_coke_tot_arrests','sale_other_drug_tot_adult','sale_other_drug_tot_arrests','sale_synth_narc_tot_adult','sale_synth_narc_tot_arrests','stolen_prop_tot_adult','stolen_prop_tot_arrests','suspicion_tot_adult','suspicion_tot_arrests','theft_tot_adult','theft_tot_arrests','vandalism_tot_adult','vandalism_tot_arrests','weapons_tot_adult','weapons_tot_arrests']

# # plot data

# states = ["arizona", "california", "texas", "new york", "new jersey", "louisiana", "florida", "virginia"]
# for state in states:
#     curr_df = crime_data_clean[crime_data_clean["state"] == state]
#     curr_df['sum'] = curr_df.iloc[:, 6:50].sum(axis=1)
#     curr_df = curr_df.groupby(['city_name', 'date'], as_index=False).agg({'sum':'sum'})

#     curr_chart = px.line(curr_df, x = "date", y = "sum", color = "city_name")
#     curr_chart.show()
#     curr_chart.write_image(f"figures/crime_by_city/{state.lower()}_chart.png")

# # az_df = deportation_data_raw[deportation_data_raw["state"] == "AZ"]
# # az_df = az_df.groupby(['new_date', 'location', 'citizenship'], as_index=False).agg({'num_deportations':'sum'})
# # ca_df = deportation_data_raw[deportation_data_raw["state"] == "CA"]
# # ca_df = ca_df.groupby(['new_date', 'location', 'citizenship'], as_index=False).agg({'num_deportations':'sum'})
# # tx_df = deportation_data_raw[deportation_data_raw["state"] == "TX"]
# # tx_df = tx_df.groupby(['new_date', 'location', 'citizenship'], as_index=False).agg({'num_deportations':'sum'})

# print("apple")

# q2 is a massive improvement, aybe tthe seasonals is 
# srvices & manufacturing rise

# how do the seeasonals differ

