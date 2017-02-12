# BurpHelper

##1. Intro
![Alt text](http://cfile10.uf.tistory.com/image/2170343D58A013DE090029)

- Jython을 기반으로 한 Burp Suite 플러그인입니다. 
- 윈도우 환경에서 사용 가능합니다.
- Window 10에서 Cooxie 대용으로 사용이 가능합니다.

##2. Patch Note

### ver 1.2
* Check Current IP
- 현재 진단하고 있는 PC의 공인/사설 IP 확인 기능 추가

### ver 1.1
* Target Site List
- 진단 대상 사이트의 주소, ID, 패스워드를 등록 및 클립보드 복사 기능 추가
- [주의] 등록한 정보(사이트, ID, PW)를 C:\burphelper\sitelist 경로에 저장합니다. 
  (종료 후 시작에도 설정값 불러오기 위함)

### ver 1.0
* Windows Internet Explorer 프록시 설정 기능 제공
- BurpHelper 플러그인의 IEProxy Settings를 통해 프록시로 사용할 아이피를 등록/변경/삭제가 가능합니다.
- 체크박스 on/off를 통해 쉽게 프록시 설정이 가능합니다.
- 프록시 설정을 저장하기 위해 C:\burphelper\proxylist 경로에 저장합니다.
  (종료 후 시작에도 설정값 불러오기 위함)

##3. Installation
3. Burp Extention Installation
-------------

1) jython Standalone 
http://www.jython.org/archive/22/installation.html
2) Burp 실행 → 상단 메뉴 [Extender] → [Options]를 누릅니다.

3) [Python Environment]에서 앞에서 다운받은 jython standalone jar 파일을 찾아서 등록합니다.
(jython 기반이라 한글 경로 인식시 에러가 납니다. 꼭 영문만 포함된 경로에 jar 파일을 저장후 불러와주세요.)

4) Burp의 [Extender]-[Extensions]-[Burp Extensions]에서 Add 버튼을 누릅니다.

5) [Extensions type] > Python 선택, [Extension file(.py)] > BurpHelper_v버전.py 파일을 추가시켜 준 후 Next를 클릭

6) 정상적으로 플러그인이 로딩되는 경우 아래 그림과 같은 Output 탭에 메시지를 확인할 수 있습니다. 로드상 오류가 있으면 Errors 탭에 에러가 표기됩니다

7) 정상적으로 등록이 완료가 되면 상단 메뉴에 BurpHelper 플러그인 메뉴가 등록됩니다.

8) BurpHelper 플러그인을 선택해서 Add/Edit/Remove 버튼을 통해 사용할 프록시 서버 IP 등록/편집/삭제 가능합니다.
(등록한 설정은 파일로 저장되며 종료후 재시작시에도 설정을 불러옵니다.)

9) IP등록 후에는 프록시 설정 사용시→ Enabled 체크박스 클릭 , 프록시 설정 해지시 → Enabled 체크박스 체크해제 
(Burp Suite에서 플러그인 로딩시 프록시 설정은 자동해제됩니다)



