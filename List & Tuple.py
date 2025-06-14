# List와 Tuple - Python 자료구조
#list와 tuple은 파이썬에서 데이터를 저장하고 관리하는데 사용 되는 가장 기본적인 자료입니다

# 1. index (인덱스)
#각 항목에 부여된 고유한 번호라고 생각하면 된다(두가지의 세는 방법이 있는대 하나는 (positive)0부터세는 섯이고, 두번째는 뒤에서부터 (negative)1부터 세는 것이다)

# 2. List (리스트)
#리스트는 여러 개의 항목을 순서대로 저장할 수 있는 변경 가능한 (mutable) 데이터 타입입니다.
game=['overwatch','roblox','battlegrounds']

# 2-1. 항목 추가하기 (append())
game.append("valorant")

# 2-2. 항목 삽입하기 (insert()) / append와 insert의 차이는 append를 쓴다면 그 추가된 항목은 뒤로 가지만 insert는 그 추가한 항목의 위치를 설정 할 수 있다
game.insert(2,"chess")
            
# 2-3. 항목 제거하기 (remove())
game.remove("chess")
            
# 2-4. 인덱스로 항목 제거하기 (pop())
game2=game.pop(0)            
            
# 2-5. 항목 찾기 (index())
game3=game.index("battlegrounds")

# 2-6. 리스트 슬라이싱
          
# 3. Tuple (튜플)
#튜플은 리스트와 비슷하지만, 값이 변경되지 않는 불변 데이터 타입입니다(변경 불가능한(immutable)
