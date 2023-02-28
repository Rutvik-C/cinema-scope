class FirebaseUtils:
    def __init__(self, db):
        self.db = db

    def getAllMovies(self):
        docs = self.db.collection("Movies").stream()
        
        data = []
        for doc in docs:
            tmp = doc.to_dict()
            tmp["id"] = doc.id
            data.append(tmp)
        
        return data
    
    def getMovie(self, id):
        doc = self.db.collection("Movies").document(id).get()

        if doc.exists:
            tmp = doc.to_dict()
            tmp["id"] = doc.id
            
            return tmp
        
        return None
    
    def addNewMovie(self, data):
        self.db.collection("Movies").add(data)
        
    def updateMovie(self, id, data):
        self.db.collection("Movies").document(id).update(data)
        
    def deleteMovie(self, id):
        self.db.collection("Movies").document(id).delete()
