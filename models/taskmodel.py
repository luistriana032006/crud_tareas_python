### clase entidad de una tarea

class taskmodel:
    def __init__(self,id: int, name: str, description: str, complete: bool = False,):
        self._name = name
        self._description = description
        self._complete = complete
        self._id = id

    """ 
    atributos con valores por defecto SIEMPRE van al final 
    """

    ## getters y setters
    ## ---getters---

    @property   ## -- genera el getter 
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    

    @property
    def complete(self):
        return self._complete
    

    @property
    def id(self):
        return self._id


    ## ---setters--- 

    @name.setter
    def name(self,value:str):
        self._name = value

    @description.setter
    def description (self, value:str):
        self._description = value

    
    @complete.setter
    def complete(self,value:bool):
        self._complete = value

    
    ### equals 
    def __eq__(self, other):
        if not isinstance (other, taskmodel):
            return False
        return self._id == other._id

    ### hashcode

    def __hash__(self):
        return hash(self._id)
    

    ### to string str
    def __str__(self):
        return f"taskmodel(id= {self._id}, name = {self._name}, description = {self._description}, complete = {self._complete})"
    

    ### representacion para el debugger
    
    def __repr__(self):
        return self.__str__()
    
