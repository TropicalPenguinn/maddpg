# Instroduction
Assembly어에 대해서 배울 것이고 더 나아가 이것을 Binary Code로 바꾸는 과정을 학습할 것이다.

* **Insturction**이라는 **word(command)**로 컴퓨터에게 명령을 내린다. Instruction set을 vocabulary of words라고 부른다.
* **MIPS(단어장) Instruction(단어)**
* Compiler는 High-Language를 MIPS Assembly로 바꾸는 역할을 한다.

# Arithmetic Operations
MIPS Assembly Instruction의 기본 형태를 살펴보자. (단어가 어떻게 생겨먹었는지 알아봅시다.)

![](https://velog.velcdn.com/images/everyman123/post/7e7046c3-ae07-4561-8925-a5643f94172f/image.png)
* **한 줄에 하나**의 Instruction만 온다. 
* 하나의 Destination과 2개의 sources로 구성되어 있다. **(Three Operands)**
*  간단해지기 위해서 같은 형태를 사용하는 것이 좋다는 설계 철학 (Simplicity favors regularity)

# Operands of the Computer Hardware
MIPS Assembly를 다루려면 Register에 대한 이해가 필요하다. 여기서 Arithmetic 연산을 MIPS Assembly로 바꾸는 연습을 해보자.

* Register: CPU와 직접적으로 연결되어있는 locations이다. (연산에 사용될 데이터가 바로 보관됨)
* MIPS는 32개의 Registers를 가지는데 각 Register의 크기는 32 bits이다 그러므로 MIPS 는 32 X 32-bit registers를 가진다.
* CPU 와 직접적으로 연결된 Register의 사이즈가 MIPS에서는 32bits이기 때문에 Word는 컴퓨터에게 접근하는 기본 단위이다.
* **3개의 Operands는 반드시 32개의 registers 안에서 선택 되어야 하며** Register는 Dollar Sign으로 표시한다.
![](https://velog.velcdn.com/images/everyman123/post/fad54df7-0c84-4fcb-8053-36ae9a827ab6/image.png)
![](https://velog.velcdn.com/images/everyman123/post/8b648d78-b0e9-4899-b535-99ce115a4137/image.png)

# Memory Operands
연산을 하려면 기본적으로 Register 안에 Data를 넣어야 한다. 그러기 위해서는 Main memory에 접근해야 하는데 Memory Operands를 통해 그것을 배워보자. **(주의: Memory Operands에서는 word가 4bytes이며 memory 접근은 byte 단위로 이루어진다는 사실을 인지하자)**
* **Alignment Restriction** : 4씩 곱해라
* 종류: lw(load word),sw(save word),lh(load halfword),lhu(load halfword unsigned),sh(store half)
* 형식 ![](https://velog.velcdn.com/images/everyman123/post/9d5d19e6-e14e-4d48-a500-e63b5975efa1/image.png)
* 원리: 데이터 접근은 base address + offset으로 주솟값을 찾는다
![](https://velog.velcdn.com/images/everyman123/post/2734f28e-ecca-49fc-9091-64e54befeb45/image.png)
* 문제 해설
> * 더하기를 하려고 보니 A[8]이 있네? 저 데이터는 register에는 없으니 lw로 가져오자
> * 가져왔으면 더하자
> * 그런데 보니 다시 그 값을 저장해야하니 sw를 사용하자.



# Constant or Immediate Operands

 **make the common case fast** 은 설계에 있어서 성능을 높이기 위해 중요한 철학이다. 연산에서 common case는 어떤 것이 있을까? **상수 연산**,**zero**,**어떤 변수의 값을 다른 변수로 옮기기**  이 세 가지가 연산에서 common case라고 할 수 있다. MIPS는 이 3가지 경우를 **immediate operands,$zero register, move pseudoinstruction**로 해결하였다. 
 

* ![](https://velog.velcdn.com/images/everyman123/post/e20633bf-28f4-43f9-a5a8-b12e7bdb6d32/image.png)

* 단 더하기만 있고 빼기 subi같은 건 없다.
![](https://velog.velcdn.com/images/everyman123/post/aa39f05d-ae2b-4fce-a633-85576cf25ef4/image.png)

* **make the common case fast** 에 대해서 더 살펴보면 사실 0을 쓰는 경우가 굉장히 많으니 0의 경우는 아예 register로 wired되어 있다. **$zero** 

* 어떤 register의 값을 다른 register로 옮기는 방식은 
add $s1, $s0, $zero 로 하면 된다. 하지만 값을 이동하는 것은 **make the common case fast** 이기 때문에 move연산을 따로 만든다.

move $s1, $s0 (operands가 2개이기 때문에 이런 연산은 **pseudoinstruction**이라고 부른다.)

# Signed and Unsigned Numbers
![](https://velog.velcdn.com/images/everyman123/post/f29f3b51-b8dc-4311-8b34-75979b18b8bb/image.png)
* 반대 부호 만들기: 다 바꾸고 1 더하기

# Representing Insturctions 

MIPS의 register의 크기는 32bit이다. 또한 모든 Instruction word는 32bit이다. 하지만 같은 32bit라고 하더라도 목적에 따라 format이 다른데 3가지 format 이 있다.

또한 위는 MIPS Instructio이 32bit Binary 코드로 어떻게 변하는지 구할 수 있다.

* **R-format** : Arithmetic 연산 (6 fields) (6(op),5(rs),5(rt),5(rd),5(shamt),6(funct))
* **I-format** : data transter 연산(4 fields) 
* **J-format** : Jump 연산(2 fields) 
![](https://velog.velcdn.com/images/everyman123/post/c58c9385-9b18-402f-95f9-98cc924a42e6/image.png)

# R format (for register, Arithmetic operations)
![](https://velog.velcdn.com/images/everyman123/post/113e74c0-b563-4827-b3de-ddf77a52345f/image.png)
* $s0 ~$s7 16~23
* $t0 ~ $t7 8~15, $t8~ $t9 24~25 (대체로 t는 7개안에 다 처리되기 때문이다.)
* t0~t7,s0~s7,t8~t9 (8~25)
![](https://velog.velcdn.com/images/everyman123/post/2c525d5c-961c-4aa9-b5de-fbfc44f9c695/image.png)

0 | 17 | 18 | 8 | 0 | 32

000000 | 10001 | 10010 | 01000 | 00000 | 100000

=0000 0010 0011 0010 0100 0000 0010 0000 (2) =02324020(16)
> 문제해설
* add는 op가 0이고 funct가 32이다.
* s1,s2는 source operand에 위치하기 때문에 rs rt에 s1,s2에 해당하는 17,18을 집어넣는다
* t0은 8

# I format (for Immediate and data transfer inst)
![](https://velog.velcdn.com/images/everyman123/post/ad59da68-6e29-4bf1-999a-c92e282f2148/image.png)

* rs에 base, rt에 destination constant에 offset이 들어간다. (byte)
* 16bit이지만 맨앞 비트는 부호 표시이기 때문에 $-2^{15} \sim 2^{15}$까지 표현 가능하다.
* rd,shampt,funct가 합쳐짐
![](https://velog.velcdn.com/images/everyman123/post/2f9aaa50-2ee9-42c1-9193-23eb8499bf73/image.png)

35 | 19 | 8 | 32
100011 | 10011 | 01000 | 0000000000100000 
![](https://velog.velcdn.com/images/everyman123/post/fc6190e6-6f17-41df-bedf-d33855a0ed7c/image.png)

# Logical Operations (R-format)
* 종류: 네가 아는 논리 연산 + Shift 연산 (무엇을 사용해? R-format)
* sll(왼쪽),srl,and,andi,or,ori,nor

## Shift 연산
* sll (왼쪽으로 shift) : 2배씩 커지는 효과, op가 0 funct가 0
* srl (오른쪽으로 shift) : 2배씩 작아지는 효과, op가 0 funct가 2
![](https://velog.velcdn.com/images/everyman123/post/ee734ae2-068a-489c-9e13-d80f54d82969/image.png)

* 0 | 0 | 16 | 10 | 4 | 0 = 000000 | 00000 | 10000 | 01010 | 00100 | 000000 (2)
> 문제해설
> * sll 연산이니 op,funct 모두 0
> * sll은 rt,rd만 채우면 된다 s0를 rt t2를 rd에 넣고 4는 shift정도니 shamt에 넣는다
> * t2는 10 s0 은 16이다

![](https://velog.velcdn.com/images/everyman123/post/dbcfef64-c827-4c5b-92bb-ec9df40cb089/image.png)

* 0 | 0 | 16 | 10 | 4 | 2 = 000000 | 00000 | 10000 | 01010 | 00100 | 00010 (2)
> 문제 해설
>* srl 연산이니 op는 0 funct는 2
>* 나머지는 동일

## Logical Operation : PPT보고 어차피 예제임
# Instructions for Making Decisions (예제 위주)
* beq register1, register2, L1
* bne register1, register2, L1
* slt(set on less than): 작으면 1
* slti (immediate)
* sltu,sltiu (unsigned): 맨 앞이 1이더라도 음수가 아님
![](https://velog.velcdn.com/images/everyman123/post/08e78882-2ee3-4f8b-9d3c-a270d840bbae/image.png)


![](https://velog.velcdn.com/images/everyman123/post/e3466d99-67d9-4d54-9c94-cef179eb7d72/image.png)
![](https://velog.velcdn.com/images/everyman123/post/a0b940b2-3d00-469c-9826-f00da0af8122/image.png)


# Supporting Procedures in MIPS

함수 호출과 관련된 MIPS Assembly instruction에 대하여 공부한다. **Procedure(function) calling**
![](https://velog.velcdn.com/images/everyman123/post/c9aab00e-8c74-4422-aab2-16edf4de6b3f/image.png)

* **jal(jump and link instruction)** : nested 함수 안에 함수 호출
* **jr (jump register instruction)** : 함수가 끝났을 때

* 그런데 위에 있는 것보다 function을 처리하기 위해 더 많은 register가 필요하면 어떻게 하지? (ex: nested procedure)

**해답: 지금 procedure 관련 register을 stack에 저장하면 된다.**

* **Stack: register를 저장하기 위한 Data structure**
![](https://velog.velcdn.com/images/everyman123/post/23fa7b13-23be-4bf7-9fa1-16a2f06ff8bc/image.png)
* $sp register가 base address를 기억하고 그 아래 방향으로 register 정보를 집어넣으면 더 많은 register를 사용하는 효과를 누릴 수 있다.
![](https://velog.velcdn.com/images/everyman123/post/31ca7ed3-a04b-41b7-b42e-355f4f81e21f/image.png)

