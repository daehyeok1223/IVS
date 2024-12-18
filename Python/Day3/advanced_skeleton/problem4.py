import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.

def get_deposit_products():
    api_key = '1a9fb2baf17c6066cf13d56da82c4bee'
    url = 'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(url, params = params).json()
    base_list = response['result']['baseList']  # 기본 상품 리스트
    option_list = response['result']['optionList']  # 옵션 리스트
    result = []
    for product in base_list:
        new_product = dict()
        options = []
        for option in option_list:
            new_option = {}
            if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                new_option['저축금리유형'] = option['intr_rate_type']
                new_option['저축금리유형명'] = option['intr_rate_type_nm']
                new_option['저축기간'] = option['save_trm']
                new_option['저축금리'] = option['intr_rate']
                new_option['최고우대금리'] = option['intr_rate2']
                options.append(new_option)
        new_product['금리정보'] = options
        new_product['금융회사명'] = product['kor_co_nm']
        new_product['금융상품명'] = product['fin_prdt_nm']
        result.append(new_product)


    return result
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)


