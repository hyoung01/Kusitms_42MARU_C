import re
text = input()

date = re.compile(r"""
                (오늘|내일|어제|금일) #오늘
                |(\d+년\s\d+월\s\d+일) #날짜
                |(\d+월\s\d+일) #월
                |([ㄱ-ㅣ가-힣]요일)#요일
                """, re.VERBOSE)
date_period = re.compile(r"""
                        (이번[주해월])
                        |(다음[주해월])
                        |(저번[주해월])
                        |(올해|작년|내년|전년|주말|평일|내후년)
                        |((\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?부터\s(\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?까지)
                        |((\d+년\s?)(\d+월)?)
                        """, re.VERBOSE)
date_lunar = re.compile(r"""
                        음력\s@sys.date.period #꼼수 쓸려헀는데 망함ㅎ 수정필요
                        | 음력\s@sys.date 
                        | 음력\s(설|추석)
                        """, re.VERBOSE)
date_period_lunar = re.compile(r'음력\s\d+월')

#time = re.compile(r'(정오)?(오전)?((\d+분|\d+시|\d+초)\s+뒤?)?')
#time_period = re.compile(r'((오전|오후)?)*\s?((아침|점심|저녁)?)*\s?((\d+시부터\s?\d+시까지)?)')
#date_time = re.compile(r'(내일|현재|오늘|모레|(\d+월\s?\d일))?\s((오전|오후)?\s?((\d+시)?\s?(\d+분)?))?')
#date_time_period=re.compile(r'(([월화수목금토일]요일)|오늘|내일|모레|글피|어[제|젯]|(\d+월\s?\d일))?\s?((낮|밤|저녁|오전|오후)?)*\s?((아침|점심|저녁)?)*\s?((\d+시부터\s?\d+시까지)?)')
#number=re.compile(r'((일|이|삼|사|오|육|칠|팔|구|십)?|(하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉)?)*(((\d+)(명|개))?((하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉)\s?(명|개))?)*(열명|열개)?')
#number_times=re.compile(r'(\d+(화|부|편|차|회|회차))')
#number_percent=re.compile(r'(\d+(퍼센트|프로|%))')


number_ordinal = re.compile('(\d+번)|(첫?두?세?네?(열|(스[무|물])|(서른)|(마흔)|(쉰)|(예순)|(일흔)|(여든)|(아흔))?\s?[한두세네]?(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?\s?번째)')
number_age = re.compile('(\d+[살세])|(((열)?(스[무물])?(서른)?(마흔)?(쉰)?(예순)?(일흔)?(여든)?(아흔)?)\s?([한두세네]*(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?)\s?살)')
number_birthyear = re.compile('\d{1,4}년생')
number_rank = re.compile('\d+[등위]')
number_decade = re.compile('\d{1,4}년대')
unit_length = re.compile('\d+\.?\d*\s?((mm|(밀리미터))|((?!cm²)cm|(센티미터))|((?!m²)m|(미터))|((?!km²)km|(킬로미터))|(in|(인치))|((?!ft²)ft|(피트))|((?!yd²)yd|(야드))|(ch|(체인))|(fur|(펄롱))|(mile|(마일)))')
unit_area = re.compile('\d+\.?\d*\s?((m²|(제곱미터))|(a|(아르))|(ha|(헥타르|(헥타아르)))|(km²|(제곱킬로미터))|(ft²|(제곱피트))|(yd²|(제곱야드))|(ac|(에이커))|(평)|(단)|(정))')
#은비
unit_weight = re.compile(r"""
    \d+\s?mg|\d+\s?g|\d+\s?kg|\d+\s?t|\d+\s?kt|\d+\s?gr|\d+\s?oz|\d+\s?lb
    |\d+\s?milligram|\d+\s?gram|\d+\s?kilogram|\d+\s?tonne|\d+\s?metric ton|\d+\s?kiloton|\d+\s?grain|\d+\s?ounce|\d+\s?pound
    |\d+\s?밀리그램|\d+\s?그램|\d+\s?킬로그램|\d+\s?톤|\d+\s?킬로톤|\d+\s?그레인|\d+\s?온스|\d+\s?돈|\d+\s?냥|\d+\s?근|\d+\s?관
    |\d+錢|\d+兩|\d+斤|\d+貫
""", re.VERBOSE)

