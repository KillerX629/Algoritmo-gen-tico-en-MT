
class cinta():
    def __init__(self) -> None:
        self.posicion = 0
        self.lista = []
    
    def get(self) -> int:
        return self.lista[self.posicion]
    
    #desplazamiento del cabezal de la cinta a izquierda y derecha
    def SHR(self) -> None:
        self.posicion += 1
    def SHL(self) -> None:
        self.posicion -= 1

    #establecer un valor en la posicón actual de la cinta
    def set_valor(self, valor)-> float:
        self.lista[self.posicion] = valor

    def print_cinta(self):
        print(self.lista)
    

    

    



class maquinaDeTuring():
    def __init__(self):
        self.cinta = cinta
        self.cintaFitness = cinta
        self.cintaCruce = cinta
        self.estado = 0
        self.memoria = cinta
        self. probCruce = 0.5
        self.probMutacion = 0.1

    
    
    def escribirCinta(self,valor):
        self.cinta.lista[self.cinta.posicion] = valor

    def ejecutar(self):
        while self.estado != 'F':
            self.estadosDeTransicion()
            self.mostrarMaquina()


    def cambiarEstado(self,stateChange,stateChange2,stateChange3,stateChange4):
        #stateChange =(ValorAEscribir, Direccion, Estado, valorAEscribirEnMemoria)
        if stateChange != None:
            if (stateChange[3] != None):
                self.memoria = stateChange[3]
            if(stateChange[0] != None):
                self.cinta.set_valor(stateChange[0])
            self.estado = stateChange[2]
        if stateChange2 != None:
            self.estado = stateChange2[2]
            if(stateChange2[0] != None):
                self.cinta.set_valor(stateChange2[0])
    
    def mostrarMaquina(self):
        print("Estado: ",self.estado)
        print("Posición: ",self.posicion)
        print("Memoria: ",self.memoria)
        print("\n")
        print("Cinta: ",self.cinta)
        print("\n")


    def cruce(self,padre1,padre2):
        """tomando dos números de la cinta (uno en self.memoria y otro en la posición de la cinta)
        y cruzando ambos, se obtiene un hijo que será el valor promedio de los dos números"""
        if random.random() < self.probCruce:
            hijo = (padre1.memoria + padre2.memoria)/2
            return hijo
        else:
            return self.memoria
        
  
    #anatomia de estados de transición: [estado, dirección, valor, nuevo estado]
    #cinta ejemplo: 
    """ [0,20,35,10,.5,0] <-Almacena el Fitness de cada individuo
        [0,0,1,0,0,0] <-Almacena el estado de cada individuo
        [P,15,100,60,90,F]<-Almacena símbolos de la cinta y valores de los individuos

         """


    #estados de transición:[q0,0]=[0,R,q1]
    #explicación: si está en el estado q0, y lee un 0, deja el 0, se mueve a la derecha y cambia de estado a q1

    #los estados de esta máquina de turing le permitiran realizar operaciones genéticas

    def estadosDeTransicion(self):
        """el match es un switch de estados de transición, dentro de cada estado de transición hay que
        definir que pasa cuando se lee un valor"""
        match self.estado:#estado de la máquina de turing
            
            case 'OrdIzq':
                entero = isinstance(self.cinta.get(),float)
                if entero:

            

            case _:
                print("Error: estado no reconocido")









"""
case 0:
    esNumero = isinstance(self.cinta.get(),float)
    match esNumero:
        case True:
            #si lee un número, esa posición en la cinta tiene un individuo
            pass


        case False:
            #si lee una letra, esa posición en la cinta tiene un caracter especial
            pass

case 1:#usamos este estado y el estado 2 para hacer un bubble sort de la cinta
    esNumero = isinstance(self.cinta.get(),float)
    match esNumero:
        case True:
            if(self.leerCinta() > self.memoria):
                self.cambiarEstado((None,-1,2,self.leerCinta()))
            else:
                self.cambiarEstado((None,1,1,self.leerCinta()))
        case False:
            if(self.leerCinta() == 'F'):
                self.cambiarEstado((None,-1,3,None))

case 2:
    esNumero = isinstance(self.cinta.get(),float)
    match esNumero:
        case True:
            self.cambiarEstado((self.memoria,1,1,None))


case 3:#el caso 3 moverá la cinta a la izquierda hasta que encuentre un símbolo
    esNumero = isinstance(self.cinta.get(),float)
    match esNumero:
        case True:
            self.cambiarEstado((None,-1,3,None))
        
        case False:
            self.cambiarEstado((None,1,0,None))
        
case 'F': #Estado final
    pass

#para realizar el cruce entre individuos, se combinarán dos individuos al azar y se almacenará el resultado
#en el lado derecho de la cinta, después del caracter F
case 'C':
    self.cambiarEstado((self.cruce(self.cinta[0],self.cinta[1]),1,0,None))


"""



