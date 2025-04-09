class StatusManager:
    def __init__(self):
        self.observers = []
        self.status = "Pronto para iniciar"
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def update_status(self, new_status):
        self.status = new_status
        for observer in self.observers:
            observer(self.status)