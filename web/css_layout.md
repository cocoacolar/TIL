# 1. CSS Layout

### 레이아웃정렬방법

1. Display
2. Position
3. Float
4. Flexbox
5. Grid system

아래로 내려 올수록 최신 기술이다. 그렇다고하여 최신기술만 익히면 안된다. 다양한 방법이 복합적으로 사용되기도 하고 또한 인터넷익스플로러와 같이 많은 기술을 지원하지 않는 브라우저가 존재하기 때문이다. 

# 2.Float

Float 기술이 도입된 배경은 이미지의 좌우 주변으로 텍스가 둘러싸도록 하는 레이아웃을 위해서이다. 쉽게 생각하면 한글의 글자처럼 취급을 생각하면된다. float를 적용한 박스들이 위로 붕 뜬것을 볼 수 있다. 

![Tag: Float - HYUNGI'S TECH BLOG](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHVsDqVfC7yW4AaVVQIEukmgpkrCk4wub8Wg&usqp=CAU)

### a. Float 속성

- none:  기본값
- left: 요소를 왼쪽으로 띄움
- right: 요소를 오른쪽으로 띄움

```css
.클래스명 {
	float: left;
}
```

- float를 사용하면 아래에있던 요소가 올라오게 되는데 이를 막기위해 사용되는 기법이 ___Float clear___이다.

  ```css
  .clearfix::after {
      content: "";
      display: block;
      clear: both;
  }
  ```

- 요소의 마지막 자식으로 가상의 요소를 생성하여 올라오지 못하도록 막는다. 얇은 막을 형성한다 생각하면 쉽다.  content 속성과 함께 사용되며 기본값은 inline 이다.

# 3. Flexbox

### 1. Flexible Box Layout

- 요소 :  Flex Container(부모요소), Flex Item(자식요소)
- 축 : main axis(메인축), cross axis(교차축)

위의 해당 내용을 반드시 잘 숙지하고있어야한다. 특히, 메인축이 x축이라는 생각을 하지 않아야한다. 메인축은 좌우 , 상하 모두 가능하며 교차축은 메인축과 수직으로 만나기 때문에 인지만 하고 있으면 된다.

```css
.flex-container {
	display: flex
    
    flex-wrap: wrap;
    flex-direction: row;
    flex-flow: comlumn wrap;
    justify-content: center;
    align-items: center;
}

```

displayL flex 정렬하려는 부모 요소에 작성

flex- direction : row, row-reverse, column, column-reverse

flex-wrap : nowrap, wrap, wrap-reverse;

flex-flow:  row no wrap(direction 과 wrap의 shorthand)



jutify-content : main축 정렬

flex-start, flex-end, center, space-between, space-around,space-evenly

align -items :cross 축 정렬

stretch 기본, flex-start flex-end, center, baseline 내부의 text 기준선

align -self



# 3. Bootstrap

1. CDN:콘텐츠를 효율적으로 전달하기 위해 여러노드에 가진 네트워크에 데이터를 제공하는 시스템.
2.  bootstrap을 통해 훨씬 간편하게 layout을 해결할 수 있다. 
3. 사용방법은 공식 홈페이지에 있는 내용을 바탕으로 이해할 수 있다. 
4. 모든 사용은 클래스를 사용하여 이루어진다. 

# 4.Grid system

- bootcamp의 그리드 시스템은 flexbox로 제작된다. 
- container, rows, column으로 컨텐츠를 배치하고 정렬(앞선 flex와 사용방법이 조금 다르다)
- 12개의 column
- 6개의 grid breakpoints 를 이용하여 반응형 웹을 만들 수 있다.

- 그리드를 잘이용하기 위해서는 더 많은 경험이 필요할 것같다...