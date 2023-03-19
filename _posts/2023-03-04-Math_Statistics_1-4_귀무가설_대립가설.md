---
layout: post
title: "[기초통계] 1-4 귀무가설, 대립가설"
date: 2023-03-04 15:20:00 +0900
author: nhh2907
categories: [Math, Statistics]
tag: [Statistics, Sapientia a Dei]
math: true
---

> 문제 정의 → 가설 수립→ 가설 검정(Hypothesis Test)

- 통계학자들은 가설을 먼저 정해놓고 두 개의 가설 중 무엇이 맞을지 검정하는 작업을 하도록 일련의 과정을 설계하였음

# 귀무가설 - Null Hypothesis

<aside>
💡 Null : '비어 있다' 또는 '아무 것도 없다'

</aside>

### 정의

- <span style="color:coral">어떤 사건이 우연히 일어났을 가능성</span>에 대한 가설
- **아무 영향도 없음** 그리고 **아무 일도 없다** 라는 것을 가정하는 가설
    - The Null hypothesis represents **no change** or **no difference** from the past - 통계 원서책
- 통계학에서 처음부터 버릴 것을 예상하는 가설 - [위키백](https://ko.wikipedia.org/wiki/%EA%B7%80%EB%AC%B4_%EA%B0%80%EC%84%A4)과
- <span style="color:coral">사건(귀무가설)</span>이 우연히 일어날 확률이 높으면 기각이 안되고 우연히 일어날 확률이 낮으면 기각됨
    - 예시:
        - 귀무가설 : 호랑이와 토끼가 (우연히)같은 종이다
        - 호랑이와 토끼가 우연히 같은 종일 확률이 95%이면 우연히도 두 동물의 종은 같다. 그러나 호랑이와 토끼가 우연히 같은 종일 확률이 5%라면 우연 확률이 너무나도 낮으니 이건 뭔가 유의(의미, 인과관계)가 있다고 추론할 수 있음
    

### 오류

- 1종 오류 : 귀무가설이 참이어도 기각하는 경우(귀무가설을 기각하는 경우) - [위키백과](https://ko.wikipedia.org/wiki/%EA%B7%80%EB%AC%B4_%EA%B0%80%EC%84%A4)
    - $H_0 \text{ is rejected when} \ H_0 \  \text{is true}$  -  통계 원서책
- 2종 오류 : 귀무가설이 거짓이어도 기각하지 않는 경우(귀무가설을 기각하지 않는 경우) - [위키백과](https://ko.wikipedia.org/wiki/%EA%B7%80%EB%AC%B4_%EA%B0%80%EC%84%A4)
    - $H_0 \text{ is accepted when} \ H_1 \  \text{is true}$  -  통계 원서책

# 대립가설 - Alternative Hypothesis

<aside>
💡 무엇에 대한 **대립**인가? 귀무가설

</aside>

- <span style="color:coral">어떤 사건이 우연히 일어난 것이 아니라 어떤 이유(의미, 인과관계)가 있을 가능성</span>에 대한 가설
- The alternative hypothesis represents **change** or **difference** - 통계 원서책
- The alternative is often referred to as **the research worker’s hypothesis** - 통계 원서책
    - 대립가설은 연구자가 연구를 통해 입증되기를 기대하는 예상이나 주장하는 내용 - [위키백과](https://ko.wikipedia.org/wiki/%EA%B7%80%EB%AC%B4_%EA%B0%80%EC%84%A4)

# P-Value와 가설

<aside>
💡 P-Value : “어떤 사건이 **우연히** 일어날 확률”

</aside>

- <span style="color:coral">사건이 우연히 일어났다</span>라고 가정하는 것이 **귀무가설**이고, 그 <span style="color:coral">사건이 우연히 일어난 것이 아니고 뭔가 이유(인과관계)가 있다</span>라고 가정하는 것이 **대립가설**
    - 즉, 귀무가설이 맞다면 그 사건은 우연히 일어난 것으로 추정하고, 대립가설이 맞다면 우연히 일어난 것이 아닌 뭔가 이유(인과관계)가 있다고 추정하는 것이다
- **P-value < 0.05**이면 귀무가설 선택, **P-value > 0.05**이면 대립가설 선택
    
    예시: 금년도 12월 매출이 우연히 1000만원 더 나올 확률이 5%보다 작으면, 이는 우연이 아니고 안주임의 신규 판매전략이 효과가 있다는 추정할 수 있다. 그러나 만약 5%보다 크다면, 이는 우연히 1000만원의 매출이 증가한 것이다
    
- 엄밀히 말하자면 P-Value의 확률값은 <span style="color:coral">1종 오류의 수준을 5%로 제약</span>한다는 의미. 다르게 말하자면 실제는 (귀무가설) 어떤 사건이 우연히 발생했음에도 우연히 발생하지 않았다고 결론 내릴 오류를 5% 이내로 하겠다는 것

하지만, 통계에 처음 접근할 때에는 그냥 어떤 사건이 우연히 발생할 확률의 의미로 p-value을 접근해도 무방함. 아니면 이후에 통계를 이해하는데 어렵기 때문

|  |  | 진실 | 진실 |
| --- | --- | --- | --- |
|  |  | $H_0$이 참 | $H_0$이 거짓 |
| 연구 결과 | $H_0$이 참 | 문제 없음 | 2종 오류 |
| 연구 결과 | $H_0$이 거짓 | 1종 오류 | 문제 없음 |

# Reference

- [위키백과](https://ko.wikipedia.org/wiki/%EA%B7%80%EB%AC%B4_%EA%B0%80%EC%84%A4)
- [Introduction to Mathematical Statistics 원서](https://www.amazon.com/Introduction-Mathematical-Statistics-Robert-Hogg/dp/0321795431/ref=sr_1_2?crid=1X5NXCV5TCJGC&keywords=Introduction+to+Mathematical+Statistics&qid=1679145931&s=books&sprefix=introduction+to+mathematical+statistics%2Cstripbooks-intl-ship%2C261&sr=1-2)
- [Sapientia a Dei](https://www.youtube.com/watch?v=NG1ZNH1kOl0)