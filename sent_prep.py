from tqdm import tqdm


ADL_uri = []
ADL_resp = []
ADL_pos = []
ADL_outbed =[]
ADL_meal=[]
new_patient_list = []
new_date_list = []

def adl_pre(test):
    for num, i in tqdm(enumerate(test['agg'].tolist())):
        patient = i.split('_')[0]
        new_patient_list.append(patient)
        date = i.split('_')[1]
        new_date_list.append(date)
        detail = i.split('_')[2]
    
        ## 배뇨배변 ###
        if detail =="도움 없음(도움 없이 배변, 배뇨를 위한 일련의 행위, 장루관리를 스스로 할 수 있는 경우, 관장하는 경우)":
            detail_input = patient+'_'+date+'_'+'0'
            ADL_uri.append(detail_input)
        elif detail =="도움없음(배변을 위한 일련의 행위 모두를 스스로 할 수 있는 경우)":
            detail_input = patient+'_'+date+'_'+'0'
            ADL_uri.append(detail_input)
        elif detail == '일부 도움(도움 없이 배변, 배뇨를 위한 일련의 행위를 하는데 어려움이 있어 간호직원 등의 일부 도움이 반드시 필요한 경우,  정서장애, 인지장애, 혈압조절장애 등으로 인하여 배변, 배뇨를 하는 동안 반드시 누군가 곁에서 관찰, 감독이 필요한 경우, Foley-catheter 적용중인 경우)(nelaton catheter제외)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_uri.append(detail_input)
        elif detail == '일부도움(배변을 위한 일련의 행위에 일부 도움이 행해지는 경우)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_uri.append(detail_input)
        elif detail =='전부 도움(스스로 배변 배뇨를 위한 일련의 행위 모두를 전혀 할 수 없어 간호 직원 등에 의해 전적인 도움 필요, 기저귀 착용,장루관리를 간호직원이 하는 경우)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_uri.append(detail_input)
        elif detail =='전부도움(배변을 위한 일련의 행위에 전부 도움이 행해지는 경우, 활동에 제한이 있어 기저귀를 적용한 환자 모두 포함)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_uri.append(detail_input)

        ### 식사섭취###
        if detail == '도움 없음(도움, 관찰 없이 스스로 식사 가능한 경우, 보조기구 이용 스스로 식사 가능한 경우, NPO, TPN 등의 사유로 식사하는 행위가 미발생 하는 경우)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_meal.append(detail_input)
        elif detail == '도움없음(도움, 지켜보는 것 없이 스스로 식사를 할 수 있는 경우, 젓가락, 숟가락 이외의 다른 보조기구등을 사용하는 경우, 식사중지, 단식의 경우)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_meal.append(detail_input)
        elif detail == '일부 도움(간단한 식사도구는 스스로 다룰 수 있으나 작게 자르기, 껍질 벗기기, 생선 바르기 등을 스스로 할 수 없어 간호직원 등의 도움이 필요한 경우,  흡인( aspiration) 과거력, 인지장애, 연하곤란(dysphagia) 등으로 인하여 식사하는 동안 반드시 누군가 곁에서 관찰, 감독이 필요한 경우) ':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_meal.append(detail_input)
        elif detail == '일부도움(필요에 따라 식사 섭취 행위의 일부에 도움을 주는 경우, 식탁에서 먹기 편하도록 배려하는 행위가 이루어 지고 있는 경우, 식사 중 한 가지라도 도움을 주는 경우, 지켜보며 지시가 필요한 경우)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_meal.append(detail_input)
        elif detail == '전부 도움(혼자서는 식사를 전혀 할 수 없어 간호직원 등에 의해 모든 과정에서 전적인 도움(스푼 피딩)을 받아야 함)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_meal.append(detail_input)
        elif detail == '전부도움(스스로는 전혀 먹을 수 없고 모든 것에 도움이 필요한 경우, 식사 시작부터 끝까지 모든 도움이 필요한 경우)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_meal.append(detail_input)

            ### 체위변경 ###
        elif detail =='도움없음(도움 없이 스스로 변경 가능, 한쪽으로만 변경이 가능해도 됨, 침대 난간, 끈, 바, 사이드 레일 등을 사용하는 경우)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_pos.append(detail_input)
        elif detail =='도움없음(침대에서 뒤척임을 환자 스스로 할 수 있는 경우)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_pos.append(detail_input)
        elif detail =='일부 도움(스스로 체위 변경을 하는데 어려움이 있어 간호 직원 등이 팔 또는 몸의 일부를 지지하는 도움이 반드시 필요, 환자가 스스로 할 수 있으나, 간호직원 등이 도움을 주는 경우 제외)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_pos.append(detail_input)
        elif detail =='일부도움(침대 난간, 끈, 바, 사이드레일 등을 잡으면 혼자서 침대에서 뒤척임을 할 수 있는 경우)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_pos.append(detail_input)
        elif detail =='전부 도움(혼자서는 침상 밖으로 이동을 전혀 할 수 없어 간호직원 등에 의해 안고, 옮겨주는(기구 혹은 장비 이용 포함) 등의  전적인 도움을 받는 경우)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_pos.append(detail_input)
        elif detail =='전부도움(침대에서 뒤척이는데 도움이 필요한 경우)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_pos.append(detail_input)
        elif detail =='전부 도움(체위 변경을 혼자서는 전혀 할 수 없어 간호 직원 등에 의해 모든 과정에서 전적인 도움을 받아야 함)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_pos.append(detail_input)

            ### 호흡 ###
        elif detail =='해당없음(ex.비침습적 양압환기 및 가온 가습 고유량 비강캐뉼라 요법)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_resp.append(detail_input)
        elif detail =='해당없음':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_resp.append(detail_input)
        elif detail =='비강캐뉼라, 산소마스크 등을 이용하여 산소투여하고 시행하고 기록이 있는 경우':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_resp.append(detail_input)
        elif detail =='T-cannula, E-tube 등을 통한 흡인간호, 드레싱 교환, T-cannula 교환':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_resp.append(detail_input)

            ### 침상이동 ###
        elif detail == '도움 없음(도움 없이 스스로 침상 밖으로 이동이 가능, 무언가 잡거나 보조기구를 이용하여 스스로 가능한 경우, 와상, 절대안정 등의 사유로 침상 밖으로 이동이 없는 경우에 해당, 이동하기 위해 보조기구를 준비, 사이드 레일을 내리는 등의 도움은 포함하지 않음)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_outbed.append(detail_input)
        elif detail == '도움없음(도움없이 이동할 수 있는 경우, 기어서라도 이동을 스스로 할 수 있는경우도 포함)':
            detail_input = patient+'_'+date+'_'+'0'
            ADL_outbed.append(detail_input)
        elif detail == '일부 도움(스스로 침상 밖으로 나오는데 어려움이 있어 팔 또는 몸의 일부를 지지하는 도움이나 관찰이  반드시 필요함, 환자의 허약, 장애, 약물, 낙상 과거력, 치료기구 등으로 인하여 침상 밖으로 이동할 때마다 관찰이 필요한 경우)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_outbed.append(detail_input)
        elif detail == '일부도움(직접 도움을 줄 필요는 없지만 사고 등이 나지 않도록 지켜보는 경우, 들것에 이동 시 환자가 자력으로 조금씩 이동할 수 있는 경우, 부분적 도움이 행해지는 경우, 위험이 없도록 간호사 등이 추가 도움을 주는 경우)':
            detail_input = patient+'_'+date+'_'+'1'
            ADL_outbed.append(detail_input)
        elif detail == '전부 도움(혼자서는 침상 밖으로 이동을 전혀 할 수 없어 간호직원 등에 의해 안고, 옮겨주는(기구 혹은 장비 이용 포함) 등의  전적인 도움을 받는 경우)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_outbed.append(detail_input)
        elif detail == '전부도움(자신이 이동을 전혀 할 수 없는 경우, 전면적인 도움이 행해지는 경우)':
            detail_input = patient+'_'+date+'_'+'2'
            ADL_outbed.append(detail_input)


        else:
            pass
        
        
    return ADL_uri, ADL_resp, ADL_pos, ADL_outbed, ADL_meal, new_patient_list, new_date_list




