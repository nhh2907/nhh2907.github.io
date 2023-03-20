---
layout: post
title: "[기초통계] 2-1 상관관계, 상관계수"
date: 2023-03-12 19:29:00 +0900
author: nhh2907
categories: [Math, Statistics]
tag: [Statistics, Sapientia a Dei]
math: true
---


# 상관관계(Correlation)

### 정의

한 변수가 다른 변수와 <span style="color:coral">공변</span>하는 관계

- <span style="color:coral">상관관계는 인과관계가 아니다</span>
    
    상관관계는 두 변수가 서로 관계가 있는지 없는지에 대한 것, not 원인과 결과의 인과관계
    
- <span style="color:coral">선형(직선)관계만을 측정</span>할 수 있음, not 비선형

### 종류

1. 양의 상관관계 : 두 변수가 같은 방향으로 변화
    - X가 증가할 때, Y가 증가
    - X가 감소할 때, Y가 감소
2. 음의 상관관계 : 두 변수가 다른 방향으로 변화
    - X가 증가할 때, Y가 감소
    - X가 감소할 때, Y가 증가

# 상관계수

상관관계를 나타내는 계수

### 두 가지 의미 지님

1. <span style='color:coral'>방향</span>: 우상향(+) or 우하향(-)
2. <span style='color:coral'>힘</span>: 절대값 크기
    - 상관계수가 절대값 1에 가까울 수록 힘이 세다
    - 힘이 세다라는 것은 데에터가 가깝게 모여있음을 의미
    - 따라서, 데이터가 퍼져있으면 상관계수가 0에 가까워짐을 의미

### 범위: [-1, 1]

- 상관계수가 -1일때 완벽한 음의 상관관계
- 상관게수가 +1일때 완벽한 양의 상관관계
- 상관계수가 0일때 아무런 관계 없음

### **Pearson Correlation Coefficient**

$$
\rho_{X,Y}= \frac{Cov(X, Y)}{\sigma_X\sigma_Y}
$$

Where

- Cov is the [covariance](https://en.wikipedia.org/wiki/Covariance)
- $\sigma_X$ is the standard deviation of $X$
- $\sigma_Y$ is the standard deviation of $Y$

The formula for $\rho$ can be expressed in terms of mean and expectation. Since 

$$
Cov(X, Y) = E[(X-\mu_X)(Y-\mu_Y)]
$$

the formula for $\rho$ can be also be written as 

$$
\rho_{X,Y}= \frac{E[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X\sigma_Y}
$$

- $\mu_X$ is the mean  of $X$
- $\mu_Y$ is the mean  of $Y$
- $E$ is the expectation

The formula for $\rho$ can be expressed in terms of uncentered moments. Since

- $\mu_X = E[X]$
- $\mu_Y = E[Y]$

<span style='color:plum'>위키백과에서 이 부분부터는 이해가 잘안되네… 좀 더 공부하고 작성해야함 — 현재 머리가 안돌아감</span>
# 주의

![correlation coefficiency](/assets/img/etc/math/2023-03-12_correlation_coefficiency/correlation_coefficiency.png)

- <span style="color:coral">기울기와 상관관계 크기는 관계없다</span>. 기울기가 크다고 해서 상관관계가 큰것이 아니다. 단순히 기울기는 양의 관계인지 음의 관계인지만 나타냄. 따라서 데이터가 직선에 모여있는데 기울기만 양으로 같다면 모두 같은 상관계수를 같는다. 다시 말하면, 기울기가 높다고 해서 상관계수가 크다는 것이 아님
- 단 기울기가 0이면 상관계수는 0이다. 왜냐하면, X가 증가할 때 Y는 아무런 변화가 없기 때문이다

# Reference

- [Sapientia a Dei](https://youtu.be/Se7mWTBRfCc)
- [Pearson correlation coefficient - Wikipedia](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)