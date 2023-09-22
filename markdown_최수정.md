# 마크다운
일반 텍승트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하여 빠르게 문서를 정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.

## 1. 문법
### 1.1 Header
해더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아닌 의미론적인 중요도를 나타냅니다.
- ```<h1>```부터 ```<h6>```까지 표현 가능합니다.
- ```#```의 개수로 표현하거나 ```<h1></h1>```의 형태로 표현 가능합니다.
  
  # h1 태그입니다.
  ## h2 태그입니다.
  ### h3 태그입니다.
  #### h4 태그입니다.
  ##### h5 태그입니다.
  ###### h6 태그입니다.

  ### 1.2 List
  목록을 나열할 때 사용합니다. 수서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래 순서가 없는 항목을 지정할 수 있으며 그 반대도 가능합니다.
 - 순서가 없는 목록
    - ```1.```을 누르고 스페이스바를 누르면 생성
    - ```tab```키를 눌러서 하위항목을 생성할 수 있고, ```shift + tab```키를 눌러서 상위항목으로 이동할 수 있습니다.
 
 - 순서가 있는  목록
     - ```-```을 쓰고 스페이스바를 누르면 생성할수 있습니다.
     - ```tab```키를 눌러서 하위 항목을 생성할 수 있고   ```shift + tab```키를 눌러서 상위 항목으로 이동할 수 있습니다.

1. 순서가 있는 항목
2. 순서가 있는 항목
   1. 순서가 있는 항목
   2. 순서가 있는 항목

- 순서가 없는 항목
- 순서가 없는 항목
  - 순서가 없는 항목
  - 순서가 없는 항목

### 1.3 Code Block
코드블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다. 인라인과 브럭단위로 구분할수 있습니다.
- Inline
  - 인라인블럭으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다.
- Block 
  - `(백틱)을 3번 입력하고 `enter`를 눌러 생성합니다.

<br>```add```한 요소를 remote저장소에 올리려면 ```$ git push origin master``` 를 터미널에 입력합니다.
<br>
```
$ git add .
$ commit -m "first commit"
$ git push orgin master
```

### 1.4 Image
로컬에 있는 이미지를 삽입하거나 이미지를 링크를 황용하여 이미지를 나타낼 때 사용합니다.
- ```![]()```를 작성하고 ```()```안에 이미지 주소를 입력합니다. []안에는 이미짛파일의 이미지이름을 작성합니다.
- 로컬에 이미파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장합니다.
  ![git](data:image/png;base64,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)

  ### 1.5 Link
  특정 주소로 링크를 갈 때 사용합니다.
  - ```[]()```을 작성하고 ```()```안에 링크 주소를 작성하고 ```[]```안에 어떤 링크 주소인지 작성합니다.
  
[git 공식문서](https://git-scm.com/book/ko/v2) <br>
[github 공식문서](https://docs.github.com/ko)
### 1.6 Table
표를 작성하여 요소를 구분 할 수 있습니다.
 - ```|``` (파이브)사이에 컬럼을 작성하고 ```enter```를 입력합니다.
 - 마지막 컬럼을 작성하고 뒤에 ```|```를 붙여줍니다.

|working directory

| **statging area** | **remoe repo** | **working tree** |
| --- | --- | --- |
| working tree | index | history |
|working copy| cache|tree|

### 1.7 기타
**인용문0**
- ```>```을 입력하고 ```enter``` 키를 누릅니다.
       
    >  git은 컴퓨터파일의 변경사항을 추적하고 여러 명의사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.
 
 - 인용문 안에 인용문을 작성하면 중첩해서 사용할 수 있습니다.
     
     > $git add.
    >> $gitcommit -m
    >>>git push origin master

 **수평선**
 - ```---```, ```***```, ```___```을 입력하여 작성합니다.

  working Directory
  ---
  Staging Area
  ---
  Remote Repository
  ---

  **강조**
  - 이탤리체는 해당 부분을 * 혹은 _(언더바)로 감싸줍니다.
  - 취소선은 ~~표시를 사용합니다.
이것은 _이태릭체_ 입니다.<br>
이것은 **보드체** 입니다.<br>
이것은 ~~취소선~~ 입니다.


  


