"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify, request
import random
import requests

from .template_parser import run, getAllFileNames

from .apibox import Apibox
from .volvo_connected_api import ConnectedApi
from .volvo_extended_api import ExtendedApi
from .gen_json import gen_json


api = Blueprint('api', __name__)


@api.route('/test/', methods=['GET'])
def testImport():
    r = run('test')
    return r


@api.route('/get-all-methods/', methods=['GET'])
def getMethods():
    method_list_apibox = [func for func in dir(Apibox) if callable(getattr(Apibox, func)) and not func.startswith("__")]
    method_list_connected = [func for func in dir(ConnectedApi) if callable(getattr(ConnectedApi, func)) and not func.startswith("__")]
    method_list_extended = [func for func in dir(ExtendedApi) if callable(getattr(ExtendedApi, func)) and not func.startswith("__")]
    method_list = method_list_apibox + method_list_connected + method_list_extended
    return jsonify({'methods': method_list})


@api.route('/get-templates/', methods=['GET'])
def getTemplates():
    data = getAllFileNames()
    return jsonify({'templates': data})


@api.route('/excecute-template/', methods=['GET'])
def excecuteTemplate():
    template_name = request.args.get('template', None)
    if template_name is None:
        return 'template name needed'
    else:
        name = template_name
    r = run(name)
    return jsonify(r)


@api.route('/create-template/', methods=['POST'])
def createTemplate():
    data = request.get_json(force=True)
    r = gen_json(data)
    return jsonify(r)


@api.route('/cards-info/', methods=['GET'])
def getCards():
    data = Apibox.getCardsInfo()
    return jsonify(data)


# for example
@api.route('/car/', methods=['GET'])
def getCar():
    carList = ['XC40', 'XC60']
    carModel = random.choice(carList)
    print(carModel)
    return jsonify({'carModel': carModel})


@api.route('/get-datetime/', methods=['GET'])
def getDateInfo():
    result = Apibox.getDateTime()
    return jsonify({'dateInfo': result})


@api.route('/get-weather/', methods=['GET'])
def getWeather():
    result = Apibox.getWeatherData()
    return jsonify(result)


# for example
@api.route('/get-v-model/', methods=['GET'])
def getVModel():
    result = ConnectedApi.getVehicleModel()
    return result


@api.route('/get-windows-status/', methods = ['GET'])
def getWinStatus():
    result = ConnectedApi.getWindowStatus()
    return jsonify(result)


@api.route('/get-warning/', methods = ['GET'])
def getWarnStatus():
    result = ConnectedApi.getWarnings()
    return jsonify(result)


@api.route('/get-tyre/', methods = ['GET'])
def getTyre():
    result = ConnectedApi.getTyreStatus()
    return jsonify(result)


@api.route('/get-v-stat/', methods = ['GET'])
def getStat():
    result = ConnectedApi.getVehicleStat()
    return jsonify(result)


@api.route('/get-odo/', methods = ['GET'])
def getOdo():
    result = ConnectedApi.getOdometer()
    return jsonify(result)


@api.route('/get-fuel-info/', methods = ['GET'])
def getFuelinfo():
    result = ConnectedApi.getFuel()
    return jsonify(result)


@api.route('/get-env-temp/', methods = ['GET'])
def getEnvir():
    result = ConnectedApi.getEnvironment()
    return jsonify(result)


@api.route('/get-eng-diag/', methods = ['GET'])
def getEngDiag():
    result = ConnectedApi.getEngineDiagnostics()
    return jsonify(result)


@api.route('/get-door-lock-status/', methods = ['GET'])
def getLockStatus():
    result = ConnectedApi.getDoorLock()
    return jsonify(result)


@api.route('/get-v-diag/', methods = ['GET'])
def getDiag():
    result = ConnectedApi.getDiagnostic()
    return jsonify(result)


@api.route('/get-brake-status/', methods = ['GET'])
def getBrake():
    result = ConnectedApi.getBrakeStatus()
    return jsonify(result)


@api.route('/post-climatization-start/', methods = ['POST'])
def postClimStart():
    status = ConnectedApi.postClimatizationStart()
    return status


@api.route('/post-climatization-stop', methods = ['POST'])
def postClimStop():
    status = ConnectedApi.postClimatizationStop()
    return status


@api.route('/post-engine-start', methods = ['POST'])
def postEngStart():
    status = ConnectedApi.postEngineStart()
    return status


@api.route('/post-engine-stop', methods = ['POST'])
def postEngStop():
    status = ConnectedApi.postEngineStop()
    return status


@api.route('/post-flash', methods = ['POST'])
def postFla():
    status = ConnectedApi.postFlash()
    return status


@api.route('/post-honkflash', methods = ['POST'])
def postHonFla():
    status = ConnectedApi.postHonkFlash()
    return status


@api.route('/post-honk', methods = ['POST'])
def postHo():
    status = ConnectedApi.postHonk()
    return status


@api.route('/post-lock', methods = ['POST'])
def postLo():
    status = ConnectedApi.postLock()
    return status


@api.route('/post-navigation', methods = ['POST'])
def postNavi():
    status = ConnectedApi.postNavigation()
    return status
