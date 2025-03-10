import random
from Crypto.Util.number import *
m = bytes_to_long(b'NSSCTF{******}')
e = 3
cnt = 5
A = [random.randint(1, 128) for i in range(cnt)]
B = [random.randint(1, 1024) for i in range(cnt)]
Cs = []
Ns = []
ds = []
for i in range(cnt):
    p = getPrime(1024)
    q = getPrime(1024)
    N = p * q
    Ns.append(N)
    c = pow(A[i] * m + B[i], e, N)
    Cs.append(c)

print(f'Cs = {Cs}')
print(f'Ns = {Ns}')
print(f'A = {A}')
print(f'B = {B}')

'''
Cs = [3883550483902420926234302242195949363902226654053022494278088796963093148922544154652393440710324453957805003804862341179812753736616349557399185135880313324078548975985811806182903172952051652658588498612963004980264760087430598878125976827727487812798234711111712162020259061748840871764150680864715622600474900724019717, 44236067230701013362887598977513235723198800481322709348886355202907732899445854511587419035591039483362973933824325371001141984765195796979842132811747908218486539899605454036424269293612496645594202012384509417494958938609654993954815298870367636552785788956298375017694826184378792550191638399421497826339423606821604157, 6357650953899476167368901224389387403906446759598372329485772462484633677698135444868033121301336092469156582681179266678600618088894651608959308419170191169045155695737438290373562868522834196889856654007109891894017495798358315308038562408520108440771857096111507359080036538511243240503551392124933753089110476128205879, 22113876206623661433094377745740418662890776774627724662206682745097788065566600734855556673140969239465263787646309908630165398806037735405429975451284487302914604239730662891329034924321076102542709261476260968369261179396546360622009680551846353241542278987410340410787241742872482813920394082039159494900989803139848, 3482139402999788223900773097355269284333433274039980036209713091774078099956379218113295375979469580323031564990774054948555715060182912479470463142901382767332589017162687376944227096536463901792518843690268101660074429034365722795293704792196728134808253362549344588424246863639211005569740713503298812433885633339928000]
Ns = [16475947720089128737086499038994656469812989231809435921247088488421456071533054401942524421620331649062071397844226728071767213827034006847771426419523100773295773164564476217357610574522713490589578290280800714302496527429690267342283298617108512673396866659851168908725556917773195601048972304412711680140760801040935590195586074637385222382292803661244860123231496798860777536415139625565081790463543592610972293444445484103576151223863074744798386995109810985102707212603792744509634887671301358727199987659311189567616661188675145831286196163294361139604739930788248190209148634033965292667427275010588011907449, 20577756967813119473983751142406348831049793754920537415005815223703461130310397180758312537008616509869607815711902558904863798387297921980544196445945053155779852988514975874071063143079007922739179751830691324912287324521191080786349595537328978318940405478035852622078260078106150355838894304903666410802941404171580632337325226810035755441751019274785623857299274197733366157959314887828355684391955406242669453470960096408521602483306976326328443227588146790803825249363494429478920856868334932355802422905860734038456902208606699044555491079703407805059303577939602439962034474867810455961978123428573930309579, 25378900199358568547963276996842869295995268651191814514603221510827400166103120330924988917554751086130358554721062101701515825946297524373525439060420148179742729309006073061967296139229954269726231365437710075337125457376990188019604789882474361937774315087501386157518068677103700336670450539759041322742305750381808526633011613014316600728378154635620303486714630541107978228937765593165029293600696974317531575469630789089360595175501977260250968161370460576429760743419177492425307438895058834861598683601140950473599184767494278677563047031229859204765208419798131798581975676005652781036214330956450007099403, 9926930930542540303568927026135349869339912234415090245441062010278559018661286180235901235221302260175325531516014675014545716516533078219977130807590578846757066721033900594646767488495122383467444918251577083210413483316448060657426105745966157951221212755678202988755054192555411944547922101946719460879213184073264876177559979901796761414990531875287201475974601204234252323254624416703924391519239658714195344209537776288504410483034555245167972866281710032749023882686703242857598745646748066876170805806058616787854614797120972981188197354785585317082619741063413472652781873599900240100437586392949061248911, 20830107058752240343833750223075661528901765032886427653372256688107333986271844745610709207164953960695218903201021174901973495649232416991828815735226979007977454196096030222267886398005100472650709789400722193947140354500257454594031250139843254349174343293378469322212240525155348525032929797789787100019790044104691478313003888625343348575779856701393153928092199647854293030744711864943595605801812851745568294572509414459253058726953902809163955547592002726224051451969415362170516701646937298176613945563863745599843208814303891064544739910893746169725919856235296428308161065429422882694228900677440053029677]
A = [56, 126, 66, 10, 54]
B = [261, 191, 877, 352, 62]
'''