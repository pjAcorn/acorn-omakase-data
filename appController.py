from flask import Flask, request, json, jsonify
import csv
import pandas as pd

PORT_NUM = 8000

app = Flask(__name__)

def analyzeData(recievedData):
    CSVDf = pd.read_csv("./years.csv")

    addressSido = recievedData['addressSido']
    addressSigungu = recievedData['addressSigungu']
    cateLData = recievedData['cateLData']
    cateAData = recievedData['cateAData']
    cateMData = recievedData['cateMData']

    resultDf = CSVDf[(CSVDf['시도'] == addressSido) & (CSVDf['시군구'] == addressSigungu) &
        (CSVDf['업종대분류'] == cateLData) & (CSVDf['분류'] == cateAData) & (CSVDf['업종중분류'] == cateMData)]
    resultDf.drop({"시도", "시군구", "업종대분류", "분류", "업종중분류"}, axis=1, inplace=True)

    responseData = pd.Series.to_json(resultDf, force_ascii=False)
    print(responseData)

    return responseData 


@app.route("/analyze", methods=['POST'])
def receiveData():
    receivedData = request.get_json()
    print("받은 데이터 ", receivedData)

    response = analyzeData(receivedData)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT_NUM)