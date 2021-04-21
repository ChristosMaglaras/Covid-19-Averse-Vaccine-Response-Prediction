import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    colnames = ['AGE_YRS','SEX','DISABLE','BIRTH_DEFECT','VAX_DOSE_SERIES','none cur_ill','nka','nkda','penicillin','sulfa','pcn','latex','codeine','amoxicillin','sulfa drugs','shellfish','morphine','bactrim','seasonal allergies cur_ill','erythromycin','aspirin','sulfa antibiotics','augmentin','lisinopril meds','lactose','denies','penicillins','bee stings','cipro','iodine','nickel','levaquin','seasonal','ceclor','percocet','compazine','gluten','nkma','doxycycline','nsaids','keflex','ibuprofen meds','naproxen','codiene','tree nuts','bee venom','peanuts','clindamycin','none history','covid-19 history','asthma history','uti','seasonal allergies history','sinus infection','hypertension history','diabetes history','migraines history','blood pressure high','urinary tract infection','migraine history','hypothyroidism history','allergies','anxiety history','diabetic','gerd history','cold','sinusitis','acid reflux','copd history','new diagnosis of t2dm','fibromyalgia history','rheumatoid arthritis history','none meds','asthma','hypertension','hypothyroidism','diabetes','high blood pressure','migraines','htn','covid-19','anxiety','gerd','obesity','depression','hypothyroid','arthritis','rheumatoid arthritis','high cholesterol','copd','seasonal allergies','penicillin allergy','fibromyalgia','migraine','pcos','hyperlipidemia','lupus','ibs','sulfonamide allergy','ulcerative colitis','psoriasis','adhd','none','multivitamin','tylenol','synthroid','levothyroxine','birth control','ibuprofen','vitamin d','lexapro','prenatal vitamins','zyrtec','adderall','zoloft','vitamins','lisinopril','prenatal vitamin','metformin','multi vitamin','multivitamins','losartan','prozac','wellbutrin','flonase','eliquis','metoprolol','vitamin c','nuvaring','atorvastatin','omeprazole','melatonin','insulin','birth control pill','multi-vitamin','mirena iud','acetaminophen','amlodipine','daily multivitamin','prilosec','sertraline','albuterol','vitamin d3','birth control pills','coumadin','allegra','benadryl','STATE: _0','STATE: _1','STATE: _2','STATE: _3','STATE: _4','STATE: _5','STATE: _6','STATE: _7','STATE: _8','STATE: _9','STATE: _10','STATE: _11','STATE: _12','STATE: _13','STATE: _14','STATE: _15','STATE: _16','STATE: _17','STATE: _18','STATE: _19','STATE: _20','STATE: _21','STATE: _22','STATE: _23','STATE: _24','STATE: _25','STATE: _26','STATE: _27','STATE: _28','STATE: _29','STATE: _30','STATE: _31','STATE: _32','STATE: _33','STATE: _34','STATE: _35','STATE: _36','STATE: _37','STATE: _38','STATE: _39','STATE: _40','STATE: _41','STATE: _42','STATE: _43','STATE: _44','STATE: _45','STATE: _46','STATE: _47','STATE: _48','STATE: _49','STATE: _50','STATE: _51','STATE: _52','STATE: _53','BRAND: _0','BRAND: _1','BRAND: _2','BRAND: _3','VAX_SITE: _0','VAX_SITE: _1','VAX_SITE: _2','VAX_SITE: _3','VAX_SITE: _4','VAX_SITE: _5','VAX_SITE: _6','VAX_SITE: _7','VAX_SITE: _8','VAX_SITE: _9','VAX_ROUTE: _0','VAX_ROUTE: _1','VAX_ROUTE: _2','VAX_ROUTE: _3','VAX_ROUTE: _4','VAX_ROUTE: _5','VAX_ROUTE: _6','ADMINBY: _0','ADMINBY: _1','ADMINBY: _2','ADMINBY: _3','ADMINBY: _4','ADMINBY: _5','ADMINBY: _6','ADMINBY: _7','ADMINBY: _8']
    df = pd.DataFrame(columns=colnames)    
    df = df.append(pd.Series(0, index=df.columns), ignore_index=True)
    
    data2 = request.form['Brand']
    if data2 == "Moderna":
        df['BRAND: _1'] = 1
    elif data2 == "Phizer":
        df['BRAND: _2'] = 1
    elif data2 == "Janssen":
        df['BRAND: _3'] = 1
    else:
        df['BRAND: _0'] = 1
    
    data3 = request.form['Administrator']
    if data3 == "Public":
        df['ADMINBY: _3'] = 1
    if data3 == "Private":
        df['ADMINBY: _4'] = 1
    elif data3 == "Senior Home":
        df['ADMINBY: _6'] = 1
    elif data3 == "School":
        df['ADMINBY: _5'] = 1
    elif data3 == "Military":
        df['ADMINBY: _0'] = 1
    elif data3 == "Pharmacy":
        df['ADMINBY: _2'] = 1
    elif data3 == "Workplace":
        df['ADMINBY: _8'] = 1
    elif data3 == "Unknown":
        df['ADMINBY: _7'] = 1
    else:
        df['ADMINBY: _1'] = 1
        
    data4 = request.form['Administration Route']
    if data4 == "Intradermal":
        df['VAX_ROUTE: _0'] = 1
    elif data4 == "Intramuscular":
        df['VAX_ROUTE: _1'] = 1
    elif data4 == "Subcutaneous":
        df['VAX_ROUTE: _4'] = 1
    elif data4 == "Srynge":
        df['VAX_ROUTE: _5'] = 1
    elif data4 == "Jet":
        df['VAX_ROUTE: _2'] = 1
    elif data4 == "Unknown":
        df['VAX_ROUTE: _6'] = 1
    else:
        df['VAX_ROUTE: _3'] = 1
    
    data5 = request.form['Administration Site']
    if data5 == "Left Arm":
        df['VAX_SITE: _2'] = 1
    elif data5 == "Right Arm":
        df['VAX_SITE: _7'] = 1
    elif data5 == "Arm":
        df['VAX_SITE: _0'] = 1
    elif data5 == "Left Leg":
        df['VAX_SITE: _4'] = 1
    elif data5 == "Right Leg":
        df['VAX_SITE: _8'] = 1
    elif data5 == "Leg":
        df['VAX_SITE: _1'] = 1
    elif data5 == "Unknown":
        df['VAX_SITE: _9'] = 1
    else:
        df['VAX_SITE: _6'] = 1
    
    
    
    try:
        df['AGE_YRS'] = request.form['AGE_YRS']
    except:
        pass
    try:
        df['SEX'] = request.form['SEX']
    except:
        pass
    try:
        df['DISABLE'] = request.form['DISABLE']
    except:
        pass
    try:
        df['BIRTH_DEFECT'] = request.form['BIRTH_DEFECT']
    except:
        pass
    try:
        df['VAX_DOSE_SERIES'] = request.form['VAX_DOSE_SERIES']
    except:
        pass
    try:
        df['none'] = request.form['none']
    except:
        pass
    try:
        df['cur_ill'] = request.form['cur_ill']
    except:
        pass
    try:
        df['nka'] = request.form['nka']
    except:
        pass
    try:
        df['nkda'] = request.form['nkda']
    except:
        pass
    try:
        df['penicillin'] = request.form['penicillin']
    except:
        pass
    try:
        df['sulfa'] = request.form['sulfa']
    except:
        pass
    try:
        df['pcn'] = request.form['pcn']
    except:
        pass
    try:
        df['latex'] = request.form['latex']
    except:
        pass
    try:
        df['codeine'] = request.form['codeine']
    except:
        pass
    try:
        df['amoxicillin'] = request.form['amoxicillin']
    except:
        pass
    try:
        df['sulfa drugs'] = request.form['sulfa drugs']
    except:
        pass
    try:
        df['shellfish'] = request.form['shellfish']
    except:
        pass
    try:
        df['morphine'] = request.form['morphine']
    except:
        pass
    try:
        df['bactrim'] = request.form['bactrim']
    except:
        pass
    try:
        df['seasonal allergies cur_ill'] = request.form['seasonal allergies cur_ill']
    except:
        pass
    try:
        df['erythromycin'] = request.form['erythromycin']
    except:
        pass
    try:
        df['aspirin'] = request.form['aspirin']
    except:
        pass
    try:
        df['sulfa antibiotics'] = request.form['sulfa antibiotics']
    except:
        pass
    try:
        df['augmentin'] = request.form['augmentin']
    except:
        pass
    try:
        df['lisinopril meds'] = request.form['lisinopril meds']
    except:
        pass
    try:
        df['lactose'] = request.form['lactose']
    except:
        pass
    try:
        df['denies'] = request.form['denies']
    except:
        pass
    try:
        df['penicillins'] = request.form['penicillins']
    except:
        pass
    try:
        df['bee stings'] = request.form['bee stings']
    except:
        pass
    try:
        df['cipro'] = request.form['cipro']
    except:
        pass
    try:
        df['iodine'] = request.form['iodine']
    except:
        pass
    try:
        df['nickel'] = request.form['nickel']
    except:
        pass
    try:
        df['levaquin'] = request.form['levaquin']
    except:
        pass
    try:
        df['seasonal'] = request.form['seasonal']
    except:
        pass
    try:
        df['ceclor'] = request.form['ceclor']
    except:
        pass
    try:
        df['percocet'] = request.form['percocet']
    except:
        pass
    try:
        df['compazine'] = request.form['compazine']
    except:
        pass
    try:
        df['gluten'] = request.form['gluten']
    except:
        pass
    try:
        df['nkma'] = request.form['nkma']
    except:
        pass
    try:
        df['doxycycline'] = request.form['doxycycline']
    except:
        pass
    try:
        df['nsaids'] = request.form['nsaids']
    except:
        pass
    try:
        df['keflex'] = request.form['keflex']
    except:
        pass
    try:
        df['ibuprofen meds'] = request.form['ibuprofen meds']
    except:
        pass
    try:
        df['naproxen'] = request.form['naproxen']
    except:
        pass
    try:
        df['codiene'] = request.form['codiene']
    except:
        pass
    try:
        df['tree nuts'] = request.form['tree nuts']
    except:
        pass
    try:
        df['bee venom'] = request.form['bee venom']
    except:
        pass
    try:
        df['peanuts'] = request.form['peanuts']
    except:
        pass
    try:
        df['clindamycin'] = request.form['clindamycin']
    except:
        pass
    try:
        df['none history'] = request.form['none history']
    except:
        pass
    try:
        df['covid-19 history'] = request.form['covid-19 history']
    except:
        pass
    try:
        df['asthma history'] = request.form['asthma history']
    except:
        pass
    try:
        df['uti'] = request.form['uti']
    except:
        pass
    try:
        df['seasonal allergies history'] = request.form['seasonal allergies history']
    except:
        pass
    try:
        df['sinus infection'] = request.form['sinus infection']
    except:
        pass
    try:
        df['hypertension history'] = request.form['hypertension history']
    except:
        pass
    try:
        df['diabetes history'] = request.form['diabetes history']
    except:
        pass
    try:
        df['migraines history'] = request.form['migraines history']
    except:
        pass
    try:
        df['blood pressure high'] = request.form['blood pressure high']
    except:
        pass
    try:
        df['urinary tract infection'] = request.form['urinary tract infection']
    except:
        pass
    try:
        df['migraine history'] = request.form['migraine history']
    except:
        pass
    try:
        df['hypothyroidism history'] = request.form['hypothyroidism history']
    except:
        pass
    try:
        df['allergies'] = request.form['allergies']
    except:
        pass
    try:
        df['anxiety history'] = request.form['anxiety history']
    except:
        pass
    try:
        df['diabetic'] = request.form['diabetic']
    except:
        pass
    try:
        df['gerd history'] = request.form['gerd history']
    except:
        pass
    try:
        df['cold'] = request.form['cold']
    except:
        pass
    try:
        df['sinusitis'] = request.form['sinusitis']
    except:
        pass
    try:
        df['acid reflux'] = request.form['acid reflux']
    except:
        pass
    try:
        df['copd history'] = request.form['copd history']
    except:
        pass
    try:
        df['new diagnosis of t2dm'] = request.form['new diagnosis of t2dm']
    except:
        pass
    try:
        df['fibromyalgia history'] = request.form['fibromyalgia history']
    except:
        pass
    try:
        df['rheumatoid arthritis history'] = request.form['rheumatoid arthritis history']
    except:
        pass
    try:
        df['none meds'] = request.form['none meds']
    except:
        pass
    try:
        df['asthma'] = request.form['asthma']
    except:
        pass
    try:
        df['hypertension'] = request.form['hypertension']
    except:
        pass
    try:
        df['hypothyroidism'] = request.form['hypothyroidism']
    except:
        pass
    try:
        df['diabetes'] = request.form['diabetes']
    except:
        pass
    try:
        df['high blood pressure'] = request.form['high blood pressure']
    except:
        pass
    try:
        df['migraines'] = request.form['migraines']
    except:
        pass
    try:
        df['htn'] = request.form['htn']
    except:
        pass
    try:
        df['covid-19'] = request.form['covid-19']
    except:
        pass
    try:
        df['anxiety'] = request.form['anxiety']
    except:
        pass
    try:
        df['gerd'] = request.form['gerd']
    except:
        pass
    try:
        df['obesity'] = request.form['obesity']
    except:
        pass
    try:
        df['depression'] = request.form['depression']
    except:
        pass
    try:
        df['hypothyroid'] = request.form['hypothyroid']
    except:
        pass
    try:
        df['arthritis'] = request.form['arthritis']
    except:
        pass
    try:
        df['rheumatoid arthritis'] = request.form['rheumatoid arthritis']
    except:
        pass
    try:
        df['high cholesterol'] = request.form['high cholesterol']
    except:
        pass
    try:
        df['copd'] = request.form['copd']
    except:
        pass
    try:
        df['seasonal allergies'] = request.form['seasonal allergies']
    except:
        pass
    try:
        df['penicillin allergy'] = request.form['penicillin allergy']
    except:
        pass
    try:
        df['fibromyalgia'] = request.form['fibromyalgia']
    except:
        pass
    try:
        df['migraine'] = request.form['migraine']
    except:
        pass
    try:
        df['pcos'] = request.form['pcos']
    except:
        pass
    try:
        df['hyperlipidemia'] = request.form['hyperlipidemia']
    except:
        pass
    try:
        df['lupus'] = request.form['lupus']
    except:
        pass
    try:
        df['ibs'] = request.form['ibs']
    except:
        pass
    try:
        df['sulfonamide allergy'] = request.form['sulfonamide allergy']
    except:
        pass
    try:
        df['ulcerative colitis'] = request.form['ulcerative colitis']
    except:
        pass
    try:
        df['psoriasis'] = request.form['psoriasis']
    except:
        pass
    try:
        df['adhd'] = request.form['adhd']
    except:
        pass
    try:
        df['none'] = request.form['none']
    except:
        pass
    try:
        df['multivitamin'] = request.form['multivitamin']
    except:
        pass
    try:
        df['tylenol'] = request.form['tylenol']
    except:
        pass
    try:
        df['synthroid'] = request.form['synthroid']
    except:
        pass
    try:
        df['levothyroxine'] = request.form['levothyroxine']
    except:
        pass
    try:
        df['birth control'] = request.form['birth control']
    except:
        pass
    try:
        df['ibuprofen'] = request.form['ibuprofen']
    except:
        pass
    try:
        df['vitamin d'] = request.form['vitamin d']
    except:
        pass
    try:
        df['lexapro'] = request.form['lexapro']
    except:
        pass
    try:
        df['prenatal vitamins'] = request.form['prenatal vitamins']
    except:
        pass
    try:
        df['zyrtec'] = request.form['zyrtec']
    except:
        pass
    try:
        df['adderall'] = request.form['adderall']
    except:
        pass
    try:
        df['zoloft'] = request.form['zoloft']
    except:
        pass
    try:
        df['vitamins'] = request.form['vitamins']
    except:
        pass
    try:
        df['lisinopril'] = request.form['lisinopril']
    except:
        pass
    try:
        df['prenatal vitamin'] = request.form['prenatal vitamin']
    except:
        pass
    try:
        df['metformin'] = request.form['metformin']
    except:
        pass
    try:
        df['multi vitamin'] = request.form['multi vitamin']
    except:
        pass
    try:
        df['multivitamins'] = request.form['multivitamins']
    except:
        pass
    try:
        df['losartan'] = request.form['losartan']
    except:
        pass
    try:
        df['prozac'] = request.form['prozac']
    except:
        pass
    try:
        df['wellbutrin'] = request.form['wellbutrin']
    except:
        pass
    try:
        df['flonase'] = request.form['flonase']
    except:
        pass
    try:
        df['eliquis'] = request.form['eliquis']
    except:
        pass
    try:
        df['metoprolol'] = request.form['metoprolol']
    except:
        pass
    try:
        df['vitamin c'] = request.form['vitamin c']
    except:
        pass
    try:
        df['nuvaring'] = request.form['nuvaring']
    except:
        pass
    try:
        df['atorvastatin'] = request.form['atorvastatin']
    except:
        pass
    try:
        df['omeprazole'] = request.form['omeprazole']
    except:
        pass
    try:
        df['melatonin'] = request.form['melatonin']
    except:
        pass
    try:
        df['insulin'] = request.form['insulin']
    except:
        pass
    try:
        df['birth control pill'] = request.form['birth control pill']
    except:
        pass
    try:
        df['multi-vitamin'] = request.form['multi-vitamin']
    except:
        pass
    try:
        df['mirena iud'] = request.form['mirena iud']
    except:
        pass
    try:
        df['acetaminophen'] = request.form['acetaminophen']
    except:
        pass
    try:
        df['amlodipine'] = request.form['amlodipine']
    except:
        pass
    try:
        df['daily multivitamin'] = request.form['daily multivitamin']
    except:
        pass
    try:
        df['prilosec'] = request.form['prilosec']
    except:
        pass
    try:
        df['sertraline'] = request.form['sertraline']
    except:
        pass
    try:
        df['albuterol'] = request.form['albuterol']
    except:
        pass
    try:
        df['vitamin d3'] = request.form['vitamin d3']
    except:
        pass
    try:
        df['birth control pills'] = request.form['birth control pills']
    except:
        pass
    try:
        df['coumadin'] = request.form['coumadin']
    except:
        pass
    try:
        df['allegra'] = request.form['allegra']
    except:
        pass
    try:
        df['benadryl'] = request.form['benadryl']
    except:
        pass
    try:
        df['STATE: _0'] = request.form['STATE: _0']
    except:
        pass
    try:
        df['STATE: _1'] = request.form['STATE: _1']
    except:
        pass
    try:
        df['STATE: _2'] = request.form['STATE: _2']
    except:
        pass
    try:
        df['STATE: _3'] = request.form['STATE: _3']
    except:
        pass
    try:
        df['STATE: _4'] = request.form['STATE: _4']
    except:
        pass
    try:
        df['STATE: _5'] = request.form['STATE: _5']
    except:
        pass
    try:
        df['STATE: _6'] = request.form['STATE: _6']
    except:
        pass
    try:
        df['STATE: _7'] = request.form['STATE: _7']
    except:
        pass
    try:
        df['STATE: _8'] = request.form['STATE: _8']
    except:
        pass
    try:
        df['STATE: _9'] = request.form['STATE: _9']
    except:
        pass
    try:
        df['STATE: _10'] = request.form['STATE: _10']
    except:
        pass
    try:
        df['STATE: _11'] = request.form['STATE: _11']
    except:
        pass
    try:
        df['STATE: _12'] = request.form['STATE: _12']
    except:
        pass
    try:
        df['STATE: _13'] = request.form['STATE: _13']
    except:
        pass
    try:
        df['STATE: _14'] = request.form['STATE: _14']
    except:
        pass
    try:
        df['STATE: _15'] = request.form['STATE: _15']
    except:
        pass
    try:
        df['STATE: _16'] = request.form['STATE: _16']
    except:
        pass
    try:
        df['STATE: _17'] = request.form['STATE: _17']
    except:
        pass
    try:
        df['STATE: _18'] = request.form['STATE: _18']
    except:
        pass
    try:
        df['STATE: _19'] = request.form['STATE: _19']
    except:
        pass
    try:
        df['STATE: _20'] = request.form['STATE: _20']
    except:
        pass
    try:
        df['STATE: _21'] = request.form['STATE: _21']
    except:
        pass
    try:
        df['STATE: _22'] = request.form['STATE: _22']
    except:
        pass
    try:
        df['STATE: _23'] = request.form['STATE: _23']
    except:
        pass
    try:
        df['STATE: _24'] = request.form['STATE: _24']
    except:
        pass
    try:
        df['STATE: _25'] = request.form['STATE: _25']
    except:
        pass
    try:
        df['STATE: _26'] = request.form['STATE: _26']
    except:
        pass
    try:
        df['STATE: _27'] = request.form['STATE: _27']
    except:
        pass
    try:
        df['STATE: _28'] = request.form['STATE: _28']
    except:
        pass
    try:
        df['STATE: _29'] = request.form['STATE: _29']
    except:
        pass
    try:
        df['STATE: _30'] = request.form['STATE: _30']
    except:
        pass
    try:
        df['STATE: _31'] = request.form['STATE: _31']
    except:
        pass
    try:
        df['STATE: _32'] = request.form['STATE: _32']
    except:
        pass
    try:
        df['STATE: _33'] = request.form['STATE: _33']
    except:
        pass
    try:
        df['STATE: _34'] = request.form['STATE: _34']
    except:
        pass
    try:
        df['STATE: _35'] = request.form['STATE: _35']
    except:
        pass
    try:
        df['STATE: _36'] = request.form['STATE: _36']
    except:
        pass
    try:
        df['STATE: _37'] = request.form['STATE: _37']
    except:
        pass
    try:
        df['STATE: _38'] = request.form['STATE: _38']
    except:
        pass
    try:
        df['STATE: _39'] = request.form['STATE: _39']
    except:
        pass
    try:
        df['STATE: _40'] = request.form['STATE: _40']
    except:
        pass
    try:
        df['STATE: _41'] = request.form['STATE: _41']
    except:
        pass
    try:
        df['STATE: _42'] = request.form['STATE: _42']
    except:
        pass
    try:
        df['STATE: _43'] = request.form['STATE: _43']
    except:
        pass
    try:
        df['STATE: _44'] = request.form['STATE: _44']
    except:
        pass
    try:
        df['STATE: _45'] = request.form['STATE: _45']
    except:
        pass
    try:
        df['STATE: _46'] = request.form['STATE: _46']
    except:
        pass
    try:
        df['STATE: _47'] = request.form['STATE: _47']
    except:
        pass
    try:
        df['STATE: _48'] = request.form['STATE: _48']
    except:
        pass
    try:
        df['STATE: _49'] = request.form['STATE: _49']
    except:
        pass
    try:
        df['STATE: _50'] = request.form['STATE: _50']
    except:
        pass
    try:
        df['STATE: _51'] = request.form['STATE: _51']
    except:
        pass
    try:
        df['STATE: _52'] = request.form['STATE: _52']
    except:
        pass
    try:
        df['STATE: _53'] = request.form['STATE: _53']
    except:
        pass
    
    
    
    pred = model.predict(df)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)