unit_volume = re.compile(r"""
(\d+\s?cc|\d+\s?mℓ|\d+\s?ml|\d+\s?dℓ|\d+\s?dl|\d+\s?ℓ|\d+\s?l|\d+\s?cm3|\d+\s?m3|\d+\s?in3|\d+\s?ft3|\d+\s?yd3|\d+\s?gal|\d+\s?gallon|\d+\s?bbl|\d+\s?barrel|\d+\s?fl. oz.|\d+\s?fl)
|(\d+\s?시시|\d+\s?밀리리터|\d+\s?데시리터|\d+\s?리터|\d+\s?세제곱센티미터|\d+\s?세제곱미터|\d+\s?세제곱인치|\d+\s?세제곱피트)
|(\d+\s?세제곱야드|\d+\s?갤런|\d+\s?배럴|\d+\s?액량 온스|\d+\s?홉|\d+\s?되|\d+\s?말|\d+\s?섬)
|(\d+\s?cubic centimeter|\d+\s?milliliters|\d+\s?deciliter|\d+\s?liter|\d+\s?cubic centimetre|\d+\s?fluid ounce)
|(\d+\s?gallon|\d+\s?barrel)
|(\d+升|\d+斗|\d+苫)
""", re.VERBOSE)

unit_pressure = re.compile(r"""
(\d+\s?atm|\d+\s?Pa|\d+\s?hPa|\d+\s?kPa|\d+\s?MPa|\d+\s?dyne/cm2|\d+\s?mb|\d+\s?\d+\s?bar|\d+\s?kgf/cm2|\d+\s?psi|\d+\s?\d+\s?mmHg|\d+\s?inchHg|\d+\s?mmH2O|\d+\s?inchH2O)
|(\d+\s?기압|\d+\s?파스칼|\d+\s?헥토파스칼|\d+\s?킬로파스칼|\d+\s?메가파스칼|\d+\s?다인/제곱센티미터|\d+\s?밀리바|\d+\s?바)
|(\d+\s?킬로그램힘/제곱센티미터|\d+\s?프사이|\d+\s?수은주밀리미터|\d+\s?수은주인치|\d+\s?수주밀리미터|\d+\s?수주인치)
|(\d+\s?atmospheric pressure|\d+\s?pascal|\d+\s?hectopascal|\d+\s?kilopascal|\d+\s?megapascal|\d+\s?dyne/square centimeters)
|(\d+\s?millibar|\d+\s?kgf/square centimeters|\d+\s?pound per square inch|\d+\s?millimeter of mercury|\d+\s?inch of mercury)
|(\d+\s?millimeter of water|\d+\s?inch of water)
""", re.VERBOSE)

unit_temperature = re.compile(r"""
(\d+\s?°C|\d+\s?°F|\d+\s?K|\d+\s?°R)
|(\d+\s?섭씨온도|\d+\s?화씨온도|\d+\s?절대온도|\d+\s?란씨온도|\d+\s?도)
|(\d+\s?celsius|\d+\s?centigrade|\d+\s?fahrenheit scale|\d+\s?kelvin|\d+\s?rankine)
""", re.VERBOSE)

