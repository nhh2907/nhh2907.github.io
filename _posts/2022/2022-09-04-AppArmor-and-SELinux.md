---
title: "AppArmor와 SELinux"
date: 2022-09-04 23:10:00 +0900
categories: [os]
tags: [os]
use_math: true
---

# AppArmor 와 SELinux

AppArmor 와 SELinux 는 시스템 관리자가 컴퓨터 보안 모델을 제어할 수 있도록 하는 리눅스 커널 보안 모듈(LSM; Linux Security Modules)이다.

## 정보 보안 모델이란

정보 보안 모델이란 운영체제에서 디렉토리나 파일, 네트워크 소켓 같은 시스템 자원을 적절한 권한을 가진 사용자나 그룹이 접근하고 사용할 수 있게 통제하는 모델이다.

시스템 자원을 객체(Object)라 하고, 자원에 접근하는 사용자나 프로세스를 주체(Subject)라 한다.

예를 들어, `/etc/passwd` 파일은 객체이고, 이 파일에 접근하여 암호를 변경하는 `passwd` 라는 명령어는 주체이다. 

크게 세 가지로 구분된다.

![1](/assets/images/2022-09-04-AppArmor-and-SELinux/1.png)

출처: [[정보보안기사] 10. 접근통제 보안 모델](https://peemangit.tistory.com/191) [티스토리]

### 1. 강제적 접근 통제(MAC; Mandatory Access Control)

주체와 객체의 보안 등급을 비교하여 접근 권한을 부여하는 규칙기반 접근 통제이다. 보안 관리자가 취급 인가를 허용한 객체만 접근할 수 있도록 강제적으로 통제하는 중앙 집중형 보안관리 모델이다.

쉬운 예시로는 네이버 카페에서 등급에 따라 접근 가능한 게시판이 다른 것이 있다. (방화벽)

- 장점
    1. 모든 객체에 대한 관리가 용이하다.
    2. 중앙 집중식 관리이기 때문에 매우 엄격한 보안을 제공한다.
    3. 군대와 같은 환경에서 적합하다.
- 단점
    1. 사용자 기능이 매우 제한적이다.
    2. 많은 관리적 부담이 요구되고, 비용이 많이 든다.
    3. 모든 접근에 대해 확인해야 하므로 성능이 저하된다.
    4. 상업적인 환경에서는 부적합하다.

### 2. 임의적 접근 통제(DAC; Discretionary Access Control)

주체가 속한 그룹의 신원에 근거하여 객체에 대한 접근을 제한하는 신분기반 접근통제이다. 객체의 소유자가 접근 여부를 결정하는 분산형 보안관리 모델이다. 하나의 주체마다 객체에 대한 접근 권한을 부여해야 한다. 리눅스, 윈도우 등의 대부분 운영체제는 DAC 에 기반한다.

- 장점
    1. 객체마다 세분화된 접근 제어가 가능하다.
    2. 특정 주체가 다른 주체에 대해 임의적으로 접근제어가 가능하다.
    3. 매우 유연한 접근 제어 서비스를 제공할 수 있다.
- 단점
    1. 시스템 전체 차원에서 일관성 있는 접근제어가 부족하다.
    2. 높은 접근 권한을 가진 사용자가 다른 사용자에게 임의적으로 접근을 허용할 수 있다.
    3. 멀웨어, 바이러스, 웜, 루트 킷, 트로이 목마 공격에 취약하다

### 3. 역할기반 접근통제(RBAC; Role Based Access Control)

주체와 객체 사이에 역할을 두어 역할에 따라 접근통제한다. 역할은 사용자의 집합과 권한 집합의 매개체로 작용한다. 강제적 접근제어와 임의적 접근제어의 대안으로 사용된다.

![2](/assets/images/2022-09-04-AppArmor-and-SELinux/2.png)

출처: [[정보보안기사] 10. 접근통제 보안 모델](https://peemangit.tistory.com/191) [티스토리]

인사담당자, 총무담당자와 같이 권한 그룹을 통해 접근을 제어하는 직무 기반 접근통제이다. 권한의 최소화와 직무의 분리, 데이터 추상화 보안 정책을 제공한다.

- 장점
    1. 관리자에게 편리한 관리를 제공한다.
    2. DAC 보다 유연성은 떨어지지만, 관리자에 의해 전체 시스템 관점에서 일관성 있는 접근제어가 가능하다.
    3. 최소 권한, 직무 분리 원칙을 충족시킬 수 있다.

## SELinux

SELinux 는 Security Enhanced Linux(보안 강화 리눅스) 의 약자로 리눅스의 커널을 보호하기 위한 도구이다. 과거 리눅스는 오픈소스였기 때문에 보안에 취약했는데, 이를 보완하기 위한 도구가 SELinux 이다.

시스템 전체에 보안 설정을 한다. 설정 및 관리가 어려운 반면 보안은 뛰어나다. 

## AppArmor

AppAromor 는 Application Armor 의 약자로, 시스템 관리자가 프로그램 프로필 별로 프로그램의 역량을 제한할 수 있게 해주는 리눅스 커널 보안 모듈이다. 강제적 접근 통제(MAC)를 제공함으로써 전통적인 유닉스 임의적 접근 통제(DAC)모델을 지원한다.

SELinux 에 비해 사용하기 쉽다는 장점이 있다. 개별 응용프로그램을 보호하며, 응용 프로그램 단위로 보안을 수행한다.

# 참고자료

- [리눅스 보안 모듈](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EB%B3%B4%EC%95%88_%EB%AA%A8%EB%93%88) [위키백과]
- [[정보보안기사] 10. 접근통제 보안 모델](https://peemangit.tistory.com/191) [티스토리]
- [보안 강화 리눅스](https://ko.wikipedia.org/wiki/%EB%B3%B4%EC%95%88_%EA%B0%95%ED%99%94_%EB%A6%AC%EB%88%85%EC%8A%A4) [위키백과]
- [AppArmor](https://ko.wikipedia.org/wiki/AppArmor) [위키백과]
- [보안 강화 리눅스(Security-Enhanced Linux)](https://lesstif.gitbooks.io/web-service-hardening/content/selinux.html) [gitbooks.io]