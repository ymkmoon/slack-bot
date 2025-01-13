# slack-bot
슬랙 봇 API 를 연동하여 스레드 이모지 노티 어플리케이션


## 가상 환경
### 가상 환경 생성

```
python -m venv venv
```

### 가상 환경 활성화

```
.\venv\Scripts\activate
```

#### 권한 에러 발생 시
1. Windows PowerShell 관리자로 실행
2. Set-ExecutionPolicy RemoteSigned 입력 후 Y 입력
3. 다시 활성화 시도 & 패키지 설치 (ex. xlwings)

```
pip install xlwings
```

### 가상환경 내 패키지 목록 저장

```
pip freeze > requirements.txt
```

### vscode 설정
- 단축키 : Ctrl + Shift + P
- Python: Select Interpreter 클릭 후 가상 환경 선택 (venv)

### 가상 환경 비활성화

```
deactivate
```

### 가상 환경 폴더 삭제

```
rmdir venv
```

### vscode 설정 해제
단축키 : Ctrl + Shift + P
Python: Select Interpreter 클릭 후 기존 환경 선택 (글로벌)

### 공용 공간 패키지 + 가상 환경 생성

```
python -m venv venv --system-site-packages
```

### 패키지 설치 (requirements.txt 파일로부터)

```
pip install -r requirements.txt
```

### 가상 환경 내 패키지 목록 조회

```
pip list --local
```

## 프로젝트 패키지 설치

- 프로젝트 경로 이동

```
python -m pip install --upgrade pip

pip install flask
```
