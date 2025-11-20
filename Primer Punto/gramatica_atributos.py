def generar_gramatica_sql():
    """
    Genera una representación en Python de una gramática de atributos
    para un lenguaje estilo SQL CRUD (SELECT, INSERT, UPDATE, DELETE).
    """

    G = {}

    def regla(atrs):
        """ Helper para formatear reglas semánticas """
        return {"semantic": atrs}

    # Gramática y atributos

    G["S"] = [
        {
            "prod": ["Sentencia"],
            **regla("S.cod = Sentencia.cod")
        }
    ]

    G["Sentencia"] = [
        {
            "prod": ["Select"],
            **regla("Sentencia.cod = Select.cod")
        },
        {
            "prod": ["Insert"],
            **regla("Sentencia.cod = Insert.cod")
        },
        {
            "prod": ["Update"],
            **regla("Sentencia.cod = Update.cod")
        },
        {
            "prod": ["Delete"],
            **regla("Sentencia.cod = Delete.cod")
        },
    ]

    #  SELECT 

    G["Select"] = [
        {
            "prod": ["SELECT", "Campos", "FROM", "ID", "Condicion"],
            **regla(
                'Select.cod = "SELECT " + Campos.cod + '
                '" FROM " + ID.lex + Condicion.cod'
            )
        }
    ]

    G["Campos"] = [
        {
            "prod": ["CampoLista"],
            **regla("Campos.cod = CampoLista.cod")
        }
    ]

    G["CampoLista"] = [
        {
            "prod": ["ID", "CampoListaP"],
            **regla('CampoLista.cod = ID.lex + CampoListaP.cod')
        }
    ]

    G["CampoListaP"] = [
        {
            "prod": [",", "ID", "CampoListaP"],
            **regla('CampoListaP.cod = "," + ID.lex + CampoListaP.cod')
        },
        {
            "prod": ["ε"],
            **regla('CampoListaP.cod = ""')
        }
    ]

    G["Condicion"] = [
        {
            "prod": ["WHERE", "Expr"],
            **regla('Condicion.cod = " WHERE " + Expr.cod')
        },
        {
            "prod": ["ε"],
            **regla('Condicion.cod = ""')
        }
    ]

    #  INSERT 

    G["Insert"] = [
        {
            "prod": ["INSERT", "INTO", "ID", "(", "Campos", ")", "VALUES", "(", "Valores", ")"],
            **regla(
                'Insert.cod = "INSERT INTO " + ID.lex + "(" + Campos.cod + ") VALUES (" + Valores.cod + ")"'
            )
        }
    ]

    G["Valores"] = [
        {
            "prod": ["ValorLista"],
            **regla("Valores.cod = ValorLista.cod")
        }
    ]

    G["ValorLista"] = [
        {
            "prod": ["VALOR", "ValorListaP"],
            **regla("ValorLista.cod = VALOR.lex + ValorListaP.cod")
        }
    ]

    G["ValorListaP"] = [
        {
            "prod": [",", "VALOR", "ValorListaP"],
            **regla('ValorListaP.cod = "," + VALOR.lex + ValorListaP.cod')
        },
        {
            "prod": ["ε"],
            **regla('ValorListaP.cod = ""')
        }
    ]

    # UPDATE 

    G["Update"] = [
        {
            "prod": ["UPDATE", "ID", "SET", "Asignaciones", "Condicion"],
            **regla(
                'Update.cod = "UPDATE " + ID.lex + " SET " + Asignaciones.cod + Condicion.cod'
            )
        }
    ]

    G["Asignaciones"] = [
        {
            "prod": ["Asig", "AsignacionesP"],
            **regla("Asignaciones.cod = Asig.cod + AsignacionesP.cod")
        }
    ]

    G["AsignacionesP"] = [
        {
            "prod": [",", "Asig", "AsignacionesP"],
            **regla('AsignacionesP.cod = "," + Asig.cod + AsignacionesP.cod')
        },
        {
            "prod": ["ε"],
            **regla('AsignacionesP.cod = ""')
        }
    ]

    G["Asig"] = [
        {
            "prod": ["ID", "=", "VALOR"],
            **regla('Asig.cod = ID.lex + "=" + VALOR.lex')
        }
    ]

    #  DELETE 

    G["Delete"] = [
        {
            "prod": ["DELETE", "FROM", "ID", "Condicion"],
            **regla('Delete.cod = "DELETE FROM " + ID.lex + Condicion.cod')
        }
    ]

    return G


# EJEMPLO DE USO

if __name__ == "__main__":
    gramatica = generar_gramatica_sql()
    for nt, prods in gramatica.items():
        print(f"\n{nt}:")
        for p in prods:
            print("  -", p)