"""
Tape (cinta)
Cabezal (apuntador,simbolo a sobreescribir,izquierda-derecha-izquierda)
Registro de estados
Tabla de transiciones
La maquina de turing tiene las caracteristicas de un Automata finito
Q = Es un conjunto de estados
    Σ = Alfabeto conjunto de caracteres (codigo utf-8 ="\u03A3")
    Γ = Simbolos de la cinta
    s = Estado inicial sϵQ
    δ= Reglas nde transicion (Codigo utf-8 = "\u03B4")
    QxΣ->Q Reglas de transicion
    bϵΓ = es un simbolo denominado blanco, que se puede repetir infinitamente en toda la cinta
    F⊆Q Estado finales o de aceptacion

    Q = {s,q1}
    Σ = {a}
    Γ = {a,b}
    s = Estado inicial q0ϵQ
    δ= Reglas de transicion
    Reglas de transicion
    Q x Σ -> Q
    ((q0,a)->q1*)
    (estado, valor) -> nuevo estado, nuevo valor, dirección)
    (s,a)->q1,b,right
    (q1,b)->--Valido--
    "si estamos en el estado s leyendo la posición q1, donde hay
    escrito el símbolo 'a', entonces este símbolo debe ser reemplazado
    por el símbolo 'b', y pasar a leer la celda siguiente, a la derecha".
    F⊆Q = {q1}

    Estructura gafica es un grafo dirigido que se conecta en los vertices
    con:
        (lee el cabezal/
        símbolo que escribirá el cabezal,
        movimiento del cabezal.)
        (s,a)->q1,b,right
        ('a',b,right)

"""

def turing_M(estado=None,  # estados de la maquina de turing
             blanco=None,  # simbolo blanco de el alfabeto dela cinta
             reglas=[],  # reglas de transicion
             cinta=[],  # cinta
             final=None,  # estado valido y/o final
             pos=0):  # posicion siguiente de la maquina de turing
    nuevoEstado = estado
    if not cinta: cinta = [blanco]
    if pos < 0: pos += len(cinta)
    if pos >= len(cinta) or pos < 0:
        raise Error("Se inicializa mal la posicion")
    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    """Estado	Símbolo leído	Símbolo escrito	  Mov.	   Estado sig.
       p(s0)        1(v0)	           x(v1)	   R(dr)	 p(s1)
    """
    while True: #ver las reglas
        print(nuevoEstado, '\t', end=" ")
        for i, contenido in enumerate(cinta):
            if i == pos:
                print("[%s]" % (contenido,), end=" ")
            else:
                print(contenido, end=" ")
        print()
        if nuevoEstado == final: break
        if (nuevoEstado, cinta [pos]) not in reglas: break
        (v1, dr, s1) = reglas[(nuevoEstado, cinta[pos])]
        cinta [pos] = v1
        # movimiento del cabezal
        if dr == 'left':
            if pos > 0:
                pos -= 1
            else:
                cinta.insert(0, blanco)
        if dr == 'right':
            pos += 1
            if pos >= len(cinta): cinta.append(blanco)
        nuevoEstado = s1

print("Maquina de turing Test")
turing_M(
    estado='p',  # estados de la maquina de turing
    blanco='b',  # simbolo blanco de el alfabeto dela cinta
    cinta=list("1011"),  # cinta
    final='q',  # estado valido y/o final
    reglas=map(tuple,
               ["p 1 x right p".split(),
                "p 0 0 right p".split(),
                "p b b right q".split()]
               )# reglas de transicion
        )