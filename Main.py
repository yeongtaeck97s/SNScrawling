import Daum
import Naver
import time
import Twitter

def text():
    text = '셀트리온'
    return text

# 사전을 추가해야함.
def sajun():
    sajun = ['트와이스', 'kf94', 'KF94', 'Kf94', 'kF94', '타임라인', '확진자', '예방수칙', '코로나19', 'corona19', 'Corona19',
             '개소리', '판매', '제품', '쿠팡', 'kf94마스크', 'KF94마스크', 'Kf94마스크', 'kF94마스크',
             '우한폐렴', '신종코로나', '신종코로나바이러스', 'coronavirus', 'Coronavirus', '사재기',
             '복지부장관', '바이러스', '피해복구', '이만희', '문재인', '이재갑', '한림대',
             '감염내과', '교수님', '정치인', '입국금지', '대변인', '청와대', '문대통령', '황기자', '신천지', '근로장려금',
             '까페', '배달', '페미', '항체', '에휴', '미래통합당', '자유한국당', '민주통합당', '3사',
             '이동통신', '갤럭시', '갤럭시S20', '감염병', '난리', '순방', '신천지','신천지사이트','쿠팡',
             '쿠팡플렉스', 'coupang flex', '배급제', '1인2매','마스크','이덴트','수출길','마스크5부제',
             '신천지연예인명단','신천지연예인','세계여성의날','식약처','양금희','시진핑','주석',
             '보건당국','구로콜센터','실거래','공적마스크','WHO','사무총장','큐넷','팬데믹','펜대믹','팬대믹',
             'pandemic','Pandemic','1800선','코스피','코스피하락','최악','급락','트럼프','cospi','cosdac','사이드카',
             '망했다','10년전','IMF','거품','금융버블','금융위기','붕괴','순매수','순매도','공매도','공매도금지법',
             '금융위원회', '한국거래소', '주지훈', '하이에나','은혜의강교회','사이비종교','집단감염','신도','카톡','카톡에러',
             '개학연기','신형아반떼','현대자동차','아반떼','Avante','1500선붕괴','1400선','n번방','n번방사건','텔레그램',
             '소신발언','벗방','그것이알고싶다','카르텔','사이버성폭력','강력처벌','BJ','그알','셀트리온','코로나항체','항체개발',
             '7월내']
    return sajun


if __name__ == '__main__':
    Naver.naver()
    time.sleep(2)
    Daum.daum()
    time.sleep(2)
    Twitter.twitter()