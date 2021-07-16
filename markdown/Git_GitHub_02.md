# Git과 GitHub_02

###  __GitHub란?__

 GitHub 는 Git을 기반으로 프로젝트를 프로젝트를 진행하고 협업지원 기능을 제공하는 Microsoft의 웹서비스이다. 특히, Local 저장소에 있는 소스코드나 여러 작업물을 원격저장소(remote repository)에 저장하여 공동작업을 원할히 수행할 수 있어 많은 인기를 끌고있는 소프트웨어 개발 플랫폼이라 할 수 있다.

---

### __Rrepository(저장소)__

1. __Local Repository__  : 작업자의 컴퓨터에 저장된 로컬 버전의 프로젝트 저장소

2. __Remote Repositorry__ : Local이 아닌 외부 서버의 프로젝트 저장소

   - 팀단위의 작업을 수행하기 유용
   - 프로젝트 공유하거나 다른 작업자의 코드를 확인할 수 있다.
   - 로컬 버전의 프로젝트와 병합, 변경사항을 적용할 수 있다.

   

---

### Repository 만들기

1. __Local Repository 만들기__

   Git을 이용하여 Local Repository를 만드는 방법에는 2가지가 있다. 

   - _**`git init`**_

   - ***`git clone`***

     ***git init***

      Local  저장소를 시작으로 새로운 프로젝트를 시작하는 경우 사용한다. 작업자가 원하는 폴더에서 Gitbash를 통해 입력하면 해당 폴더에 비어있는 git 저장소가 생성이 된다.

   

   ​				***git clone***

   ​				원격저장소에서 소스코드를 받아와 local에 git 저장소를 만드는 방법이다. 이미 원격저장소에 올라가 있				는 코드를 받아 올때 사용한다. 그러나 원격저장소가 비어있어도 비어있는 저장소를 만들어 준다.

   

   2.__Remote Repository 만들기__

   1. 깃헙 사이트 접속 및 로그인
   2. Respository에서 New 클릭

   ![화면 캡처 2021-07-17 002649](C:\Users\super\OneDrive\바탕 화면\0716 수업 정리.assets\화면 캡처 2021-07-17 002649.png)

   

   

   ​			c. 이후 name을 입력하고 설정마친 뒤 create repository 클릭

   ​			d.  원격저장소 주소를 local에 저장 

   ​			 		` $ git remote add origin 저장소 URL`을 하여 원격저장소 주소 추가

   ​					` $ git remote -v`통해  원격 저장소 목록을 확인

   ​			d. 생성된 repositoty의 default branch를 변경(Settings -> repositories)

   ​		

