import os, sys, re
import pymongo
from bson.objectid import ObjectId

# variables
COLLECTION = "files"
QUERY_ID = sys.argv[1]
DUMMY = {
  "title": "테스트 단편들 모음",
  "data": [
    {
      "chapter_num": 1,
      "chapter_name": "9급 좀비의 마지막 밤",
      "chapter_contents": [
        {
          "text": "', '', '9급 좀비들은 뛰지 못한다. 시속 3km 이하로 걸어가야 한다. 낼 수 있는 소리는 어, 으, 에와 같은 모음 종류뿐이다. 또, 팔꿈치를 한 번에 30도 이상 움직이지 못한다. 재빠르게 팔을 휘둘려 인간을 잡아챌 수 없다. 그냥 움직여야만 한다. 9급 좀비들은 3교대 근무를 선다. 하루에 8시간 이상 근무를 하는데 앉아 있거나 인간이 나오지 않는 지점에서 서성거리고 있으면 경고를 받는다.",
          "emotion": 0
        },
        {
          "text": " 경고가 3번 이상 쌓이면 1개월 감봉을 당한다. 보통 일주일에 한두번은 인간들에게 머리가 터지거나 팔이나 내장을 뜯기거나 한다. 가끔 헌팅에 성공하여 승진을 하는 동료들도 보았지만 대부분의 9급 좀비들은 한달에 한번씩 신체 재생을 위한 병가를 내는 실정이다. 하지만 10급 기능직 좀비들에 비하면 9급은 훌륭한 편이다. 10급 기능직 좀비들은 다리나 팔같은 신체가 없어 기어 다니다가 인간들이 몰고 다니는 자동차에 박살이 나기 일쑤이기 때문이다.",
          "emotion": 0
        },
        {
          "text": " 10급 기능직 좀비들은 인간에게 100번 정도 신체가 훼손되고 나면 좀비로서 퇴직하고 상위 좀비들의 신체 재생을 위한 재료로 쓰이게 된다. 가끔 인권위에서 10급 좀비들에게도 생명으로서 재생할 수 있는 가치를 부여해야 한다는 성명을 발표하긴 하지만 노동계층의 밑바닥은 존재해야 하기에 노동절 전후로만 나오는 쇼에 불과한 실정이다.', '', '처음 9급 좀비로 임용되었을 때만 하더라도 매일같이 사무관 좀비로의 승진을 상상하곤 하였지만 9급 생활만 5년차가 되다보니 지금의 생활에 안주하게 되었다.",
          "emotion": 0
        },
        {
          "text": " 30년차가 되면 은퇴를 할 수 있고 죽을 때까지 한 달에 고양이 3마리를 연금으로 받을 수 있다. 또, 일년에 한번씩 인간들이 가득 찬 테마파크에서 신나게 인간들의 팔다리를 물어뜯을 수 있는 멋진 휴가를 보낼 수 있다.  단 한명의 인간을 물어뜯기 위해 달려드는 수 많은 좀비들이 모두 멋진 노후를 위한 것이라는 상상을 해보았는가? 9급 좀비들은 그러하다.",
          "emotion": 0
        },
        {
          "text": " 한 번은 인간 한명을 물어뜯기 위해 천명이 넘는 좀비들이 달려든 적도 있었다.  난 5년간 딱 4번 인간의 어깨를 잡아보았다. 한 번은 목덜미 3cm까지 얼굴을 들이댄 적도 있었다. 8급 승진의 꿈을 꾸며 잠시 주춤하던 사이 곡괭이가 내 얼굴을 도려냈었다. 한달간 신체 재생을 하며 누워있는 동안 아쉬움으로 계속해서 눈에서 고름이 흘려 내렸다. 가끔 인적이 드문 숲 속을 한달을 헤맨 9급 좀비가 긴장이 풀려있는 인간을 물었다는 기념비적인 사건이 생기기도 한다.",
          "emotion": 0
        },
        {
          "text": " 처음 그 영웅담이 퍼졌을 때 너나할 것 없이 모두 숲으로 몰려들었던 이른바 포레스트 러시가 있었다. 그 때 숲 속으로 떠났던 수많은 9급 좀비들이 인간들의 부비트랩에 걸려 산채로 불태워 졌다. 그후 신체 재생은 고사하고 목숨을 잃은 좀비들은 숲 속으로 헌팅을 가는 것을 두려워하게 되었다.', '', '도시의 먹을거리가 사라지자 도시에선 인간들이 잡히지 않고 있다.",
          "emotion": 0
        },
        {
          "text": " 급여 지급조차 어려워져 상급 좀비들의 명예 퇴직 신청이 계속되고 있다. 그래서였을까. 어제 5급 사무관 좀생이가 9급들을 모아 위에서 내려온 공문을 읽어주었다. 발령이었다. 산 너머 있는 인간들의 거주지 인근으로. 우리들은 모두 두려움에 떨었고 다시는 돌아오지 못할 것이라는 공포에 휩쌓였다. 그나마 다행이었던 것은 5급 이하 모든 좀비들이 숲 속 인간들의 거주지로 떠난다는 것이었다.",
          "emotion": 0
        },
        {
          "text": " 5급 사무관들은 시속 40km까지 속도를 내어 달릴 수 있고, 강력한 턱뼈와 날카로운 손톱으로 인간 하나쯤은 손쉽게 찢어버릴 수 있는 자들이다. 하지만, 그들은 너무 소수이기에 인간들이 힘을 모아 덤벼들면 무참히 살해되곤 하였다. 그 날 회의를 끝내고 돌아오며 숲 속을 들어가게 될 경우 다시 이 도시로 돌아오지 못할 것이라는 기분이 들었다. 임용 동기들이 시체주로 한 잔하자며 연락이 왔다.",
          "emotion": 0
        },
        {
          "text": " 하지만, 지금은 취하고 싶지 않기에 홀로 집으로 돌아가기로 하였다. 고름으로 가득 찬 욕조에 들어가 몸을 푹 담궜다. 질퍽거리는 질감이 온 몸을 감돈다. 이제 내일 동이 틀 때면 우리 도시의 9급 좀비 수천명은 숲 속을 향해 에, 아, 우, 이 등의 소리를 내며 시속 3km로 걸어 들어갈 것이다. 다시 돌아올 수 있을지 모르겠지만 몇 몇은 8급이나 7급으로 승진을 할 수도 있을 것이다.",
          "emotion": 0
        },
        {
          "text": " 그런 행운이 나에게 오길 바라며 고름 욕조로 온 몸을 담근다.', '', .",
          "emotion": 0
        }
      ]
    },
    {
      "chapter_num": 2,
      "chapter_name": "나이트 형제",
      "chapter_contents": [
        {
          "text": "', '', '라이트 형제', 'Wilbur(형) 1867∼1912, Orville(아우) 1871∼1948  미국의 기술자, 비행기 발명가. 형제가 모두 공작에 취미가 있고 의가 좋아, 이미 소년 시절에 함께 인쇄기를 만들어 조그마한 신문을 발행하기도 하였다. 뒤에 공동으로 기계완구와 자전거 공장을 경영하다가, 1896년에 독일의 릴리엔탈이 글라이더 시험 중 떨어져 죽었다는 소문을 들었다.",
          "emotion": 0
        },
        {
          "text": " 이 소문에 자극을 받은 형제는 비행기의 연구와 실험을 계속하여 1900년에 제1호기, 이어 제2, 3호기를 만들어 시험하였다. 1903년에는 최초의 동력 비행기를 완성시켜 ‘플라이어호’라 이름 지었다. 그 해 12월 17일에 동생이 플라이어호로 36m를 날아 인류 최초로 동력기에 의한 비행에 성공하였다. 이듬해 그들 형제는 ‘아메리칸 라이트 비행기 제작 회사’를 세웠다.",
          "emotion": 0
        },
        {
          "text": "', '', '이 이야기는 비행(飛行)에 관한 이야기 이다.', '', \"'몇 분이시죠' 라는 말에 나는 주위를 둘러보았지만 분명 아무도 없었다. 나 혼자였다. 내게 조금 떨어진 곳에 지독한 냄새만을 가지고 있을 것 이라는, 지극히 정상적인 상상만이 가능한 쓰레기통과 몸이 부서질 때까지 평생 콜라캔 만 내뱉는 고지식 덩어리가 있긴 했지만 내 일행은 아니였다.",
          "emotion": 0
        },
        {
          "text": "뭐 웨이터의 잘못은 아니다. 혼자서 나이트를 오는 멍청이는 그다지 많지 않다. 이유가 있으면 모를까.\", '', '물론 난 이유가 있는 쪽이다. 그러니 멍청이도 아니였다.두달전에 집을 뛰쳐나온 형을 찾아 온것이다.며칠전 이웃집의 빨강머리가 우리 형을 이곳에서 봤다고 얘기해 주었다. 꿈을 접고 집을 뛰쳐나와 고작 나이트클럽 이라니,이해 할 수가 없다. 형은 왜 이곳으로 온 것일까.",
          "emotion": 0
        },
        {
          "text": "더이상 꿈은 꾸지 않을 생각인가. 왜 다시 날아보려 하지 않고 집을 뛰쳐나온 것인가. 형을 설득해 볼 생각이다. 형의 이름은 Wilbur 그리고 난 Orville 이다.', '', '입구에 들어서자마자 비명소리와 같은 음악소리가 귀에 들린다. 귀가 찢어질 것만 같다. 나이트 안은 굉장히 붐볐다.춤을추는 사람들, 웨이터의 손에 이끌려 이리저리 자리를 옮겨 다니는 사람들.",
          "emotion": 0
        },
        {
          "text": " 대화를 하는 사람들은 찾아 볼수 없다. 모두 비명소리 같은 음악 때문이다.', '', '언젠가 들은 얘긴데, 젖소들 에게도 음악을 틀어 준다고 한다. 다량의 젖을 생산해 내기 위해서 라고 한다. 이 찢어질 듯 한 비명 같은 음악소리는 다량의 젖을 위해서 인가. 만약 그렇다면 조금 짜거나 싱거울 것이다. 그러기 위해 소금공장이 있는게 아닌가. 기업이 있는거 아니겠는가.",
          "emotion": 0
        },
        {
          "text": " 그나저나 Wilbur 형이 보이지 않는다. 한가하게 서 있을 처지는 아닌가 보다. 아니면 다량의 젖을 품고 있는 암소의 젖을 짜고 있을지도 모르겠다.다량의 젖을 생산하는 암소 생각할 틈이 없다. 귀가 귀가 찢어질 것 같다.', '', '술에 취해, 비명소리 같은 음악에 몸과 마음을 빼앗기고 흔들리는 사람들 틈에서 암소를 끌고 있는, 아니 취한 여자 손님의 팔을 잡고 있는 Wilbur 형이 보인다.",
          "emotion": 0
        },
        {
          "text": " 암소는 짐짓 싫다고 하지만 그저 시늉뿐이다. 암소는 취한 척 하며 형의 팔에 자신의 가슴을 갖다 대기 까지 한다. 형은 훌륭한 카우보이다. 능숙하게 암소를 다루고 있다. 형의 허리춤엔 총까지 달려 있다. 이거 위험하군.', '', '형을 불러보지만 비명 같은 음악소리 때문에 내 목소리가 닿지 않는다. 이곳의 음악은 모든 소통을 단절시키고 하나의 목적만을 향해간다.",
          "emotion": 0
        },
        {
          "text": " 다량의 젖을 향해 말이다.암소들을 뚫고 형을 만났다. 음악 소리 때문에 인사를 나눌 수조차 없다. 그저 입을 뻥긋 거릴 뿐이다. 형 역시 그렇다.', '', '난 수업중인 고등학교의 교실안 처럼 소리 내지 않고 입을 벌린다.', '\"형, 재밌어?\"', 'Wilbur 형 역시 내 뜻을 잘 알고 있다. 형도 소리 내지 않고 얘기한다.', '\"어, 재밌어\"', '역시나.",
          "emotion": 0
        },
        {
          "text": " 하지만 난 여기에 온 목적대로 얘기를 꺼내본다.', '\"Wilbur 형, 여기서 뭐하는거야.집으로 돌아가서 다시 한 번 날으는걸 시도해 보자\"', '절대로 형은 내말을 알아듣지 못했을 것이다. 입만 뻥긋거렸는데 어떻게 이렇게 긴 말을 알아 들을 수 있겠는가.하지만 형은 이미 내가 할 말을 알고 있었다는 듯 내게 얘기 했다.', '', '\"Orville, 난 날고 있어\"', '', .",
          "emotion": 0
        },
        { "text": "", "emotion": 0 }
      ]
    },
    {
      "chapter_num": 3,
      "chapter_name": "편의점에서",
      "chapter_contents": [
        {
          "text": "', '', '추워요. 겨울의 한복판에서 입을 벌린 담뱃갑은 저에게 그렇게 말을 걸어왔습니다. 무언가에 굶주린 목소리로 말이죠. 텅 비어 있었기 때문입니다. 녀석의 입속은.', '염치없게 벌려진 녀석의 입 앞에 침묵하던 저는 서둘러 주머니를 뒤져봅니다. 다행히도 구겨진 지폐 두 장과 차가워진 동전 몇 개가 숨어있네요. 고개를 들어 주위를 둘러봅니다. 네온사인 사이로 노란 불빛이 새어나오는 편의점이 보입니다.",
          "emotion": 0
        },
        {
          "text": " 다행이다, 하는 생각이 담뱃갑의 입을 닫습니다. 서둘러 발걸음을 옮깁니다. 그리고 차가워진 손잡이를 밀어젖힙니다. \"딸랑\"거리는 종소리 너머로 \"어서 오세요\"라는 목소리가 들려옵니다. 마침내, 저는 사랑에 빠집니다.', '', \"당신에게만 하는 이야기지만, 저는 편의점 아가씨들을 좋아합니다. 때로는 사랑에 빠지기도 하죠. 저는 4명의 편의점 아가씨를 사랑했고, 2명의 편의점 아가씨와 연애를 했습니다.",
          "emotion": 0
        },
        {
          "text": " 누구는 대학 등록금을 마련하기 위해, 누구는 다가올 여름에 유럽으로 떠나기 위해, 누구는 예쁜 옷을 사입기 위해, 누구는 그냥 먹고살기 위해 편의점에서 일했지만 그런 건 아무래도 좋았습니다. 제가 그녀들에게 사랑을 느낀 장소는, 그녀들의 사연이 아니라 그녀들이 일하던 편의점이었으니까요. 그녀들이 가진 '시급 3100원의 명랑함'과 '시급 3100원의 태도' 그리고 그녀들이 보낸 '시급 3100원의 시간들'이 저를 설레게 했으니까요.",
          "emotion": 0
        },
        {
          "text": " 그녀들이 가진 단단한 투명함은, 저로 하여금 강화유리를 떠올리게 하기도 했습니다. 하지만, 유리는 유리라서, 깨질듯한 감수성도 가지고 있었죠. 그래서 저는 그녀들에게 늘 조심스러웠습니다. 소녀 같은 숙녀들을, 그래서 저는 늘 사랑했습니다.\", '', '오늘도 저는 편의점에서 사랑에 빠집니다. \\'시급 3100원의 명랑함\\'을 가진 그녀의 \"안녕하세요\" 한 마디 때문에 말이죠.",
          "emotion": 0
        },
        {
          "text": " 저는 눈을 마주치지 못하고, 금세 고개를 떨굽니다. 그리고 물건을 고르는 척하기 시작합니다. 새우깡을 지나, 양파링을 지나, 포카칩을 지나, 오징어땅콩을 지나, 그녀의 눈동자를 지나, 신라면을 지나, 사리곰탕을 지나, 짜파게티를 지나, 너구리를 지나, 그녀의 콧망울을 지나, 면도기를 지나, 칫솔을 지나, 샴푸를 지나, 손톱깎이를 지나, 그녀의 입술을 지나, 코카콜라를 지나, 포카리 스웨트를 지나, 하이트를 지나, 레쓰비를 지나, 어머나를 지나.",
          "emotion": 0
        },
        {
          "text": " 어머나, 눈이 마주쳐 버렸어요.', '저는 황급하게 고개를 다시 떨굽니다. 그리고 손을 뻗어, 마치 원래 꺼내려고 했던 마냥 캔커피 하나를 꺼냅니다. 손의 움직임은 어색하고, 캔커피의 따듯함은 자연스럽습니다. 어찌나 따듯한지, 금세 저의 얼굴까지 따듯하게 데울 지경이었습니다. 얼굴이 빨개지지는 않았나 걱정됩니다. 저는 나이를 이토록 먹고도 이 모양이라지요.",
          "emotion": 0
        },
        {
          "text": " 한심합니다. 저는 서둘러 캔커피 하나를 더 꺼냅니다.', '', '캔커피 두 개를 카운터에 올려놓습니다. 편의점 아가씨를 힐끔 훔쳐봅니다. 아직 소녀의 티를 벗지 못한, 화장기 없는 얼굴이 눈에 들어옵니다. 무슨 말이라도 꺼내고 싶은데, 뜨거워진 입안에서 모든 단어는 눈처럼 녹아버립니다. 서둘러 구겨진 지폐 두 장을 건넵니다. 그러자 \"2000원 받았습니다.",
          "emotion": 0
        },
        {
          "text": "\"하는 예의 \\'시급 3100원의 명랑함\\'이 돌아옵니다. 카운터 한 쪽을 힐끔 훔쳐보자, 알랭 드 보통의 \\'왜 나는 너를 사랑하는가\\'가 보입니다. 편의점 아가씨답지 않은 책이라 생각했지만, 뭐 나름대로 괜찮다고 생각합니다. 서둘러 거스름돈을 돌려받고, 다시 한번 무슨 말인가 해보려 합니다. 하지만, 남태평양 한가운데 섬 같은 입속의 날씨는 여전히 푹푹 찌고 있네요.",
          "emotion": 0
        },
        {
          "text": " 저는 엉거주춤한 뒷모습으로 편의점을 서둘러 빠져나옵니다. 한 손엔 캔커피 하나를 들고서. 편의점엔 캔커피 하나와 \"저기요\"라는 목소리를 남겨두고서 말이죠.', '', '골목 한 귀퉁이를 돌아 몸을 숨깁니다. 그 뒤로, 담배를 사오지 않았다는 생각이 뒤쫓아 옵니다. 하지만, 뭐 그래도 괜찮다고 생각합니다. 담배를 태우고 싶은 생각은 저보다 먼저 도망쳤으니까요.",
          "emotion": 0
        },
        {
          "text": " 그 대신 저는 캔커피를 따기로 합니다. \"딱\"하는 소리가 유쾌하게 밤거리를 울립니다. 커피를 한 모금 넘기자, 남태평양 한가운데 섬 같은 입속의 날씨는 한결 부드러워집니다. 따듯합니다.",
          "emotion": 0
        }
      ]
    }
  ]
}

# db settings
mongo_url_what = os.environ["MONGO_URL_FOR_PYTHON"]

# db start
client = pymongo.MongoClient(mongo_url_what)
db = client["decowrite"]
col = db[COLLECTION]

# find data
result = col.find_one({"_id": ObjectId(QUERY_ID)},{"_id": 1, "title": 1, "status":1, "file":1})
file = result["file"]

# analysis logic - to do
print(file)

# after anlaysis logic, upadate "status", "analysis"
col.update_one({"_id": ObjectId(QUERY_ID)}, {"$set":{"status":"SUCCESS", "analysis":DUMMY}}, upsert=True);

print("hello i'm python code. don't worry")