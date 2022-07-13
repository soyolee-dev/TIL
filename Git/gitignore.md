# Git 파일 관리 심화

## .gitignore 

- Git으로 **추적하지 않는 파일**을 관리

- 일반적인 개발 프로젝트에서 버전 관리와 관계 없는 파일이나 디렉토리가 발생

  - [gitignore.io](https://github.com/github/gitignore)에서 개발 언어, 개발 환경(OS, IDE) 등을 설정하여 파일을 생성할 수 있다

- Git 저장소에 **.gitignore 파일을 생성**하여 해당 내용을 관리

  - 특정 파일 : *a.txt* (모든 a.txt) 	

  ​					*test/a.txt* (test 폴더의 a.txt)

  - 특정 디렉토리 : */my_secret*
  - 특정 확장자 : **.exe*
  - 예외 처리 : **!** *b.exe*

- 이름 바꾸기 불가능





## .gitkeep

- **빈 폴더**를 커밋하기 위해 사용
- Git은 효율적으로 관리하기 위해 **파일**을 기준으로 하며 모든 하위 디렉토리의 파일을 추적하며 빈 폴더는 인식하지 않음
- 이름 바꾸기 가능