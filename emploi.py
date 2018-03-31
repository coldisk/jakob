import sqlite3

def addPostul(curs):
    dateC = input("Date candidature: ")
    nomEntreprise = input('Entreprise: ')
    contactRH = input("Contact RH: ")
    if contactRH == '':
        contactRH='NULL'
    comms = input("Commentaires : ")
    if comms == '':
        comms = 'NULL'
    values=(dateC,  nomEntreprise,  contactRH, comms, )
    curs.execute('INSERT INTO candidatures VALUES (?,?,?,?,NULL)',  values )
    curs.execute('SELECT * FROM candidatures')
    print(curs.fetchall())

if __name__=="__main__":
    conn = sqlite3.connect('candidature.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS candidatures(dateCandidature DATETIME NOT NULL, nomEntreprise VARCHAR(30) NOT NULL,  contactRH VARCHAR(50), commentaires TEXT, dateEntretien DATETIME)""")
    conn.commit()
    addPostul(cursor)
    conn.commit()
#def remPostul(index): #deleting the line
#    #on enlève la ligne index
#
#def rappel(ligne):
#	#on prend la date d'aujourd'hui on regarde si elle correspond à la date de relance, si match, envoi sms
#
#def modifPostul(index, column, value):
