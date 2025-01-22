1. 구상한 서비스(응용)의 목적과 배경

외출할 때, 옷을 선택하는 것은 매우 중요합니다. 날씨를 체크하지 않아서 기온에 맞지 않는 옷을 입고 외출을 하면 불편함을 느낄 수 있습니다. 또한, 대기 상황에 맞지 않은 마스크를 착용하면 하루종일 불편함을 느낄 수 있죠, 그래서 제가 만든 프로그램은 이런 상황을 방지하기 위해 바깥의 기온과 미세먼지를 체크하고, 이에 맞는 옷과 마스크 등급을 추천합니다.

2. 활용한 (공공) 데이터는 무엇인가?

한국환경공단_에어코리아_대기오염정보 | 공공데이터포털 (data.go.kr)
기상청_단기예보 ((구)_동네예보) 조회서비스 | 공공데이터포털 (data.go.kr)

3. 제공되는 주요 기능과 동작 시나리오

대기오염정보에서 미세먼지 농도를 제공받고, 기상청 단기예보에서는 기온을 받습니다. 두 api가 제공하는 관측소 정보가 다릅니다.(대기오염정보 : 관측초가 각 동마다 있지 않음, 기상청 단기예보 : 동별로 기온 제공) 그래서 각 동에 맞는 미세먼지 관측소를 매칭하기 위해서 sql을 활용한 데이터 베이스를 활용합니다. 동작 시나리오는 다음과 같습니다

동 입력 -> map.db에 접근하여 동에 맞는 X,Y 좌표, 관측소 정보 추출 -> X,Y 좌표를 단기예보에 입력하여 동의 기온 추출, 기온에 맞는 복장 추출 -> 동에 맞는 관측소 정보를 대기오염정보에 입력 및 미세먼지 농도 추출 -> 미세먼지 농도에 맞는 마스크 정보 출력 

4. 기획한 서비스는 어떤 효과가 있나? 공익적인 효과? 또는 사업적인 효과? 기대되는 편리성 등등.

날씨에 맞는 복장과 마스크를 편리하게 추천받고 싶은 사람들에게 편리성을 줄 수 있다고 생각합니다. 구현하지는 못했지만 구글 애드센스 등을 활용하면 광고비를 통해 사업적인 효과도 누릴 수 있다고 생각합니다,