unit_speed = re.compile(r"""
(\d+\s?m/s\d+\s?|m/h|\d+\s?km/s|\d+\s?km/h|\d+\s?in/s|\d+\s?in/h|\d+\s?ft/s|\d+\s?ft/h|\d+\s?mi/s|\d+\s?mi/h|\d+\s?kn|\d+\s?mach)
|(\d+\s?미터 매 초|\d+\s?미터 매 시|\d+\s?킬로미터 매 초|\d+\s?킬로미터 매 시|\d+\s?인치 매 초|\d+\s?인치 매 시|\d+\s?피트 매 초|\d+\s?피트 매 시)
|(\d+\s?마일 매 초|\d+\s?마일 매 시|\d+\s?노트|\d+\s?마하)
|(\d+\s?meter per second|\d+\s?meter per hour|\d+\s?kilometer per second|\d+\s?kilometer per hour|\d+\s?inch per second|\d+\s?inch per hour)
|(\d+\s?feet per second|\d+\s?feet per hour|\d+\s?mile per second|\d+\s?mile per hour|\d+\s?knot|\d+\s?mach)
""", re.VERBOSE)

unit_data = re.compile(r"""
(\d+\s?it|\d+\s?B|\d+\s?KB|\d+\s?KiB|\d+\s?MB|\d+\s?MiB|\d+\s?GB|\d+\s?GiB|\d+\s?TB|\d+\s?TiB|\d+\s?PB|\d+\s?PiB|\d+\s?EB|\d+\s?EiB|\d+\s?ZB|\d+\s?ZiB|\d+\s?YB|\d+\s?YiB)
|(\d+\s?비트|\d+\s?바이트|\d+\s?킬로바이트|\d+\s?키비바이트|\d+\s?메가바이트|\d+\s?메비바이트|\d+\s?기가바이트|\d+\s?기비바이트|\d+\s?테라바이트|\d+\s?테비바이트)
|(\d+\s?페타바이트|\d+\s?페비바이트|\d+\s?엑사바이트|\d+\s?엑비바이트|\d+\s?제타바이트|\d+\s?제비바이트|\d+\s?요타바이트|\d+\s?요비바이트)
|(\d+\s?byte|\d+\s?kilobyte|\d+\s?kibibyte|\d+\s?megabyte|\d+\s?mebibyte|\d+\s?gigabyte|\d+\s?gibibyte|\d+\s?terabyte|\d+\s?tebibyte|\d+\s?petabyte|\d+\s?pebibyte|\d+\s?exabyte)
|(\d+\s?exbibyte|\d+\s?zettabyte|\d+\s?zebibyte|\d+\s?yottabyte|\d+\s?yobibyte)
""", re.VERBOSE)

unit_energy = re.compile(r"""
(\d+\s?J|\d+\s?cal|\d+\s?kcal|\d+\s?Wh|\d+\s?kWh|\d+\s?eV|\d+\s?erg|\d+\s?Mhz|\d+\s?kHz)
|(\d+\s?줄|\d+\s?칼로리|\d+\s?킬로칼로리|\d+\s?와트시|\d+\s?킬로와트시|\d+\s?마력|\d+\s?에르그|\d+\s?전자볼트)
|(\d+\s?electron Volt)
""", re.VERBOSE)

unit_currency = re.compile(r"""
(\d+\s?원|\d+\s?달러|\d+\s?위안|\d+\s?센트|\d+\s?파운드|\d+\s?엔|\d+\s?유로|\d+\s?프랑|\d+\s?루피)
|(\S+\s?원|\S+\s?달러|\S+\s?위안|\S+\s?센트|\S+\s?파운드|\S+\s?엔|\S+\s?유로|\S+\s?프랑|\S+\s?루피)
""", re.VERBOSE)
#돼?1파운드 잡힘 -> 왜 \S지??

fortune_starsign = re.compile('[양|황소|쌍둥이|게|사자|처녀|천칭|전갈|궁수|염소|물병|물고기]+자리')
fortune_zodiac = re.compile('[쥐|소|호랑이|토끼|용|뱀|말|양|원숭이|닭|개|돼지]+띠')
currencyname = re.compile(r"""
                          ([ㄱ-ㅣ가-힣]+달러)
                          |(엔|유로|위안|파운드)
                          |([ㄱ-ㅣ가-힣]+페소)
                          |([ㄱ-ㅣ가-힣]+실링)
                          """, re.VERBOSE)
#달러 못잡음
#엔 -> @sys.currencyname  @sys.unit.currency 두 개 잡힘
#근데 이거 redis에 넣어둬야할듯 넘 많아

