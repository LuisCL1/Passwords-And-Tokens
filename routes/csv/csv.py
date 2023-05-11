from flask import Blueprint,Response
from models import Usuario
appcsv= Blueprint("appcsv",__name__,template_folder="templates")


def generateCsv():
    usuarios = Usuario.query.all()
    csvString = "ID,EMAIL,REGISTRADO,ADMIN,PASSWORD\n"
    for usuario in usuarios :
        csvString+=f'{usuario.id},{usuario.email},{usuario.registrado},{usuario.admin},{usuario.password}\n'

    headers ={
        'Content-Disposition':'attachment;filename=usuarios.csv',
        'Content-Type':'text/csv'
    }

    print(csvString)
    return Response(csvString,headers=headers)

@appcsv.route('/indexCsv')
def indexCsv():
    return generateCsv()