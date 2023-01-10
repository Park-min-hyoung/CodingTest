# 1. 콜론 2개가 있는 곳을 찾음(zero group이 위치한 곳)
# => 나중에 zero group이 들어갈 수 있는 위치를 설정하기 위해
# => zero group이 아닌 그룹의 작업을 위해 콜론 2개를 콜론 1개로 수정 및 리스트로 변환
# 2. zero group이 아닌 그룹의 작업 => 주소의 개수가 4개가 아닌 주소를 4개로 수정(앞에 0과 뒤에 콜론 한개 붙여주기)
# 3. zero group 생성함에 있어 `8 - 나머지 그룹 개수`를 통해 몇개를 생성해야 할지 설정
# 4. 아까 1번에서 설정한 zero group이 들어갈 위치에다가 필요한 개수 만큼 넣어주고 출력

adress = input()

double_colon_idx = adress.find("::")
zero_group_idx = len(adress[:double_colon_idx].split(":"))
not_zero_address = "".join(adress.replace("::", ":"))

# zero group이 아닌 group의 작업
not_zero_lst = not_zero_address.split(":")
result = []
for adds in not_zero_lst:
    plus_cnt = 4 - len(adds)
    result.append(plus_cnt * '0' + adds + ':')

# zero group 작업
zero_group_cnt = 8 - len(not_zero_lst)
result.insert(zero_group_idx, "0000:" * zero_group_cnt)
print("".join(result)[:-1])