currency_code = re.compile('[A-Z]{3}')
url = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
bussiness_number = re.compile('([0-9]{3})-?([0-9]{2})-?([0-9]{5})')
phone_number = re.compile('01[0|1|6|7|8|9?]-?[0-9]{4}-?[0-9]{4}')
licenseplate_number = re.compile(r'\d{2,3}\s?[ㄱ-ㅣ가-힣]\s?\d{4}')

regexes = {

    '@sys.date' : date,
    '@sys.date.period' : date_period,
    '@sys.date.lunar' : date_lunar,
    '@sys.date.period.lunars' : date_period_lunar,
    #'@sys.time' : time,
    #'@sys.time.period' : time_period,
    #'@sys.date.time' : date_time,
    #'@sys.date.time.period' : date_time_period,
    #'@sys.number' : number,
    #'@sys.number.times' : number_times,
    #'@sys.number.percent' : number_percent,
    '@sys.number.ordinal': number_ordinal,
    '@sys.number.age': number_age,
    '@sys.number.birthyear': number_birthyear,
    '@sys.number.rank': number_rank,
    '@sys.number.decade': number_decade,
    '@sys.unit.length': unit_length,
    '@sys.unit.area': unit_area,

    '@sys.unit.weight' : unit_weight,
    '@sys.unit.volume' :unit_volume,
    '@sys.unit.pressure':unit_pressure,
    '@sys.unit.temperature' : unit_temperature,
    '@sys.unit.speed' : unit_speed,
    '@sys.unit.data' : unit_data,
    '@sys.unit.energy' :unit_energy,
    '@sys.unit.currency' : unit_currency,

    '@sys.fortune.starsign' : fortune_starsign,
    '@sys.fortune.zodiac' : fortune_zodiac,
    '@sys.currencyname' : currencyname,
    '@sys.currency.code' : currency_code,
    '@sys.url' : url,
    '@sys.bussiness.number' : bussiness_number,
    '@sys.phone.number' : phone_number,
    '@sys.licenseplate.number' : licenseplate_number,

}

def priRegex(text):
    tagged_sentence = text
    entitiy_name_list = []
    value = []
    start_idx = []
    end_idx = []

    for k, v in list(regexes.items()):

        m = v.finditer(text)

        for i in m:

            if i.start() in start_idx: #최단 지우고, 최장으로 변경
                idx = start_idx.index(i.start())
                tagged_sentence = tagged_sentence.replace(entitiy_name_list[idx], value[idx]) #entity -> 원래 value로 치환
                value[idx]= i.group() #value 리스트 수정
                entitiy_name_list[idx] = k #entity 리스트 수정
                end_idx[idx] = i.end() - 1 #end_idx 갱신
                tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k) #tagged_sentence 수정

            else: #처음 추가
                entitiy_name_list.append(k)
                start_idx.append(i.start())
                value.append(i.group())
                end_idx.append(i.end()-1)
                tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k)


    for i in range(len(entitiy_name_list)):
        print('entitiy name =', entitiy_name_list[i])
        print('value = ', value[i])
        print('start_idx = ',start_idx[i])
        print('end_idx = ',end_idx[i])
        print('----')

    print(tagged_sentence)

priRegex(text)
'''
    print("entity_name: @{name}".format(name=sys._getframe().f_code.co_name)) #entity_name
    p = re.compile('올해|년|작년|월|일') #대체 대상 추가 가능
    someValue =p.sub('-',value)
    if someValue[0] is '-':
        someNewValue = someValue[1:-1]+" 00:00:00"
    else:
        someNewValue = someValue[0:-1]+" 00:00:00"
    print("value: "+ someNewValue)           #value
    
    print("start_idx: "+str(match.start()))  #start_idx
    print("end_idx: "+str(match.end()))      #end_idx 
    
    #print("tagged_sentence:")      
    
    #value값들 List자료로 묶어서취합 
sys_date()

'''