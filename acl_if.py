acl = input("Ingrese el número de lista de acceso: ")

# Verificar si el número ingresado es una ACL o una SACL
if acl.isdigit() and int(acl) >= 1 and int(acl) <= 99 or int(acl) >= 1300 and int(acl) <= 1999:
    print(f"{acl} es una lista de acceso estándar (SACL).")
elif acl.isdigit() and int(acl) >= 100 and int(acl) <= 199 or int(acl) >= 2000 and int(acl) <= 2699:
    print(f"{acl} es una lista de acceso extendida (ACL).")
else:   
    print("El numero ingresado no es valido")
