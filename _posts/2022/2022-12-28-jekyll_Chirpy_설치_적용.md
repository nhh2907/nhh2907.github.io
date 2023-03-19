---
layout: post
title: "Jekyll 깃허브 블로그 설정"
date: 2022-12-28 18:32:00 +0900
author: nhh2907
categories: [Github Blog, Chirpy]
tag: [Jekyll]
---

# Chirpy 설치 방법 - 6단계
> [한준혁님 Chirpy블로그](https://github.com/Han-Joon-Hyeok/Han-Joon-Hyeok.github.io)를 참조했음. 다른 블로그는 전부 실패함

1. 깃허브에서 새로운 레파지토리 생성: 
    - 깃허브 레포지토리 이름 : [깃허브 아이디].github.io
2. 깃허브 레포지토레에서 Permission 설정  
You have to configure your Repository Settings → Action → General → Workflow permissions and choose **Read and Write Permissions**
3. [해당 깃허브](https://github.com/Han-Joon-Hyeok/Han-Joon-Hyeok.github.io)에 들어가서 테마를 다운로드 한다
4. 원하는 로컬 폴더에 앞축을 푼다
5. 터미널에서 다음 명령어를 실행

<pre><code>git init
git branch -M main
git remote add origin [깃허브 레포지토리 SSH]
git add .
git commit -m "[주석]"
git push -u origin main
</code></pre>

- 푸시를 한 이후에 자동으로 gh-pages 브랜치를 생성됨

6. gh-pages 브랜치 설정  
your repository - Settings →  Pages →  Build and deployment →  Branch에서 main 브랜치를 **gh-pages 브랜치**로 변경 후 저장 

<br>

# Jekyll Chirpy 테마 설치 및 적용
- [Jekyll Chirpy 테마 사용하여 블로그 만들기](https://www.irgroup.org/posts/jekyll-chirpy/)
- [Chirpy 테마 커스터마이징](https://www.irgroup.org/posts/Chirpy-%ED%85%8C%EB%A7%88-%EC%BB%A4%EC%8A%A4%ED%84%B0%EB%A7%88%EC%9D%B4%EC%A7%95/)
- [jekyll에서 마크다운(Markdown) 사용하기](https://www.irgroup.org/posts/usage-markdown/)
- [Jekyll 테마에 utterances 댓글 연동하기](https://www.irgroup.org/posts/utternace-comments-system/)
- [컴퓨터 한대로 github 여러 계정 사용하기](https://www.irgroup.org/posts/github-%EC%BB%B4%ED%93%A8%ED%84%B0-%ED%95%9C%EB%8C%80%EB%A1%9C-%EC%97%AC%EB%9F%AC-%EA%B3%84%EC%A0%95-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/)
- [Jekyll 테마에서 구글 검색 노출 등록하기](https://www.irgroup.org/posts/jekyll-google-search/)

> 본 Jekyll Chirpy 관련 링크는 [하얀눈길 블로그님](https://www.irgroup.org/) 작성 글이다