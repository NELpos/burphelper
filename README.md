# BurpHelper 1.22

##1. Intro
- Jython을 기반으로 한 Burp Suite 플러그인입니다. 
- Windows 환경에서 사용 가능합니다.
- Window 10에서 Cooxie 대용으로 사용이 가능합니다.
<img src = http://cfile10.uf.tistory.com/image/2170343D58A013DE090029 width=100%></img>

##2. Patch Note

### ver 1.22
* 일부 버그 수정

### ver 1.2
* Check Current IP 기능 추가
 * 현재 진단하고 있는 PC의 공인/사설 IP 확인 기능 추가

### ver 1.1
* Target Site List 기능 추가
 * 진단 대상 사이트의 주소, ID, 패스워드를 등록 및 클립보드 복사 기능 추가
 * [주의] 등록한 정보(사이트, ID, PW)를 C:\burphelper\sitelist 경로에 저장합니다. 
   (종료 후 시작에도 설정값 불러오기 위함)

### ver 1.0
* Windows Internet Explorer 프록시 On/Off 기능
 * BurpHelper 플러그인의 IEProxy Settings를 통해 프록시로 사용할 아이피를 등록/변경/삭제가 가능합니다.
 * 체크박스 on/off를 통해 쉽게 프록시 설정이 가능합니다.
 * 프록시 설정을 저장하기 위해 C:\burphelper\proxylist 경로에 저장합니다.
   (종료 후 시작에도 설정값 불러오기 위함)

##3. Installation
####Step 1. Git에서 파일 다운로드
1. https://github.com/NELpos/burphelper에 접속<br>
2. jython-standalone-2.7.0.jar 파일과 BurpHelper.py 파일을 다운받습니다
<img src = http://cfile30.uf.tistory.com/image/221AFC3758A01AC80D78EA width=100%></img>

####Step 2. Burp Extender Jython 환경 설정
1. Burp Menu → 'Extender' 클릭
2. 'Options' 클릭
3.  'Python Environment'에서 Jar File에 jython-standalone-2.7.0.jar 파일 등록
<br>    (jython 기반이라 한글 경로 인식시 에러가 납니다. 꼭 영문만 포함된 경로에 jar 파일을 저장후 불러와주세요.)
<img src = http://cfile22.uf.tistory.com/image/2710354F58A02B650387F4 width=100%></img>

####Step 3. BurpHelper 플러그인 추가
1. Burp Menu → 'Extender' → 'Extentions' 클릭
2. Burp Extentions에서 'Add' 추가
3. Extentions Details에서 type을 파이썬을 선택하고 다운받은 BurpHelper.py 파일 추가
<br>   (jython 기반이라 한글 경로 인식시 에러가 납니다. 꼭 영문만 포함된 경로에 jar 파일을 저장후 불러와주세요.)
<img src = http://cfile4.uf.tistory.com/image/26750A4C58A02D0D09DD6F width=100%></img>
4. 정상적으로 플러그인이 로딩되는 경우 아래 그림과 같은 Output 탭에 메시지를 확인할 수 있습니다. 로드상 오류가 있으면 Errors 탭에 에러가 표기됩니다
<img src = http://cfile29.uf.tistory.com/image/260AB73758A017EE356C33 width=100%></img>
5. 정상적으로 등록이 완료가 되면 상단 메뉴에 BurpHelper 플러그인 메뉴가 등록됩니다.
<img src = http://cfile4.uf.tistory.com/image/2540EE4758A02E58271D84 width=100%></img>

##4. Usage
####1) Windows Internet Explorer 프록시 On/Off 기능
#####설명
<p>
* Proxy Server Setting에서 Add/Edit/Remove 버튼으로 프록시 서버 IP 등록/편집/삭제가 가능합니다.
  등록한 설정은 파일로 저장되며 종료후 재시작시에도 설정을 불러옵니다.)<br>
</p>
#####사용법
1. Proxy Sever Setting 메뉴에서 Add 버튼을 누릅니다.
2. 프록시 서버 정보를 입력 후 ADD 버튼을 누릅니다. (이때 NAME은 반드시 영어로 입력해야 합니다.)
<img src = http://cfile30.uf.tistory.com/image/273FFE4A58A02FBB046188 width=100%></img>
3. 추가가 완료되면 Enabled 체크박스를 클릭하세요.
4. 'Proxy is enabled' 알림창이 뜨면 Proxy 설정이 활성화 되었습니다. 체크 박스를 해제하면 Proxy 설정이 비활성화 됩니다.
<img src = http://cfile26.uf.tistory.com/image/2728084B58A030F10AF5AE width=100%></img>

####2) Check Current IP 기능
#####설명

* Target Site List에서 Add/Edit/Remove 버튼으로 진단 대상 사이트 URL/ID/PW 정보를 입력할 수 있습니다.
* 진단 대상 사이트 및 계정이 여러개일때 ID/PW를 저장해서 손쉽게 사이트를 불러오고 저장/복사를 위한 기능입니다.
  (등록한 설정은 파일로 저장되며 종료후 재시작시에도 설정을 불러옵니다.)

#####사용법
1. Target Site List 메뉴에서 Add 버튼을 누릅니다.
2. 사이트 URL/권한 유형/ID/PW/Comment를 입력 후 ADD로 추가합니다. (Comment는 반드시 영어로 입력해야 합니다.)
<img src = http://cfile28.uf.tistory.com/image/2470724A58A032CF04A0FF width=100%></img>
3. 등록 후에 Open URL 버튼을 클릭하면 사이트를 열 수 있습니다.
<img src = http://cfile9.uf.tistory.com/image/265DA74E58A033F81D2566 width=100%></img>
4. ID Copy/PW Copy 버튼을 클릭후 로그인 폼에 붙여넣기 하면 손쉽게 클릭만으로 붙여넣기가 가능합니다.
<img src = http://cfile2.uf.tistory.com/image/274F364B58A034B82591BE width=100%></img>

####3) Target Site List 기능 추가
#####설명
* 현재 진단하는 PC의 공인 IP/사설 IP를 확인해줍니다.
#####사용법
1. Check Current IP 메뉴에서 'Check IP' 버튼을 누릅니다.
<img src = http://cfile4.uf.tistory.com/image/2601614958A0352A331BE1 width=100%></img>
2. 공인 IP / 사설 IP 확인이 가능합니다.
<img src = http://cfile5.uf.tistory.com/image/2567804E58A03574186CC9 width=100%></img>

##5. TroubleShooting
1. Jython PY-String Non-Byte Error
  원인 :  윈도우 사용자 이름이 한글인 경우 경우에 발생<br>
  (ex. c:\users\홍길동\Desktop\jython-standalone.jar)
  해결 : jython-standalone 파일을 영문 경로에 저장후 등록

2. 아이템 추가시 Name을 한글로 적는 경우 Unicode Error 발생
   원인 > Name을 한글로 입력하는 경우 설정파일 저장 및 불러오기 불가
   해결 > Name을 영어로 입력

##6. Special Thanks
thanks to darkhi