def sent_prep(test_str):
    fall_history = []
    help_list = []
    drug_history = []
    secondary = []
    heparin_list = []
    mental_list = []
    walk_list =[]

    format_ = '%Y-%m-%d'

    for num, i in enumerate(test_str['등록번호'].tolist()):
        
        ### 낙상경험
        if ' 지난 3개월간 낙상 경험-없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            fall_history.append(detail)
        elif ' 지난 3개월간 낙상 경험-있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            fall_history.append(detail)
        elif '환경요인-낙상 경험이 있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            fall_history.append(detail)
        ### 서울###
        elif '지난 3개월간 낙상 경험-없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            fall_history.append(detail)
        elif '지난 3개월간 낙상 경험-있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            fall_history.append(detail)
        elif '환경요인-낙상 경험이 있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            fall_history.append(detail)
        ### 보행보조
        elif '보행보조-보행 불가능(침상안정) 또는 보조기구 없이 보행 가능함' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            help_list.append(detail)
        elif '보행보조-목발/지팡이/보행기 등 보조기구 사용하여 혼자 보행 가능함' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            help_list.append(detail)
        elif '보행보조-혼자 할수 없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'2'
            help_list.append(detail)
        elif '보행보조-혼자 할 수 없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'2'
            help_list.append(detail)
        
        ### 이차진단    
        elif '이차 진단 (부진단)-없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            secondary.append(detail)
        elif '이차 진단 (부진단)-있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            secondary.append(detail)
            
        ### 헤파린
        elif '정맥수액요법/헤파린록(heparin lock)-없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            heparin_list.append(detail)
        elif '정맥수액요법/헤파린록(heparin lock)-있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            heparin_list.append(detail)
        ### 약물사용
        elif  '약물사용-다른 약물 / 해당 없음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            drug_history.append(detail)
        elif  '약물사용-2시간이상 진정제, 수면제, 최면제, 정신안정제, 항불안제, 완화제/이뇨제, 진통제 투여' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            drug_history.append(detail)
    
        ### 걸음걸이/이동
        elif '걸음걸이/이동-정상/침상안정/부동' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            walk_list.append(detail)
        elif '걸음걸이/이동-허약함' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            walk_list.append(detail)
        elif '걸음걸이/이동-장애가 있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'2'
            walk_list.append(detail)
            ###서울###
            
        ### 의식정신상태
        elif  '의식/정신상태-자신의 기능 수준에 대해 잘 알고 있음' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'0'
            mental_list.append(detail)
        elif '의식/정신상태-자신의 기능수준을 과대평가하거나 잊어버림' in test_str['agg'].tolist()[num]:
            detail = test_str['agg'].tolist()[num] +'//'+'1'
            mental_list.append(detail)
           
        else:
            print(test_str['agg'].tolist()[num])

    return fall_history, help_list, drug_history, secondary, heparin_list, mental_list, walk_list
