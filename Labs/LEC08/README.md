# Drill 8 애니메이션 뷰어

제출 브랜치: `drill-08-animation-viewer`

## 실행

프로젝트 루트에서 다음 명령으로 실행합니다. 기존 프로젝트의 pico2d 가상환경을 사용합니다.

```powershell
.\.venv\Scripts\python.exe .\Labs\LEC08\animation_viewer.py
```

VS Code에서 `Labs/LEC08/animation_viewer.py`를 열고 해당 가상환경으로 실행해도 됩니다. 이미지 경로는 소스 파일 위치를 기준으로 계산하므로 터미널의 현재 폴더에 영향을 받지 않습니다. ESC 또는 창 닫기로 종료합니다. 이전 위치의 `Labs/LEC08_Animation/animation_viewer.py`도 새 실행 파일로 연결됩니다.

## 과제 기본 조건

| 조건 | 구현 |
| --- | --- |
| 최소 4종 애니메이션 | 걷기, 달리기, 회전, 넘어지기 순서 |
| 캐릭터 확대 | 모든 프레임에 같은 확대율을 적용하고 종횡비 유지. 각 프레임의 표시 높이가 600픽셀 화면의 절반 이상인지 테스트 |
| 지정 파일과 폴더 | `Labs/LEC08/animation_viewer.py` |
| 화면 중앙 재생 | 위치 `(400, 300)` 고정 |
| 동작마다 5회 반복 | 각 동작의 실제 프레임 수를 기준으로 5회 재생 |
| 반복 후 1초 정지 | 다섯 번째 재생의 마지막 프레임을 추가로 1초 유지 |
| 전체 무한 반복 | 마지막 동작의 정지가 끝나면 첫 동작으로 복귀 |
| 적절한 재생 속도 | 프레임당 0.1초(초당 10프레임), 실제 경과 시간으로 계산 |
| 과제별 브랜치 분리 | `drill-08-animation-viewer` |
| 충분한 커밋 기록 | 자료 구조·각 동작 좌표·재생·화면 출력·검증·문서 변경을 구분해 한국어로 기록 |

`sonic-sprite.png`는 기존 수업 프로젝트에 있던 이미지를 그대로 복사했습니다. 이미지에 표기된 제작·수정 크레딧을 보존했습니다. 외부에서 새로 다운로드하거나 직접 제작한 이미지로 주장하지 않습니다.

## 검사

```powershell
cd Labs\LEC08
..\..\.venv\Scripts\python.exe animation_viewer.py --validate
..\..\.venv\Scripts\python.exe -m unittest discover -v
git log --oneline main..drill-08-animation-viewer
git rev-list --count main..drill-08-animation-viewer
```

자동 검사는 실제 좌표 범위, 서로 다른 프레임 수와 크기, 5회 반복, 1초 정지 경계, 여러 차례 전체 순환, 확대 크기, 재생·정지 중 종료 입력을 확인합니다. 모든 프레임을 실제 pico2d로 출력하는 시각 점검도 별도로 수행했습니다.

추가점수 구현과 제출 시 설명할 내용은 `BONUS.md`를 참고하세요. 점수 인정은 담당 채점자의 판단에 따릅니다.
