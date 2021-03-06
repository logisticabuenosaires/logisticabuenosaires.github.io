# coding: utf8
# try something like
def index(): return dict(message="hello from usuarios.py")

def clientes():
#    if auth.user_id:
#        if auth.has_membership (group_id=3):
#            redirect(URL(r=request, c="default", f="prohibido"))
#    else:
#        redirect(URL(r=request, c="default", f="prohibido"))
    
    # SELECCIONA EL LAYOUT SEGUN EL USUARIO QUE SEA
    esqueleto='layout.html'
    if auth.has_membership (group_id=4):
        esqueleto='layout_admin.html'
    elif auth.has_membership (group_id=5):
        esqueleto='layout_despachador.html'
    elif auth.has_membership (group_id=1):
        esqueleto='layout_chofer.html'    
    
    lista_clientes = db(
    (db.auth_user.id>0) &
    (db.auth_membership.group_id==3) & 
    (db.auth_membership.user_id==db.auth_user.id)
    ).select(
    db.auth_user.id,
    db.auth_user.first_name,
    db.auth_user.last_name,
    db.auth_user.dni,
    db.auth_user.localidad,
    db.auth_user.calle,
    db.auth_user.nro_calle,
    orderby=db.auth_user.id)
    
    return {'lista_clientes' : lista_clientes,'esqueleto' : esqueleto}
############################################################################

def Operador():
    if auth.user_id:
        if auth.has_membership (group_id=5):
            redirect(URL(r=request, c="default", f="prohibido"))
    else:
        redirect(URL(r=request, c="default", f="prohibido"))
    
    # SELECCIONA EL LAYOUT SEGUN EL USUARIO QUE SEA
    esqueleto='layout.html'
    if auth.has_membership (group_id=5):
        esqueleto='layout_gestionar.html'
    elif auth.has_membership (group_id=5):
        esqueleto='layout_admin.html'   
    lista_despachadores= db(
    (db.auth_user.id>0) &
    (db.auth_membership.group_id==5) & 
    (db.auth_membership.user_id==db.auth_user.id)
    ).select(
    db.auth_user.id,
    db.auth_user.first_name,
    db.auth_user.last_name,
    db.auth_user.dni,
    db.auth_user.localidad,
    db.auth_user.calle,
    db.auth_user.nro_calle,
    orderby=db.auth_user.id)

    return {'lista_despachadores' : lista_despachadores,'esqueleto' : esqueleto}

def administrador():
    if auth.user_id:
        if auth.has_membership (group_id=4):
            redirect(URL(r=request, c="default", f="prohibido"))
    else:
        redirect(URL(r=request, c="default", f="prohibido"))
    
   #  SELECCIONA EL LAYOUT SEGUN EL USUARIO QUE SEA#
    esqueleto='layout.html'
    if auth.has_membership (group_id=4):
        esqueleto='layout_administrador.html'
    elif auth.has_membership (group_id=5):
        esqueleto='layout_despachador.html'
    
    lista_administradores = db(
    (db.auth_user.id>0) &
    (db.auth_membership.group_id==2) & 
    (db.auth_membership.user_id==db.auth_user.id)
    ).select(
    db.auth_user.id,
    db.auth_user.first_name,
    db.auth_user.last_name,
    db.auth_user.dni,
    db.auth_user.localidad,
    db.auth_user.calle,
    db.auth_user.nro_calle,
    orderby=db.auth_user.id)
    
    return {'lista_administradores' : lista_administradores,'esqueleto' : esqueleto}
