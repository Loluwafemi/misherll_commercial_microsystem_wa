from subscriber import xlRequest, xlWhatkit, xlDone
# the ones the informs the subscribers with the given information
class Subject:
    
    def __init__(self):
        self._observers = []
        
    def notify(self):
        for observer in self._observers:
            if observer != None:
                observer.update(self)   # trigger the subscriber
            
    # subscribe the observer to the list
    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            
    # unsubscribe the observer from the list
    def unsubscribe(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    
# Interface for information sent to the observers
class Data(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.name = None
        self._data = 0
        
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value # dynamic [a dictionary]
        self.notify()
            
