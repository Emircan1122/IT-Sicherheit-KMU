from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class SchnellCheckForm(FlaskForm): 
     #Frage 1
     betrieb = RadioField('Wie ist Ihr Gastronomiebetrieb strukturiert?',
                         choices=[('restaurant', 'Restaurant'),
                                  ('cafe', 'Café'),
                                  ('bar', 'Bar'),
                                  ('imbiss', 'Imbiss'),
                                  ('catering', 'Catering'),
                                  ('hotel', 'Hotel mit Gastronomie'),
                                  ('sonstiges', 'Sonstiges')],
                         validators=[DataRequired()])
                         
     #Frage 2
     tse = RadioField('Erfüllt Ihr Kassensystem die Anforderungen einer zertifizierten technischen Sicherheitseinrichtung (TSE)?',
                     choices=[('ja', 'Ja'), ('nein', 'Nein'), ('unsicher', 'Unsicher')],
                     validators=[DataRequired()])
     
     #Frage 3
     beleg = RadioField('Geben Sie für jede Transaktion einen Beleg aus?',
                       choices=[('ja', 'Ja'), ('teilweise', 'Teilweise'), ('nein', 'Nein')],
                       validators=[DataRequired()])
     #Frage 4
     pruefung = RadioField('Wurde Ihr Kassensystem innerhalb der letzten 12 Monate geprüft oder zertifiziert?',
                          choices=[('ja', 'Ja'), ('nein', 'Nein')],
                          validators=[DataRequired()])
     #Frage 5
     trennung = RadioField('Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                          choices=[('ja', 'Ja'), ('nein', 'Nein')],
                          validators=[DataRequired()])
     #Frage 6
     einnahmen = RadioField('Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?',
                           choices=[('ja', 'Ja'), ('nein', 'Nein')],
                           validators=[DataRequired()])
     #Frage 7
     steuererklärungen = RadioField('Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                                   choices=[('ja', 'Ja'), ('nein', 'Nein')],
                                   validators=[DataRequired()])
     #Frage 8
     nachforderungen = RadioField('Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                                 choices=[('ja', 'Ja'), ('nein', 'Nein')],
                                 validators=[DataRequired()])
     #Frage 9
     trinkgelder = RadioField('Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?',
                             choices=[('ja', 'Ja'), ('nein', 'Nein')],
                             validators=[DataRequired()])
     #Frage 10
     schulung = RadioField('Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?',
                          choices=[('ja', 'Ja'), ('nein', 'Nein')],
                          validators=[DataRequired()])
     
     #Einreichen
     submit = SubmitField('Fertig')
     
class quizwebanwendungen(FlaskForm): 
     #Frage 1
     web1 = RadioField('Was beschreibt eine SQL-Injection-Attacke am besten?',
                         choices=[('web1a', 'Überlastung des Webservers durch massenhafte Anfragen'),
                                  ('web1b', 'Einschleusen und Ausführen schädlicher SQL-Befehle in ein Web-Formular, um Datenbankinhalte auszulesen oder zu manipulieren.'),
                                  ('web1c', 'Abfangen von Netzwerkpaketen beim Benutzer.'),
                                  ('web1d', 'Täuschen des DNS-Systems.'),],
                         validators=[DataRequired()])
                         
     #Frage 2
     web2 = RadioField('Was kann ein Angreifer mit einer erfolgreichen SQL-Injection meist erreichen?',
                     choices=[('web2a', 'Er kann vertrauliche Daten aus der Datenbank auslesen oder verändern'), ('web2b', 'Er kann den Webserver durch massenhaftes Anfragen lahmlegen.'), ('web2c', 'Er verschickt Werbe-E-Mails an alle Kunden.'), ('web2d', 'Er ersetzt die Webseite durch eine neue.')],
                     validators=[DataRequired()])
     
     #Frage 3
     web3 = RadioField('Was ist Cross-Site-Scripting (XSS)?',
                       choices=[('web3a', 'Das Aufspüren von Viren in Skriptdateien.'), ('web3b', 'Ein Angriff, bei dem Angreifer bösartigen Skriptcode in eine ansonsten harmlose Webseite einschleusen, der im Browser anderer Nutzer ausgeführt wird.'), ('web3c', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.'), ('web3d', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.')],
                       validators=[DataRequired()])
     #Frage 4
     web4 = RadioField('frage?',
                          choices=[('web4a', 'Ja'), ('web4b', 'Nein'), ('web4c', 'Nein'), ('web4d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 5
     web5 = RadioField('Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                          choices=[('web5a', 'Ja'), ('web5b', 'Nein'), ('web5c', 'Nein'), ('web5d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 6
     web6 = RadioField('Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?',
                           choices=[('web6a', 'Ja'), ('web6b', 'Nein'), ('web6c', 'Nein'), ('web6d', 'Nein')],
                           validators=[DataRequired()])
     #Frage 7
     web7 = RadioField('Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                                   choices=[('web7a', 'Ja'), ('web7b', 'Nein'), ('web7c', 'Nein'), ('web7d', 'Nein')],
                                   validators=[DataRequired()])
     #Frage 8
     web8 = RadioField('Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                                 choices=[('web8a', 'Ja'), ('web8b', 'Nein'), ('web8c', 'Nein'), ('web8d', 'Nein')],
                                 validators=[DataRequired()])
     #Frage 9
     web9 = RadioField('Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?',
                             choices=[('web9a', 'Ja'), ('web9b', 'Nein'), ('web9c', 'Nein'), ('web9d', 'Nein')],
                             validators=[DataRequired()])
     #Frage 10
     web10 = RadioField('Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?',
                          choices=[('web10a', 'Ja'), ('web10b', 'Nein'), ('web10c', 'Nein'), ('web10d', 'Nein')],
                          validators=[DataRequired()])
     
     #Einreichen
     submit = SubmitField('Fertig')

class quiznetzwerk(FlaskForm): 
     #Frage 1
     net1 = RadioField('Was beschreibt eine SQL-Injection-Attacke am besten?',
                         choices=[('net1a', 'Überlastung des Webservers durch massenhafte Anfragen'),
                                  ('net1b', 'Einschleusen und Ausführen schädlicher SQL-Befehle in ein Web-Formular, um Datenbankinhalte auszulesen oder zu manipulieren.'),
                                  ('net1c', 'Abfangen von Netzwerkpaketen beim Benutzer.'),
                                  ('net1d', 'Täuschen des DNS-Systems.'),],
                         validators=[DataRequired()])
                         
     #Frage 2
     net2 = RadioField('Was kann ein Angreifer mit einer erfolgreichen SQL-Injection meist erreichen?',
                     choices=[('net2a', 'Er kann vertrauliche Daten aus der Datenbank auslesen oder verändern'), ('net2b', 'Er kann den Webserver durch massenhaftes Anfragen lahmlegen.'), ('net2c', 'Er verschickt Werbe-E-Mails an alle Kunden.'), ('net2d', 'Er ersetzt die Webseite durch eine neue.')],
                     validators=[DataRequired()])
     
     #Frage 3
     net3 = RadioField('Was ist Cross-Site-Scripting (XSS)?',
                       choices=[('net3a', 'Das Aufspüren von Viren in Skriptdateien.'), ('net3b', 'Ein Angriff, bei dem Angreifer bösartigen Skriptcode in eine ansonsten harmlose Webseite einschleusen, der im Browser anderer Nutzer ausgeführt wird.'), ('net3c', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.'), ('net3d', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.')],
                       validators=[DataRequired()])
     #Frage 4
     net4 = RadioField('frage?',
                          choices=[('net4a', 'Ja'), ('net4b', 'Nein'), ('net4c', 'Nein'), ('net4d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 5
     net5 = RadioField('Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                          choices=[('net5a', 'Ja'), ('net5b', 'Nein'), ('net5c', 'Nein'), ('net5d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 6
     net6 = RadioField('Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?',
                           choices=[('net6a', 'Ja'), ('net6b', 'Nein'), ('net6c', 'Nein'), ('net6d', 'Nein')],
                           validators=[DataRequired()])
     #Frage 7
     net7 = RadioField('Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                                   choices=[('net7a', 'Ja'), ('net7b', 'Nein'), ('net7c', 'Nein'), ('net7d', 'Nein')],
                                   validators=[DataRequired()])
     #Frage 8
     net8 = RadioField('Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                                 choices=[('net8a', 'Ja'), ('net8b', 'Nein'), ('net8c', 'Nein'), ('net8d', 'Nein')],
                                 validators=[DataRequired()])
     #Frage 9
     net9 = RadioField('Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?',
                             choices=[('net9a', 'Ja'), ('net9b', 'Nein'), ('net9c', 'Nein'), ('net9d', 'Nein')],
                             validators=[DataRequired()])
     #Frage 10
     net10 = RadioField('Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?',
                          choices=[('net10a', 'Ja'), ('net10b', 'Nein'), ('net10c', 'Nein'), ('net10d', 'Nein')],
                          validators=[DataRequired()])
     #Einreichen
     submit = SubmitField('Fertig')

class quizsocial(FlaskForm): 
     #Frage 1
     soc1 = RadioField('Was beschreibt eine SQL-Injection-Attacke am besten?',
                         choices=[('soc1a', 'Überlastung des Webservers durch massenhafte Anfragen'),
                                  ('soc1b', 'Einschleusen und Ausführen schädlicher SQL-Befehle in ein Web-Formular, um Datenbankinhalte auszulesen oder zu manipulieren.'),
                                  ('soc1c', 'Abfangen von Netzwerkpaketen beim Benutzer.'),
                                  ('soc1d', 'Täuschen des DNS-Systems.'),],
                         validators=[DataRequired()])
                         
     #Frage 2
     soc2 = RadioField('Was kann ein Angreifer mit einer erfolgreichen SQL-Injection meist erreichen?',
                     choices=[('soc2a', 'Er kann vertrauliche Daten aus der Datenbank auslesen oder verändern'), ('soc2b', 'Er kann den Webserver durch massenhaftes Anfragen lahmlegen.'), ('soc2c', 'Er verschickt Werbe-E-Mails an alle Kunden.'), ('soc2d', 'Er ersetzt die Webseite durch eine neue.')],
                     validators=[DataRequired()])
     
     #Frage 3
     soc3 = RadioField('Was ist Cross-Site-Scripting (XSS)?',
                       choices=[('soc3a', 'Das Aufspüren von Viren in Skriptdateien.'), ('soc3b', 'Ein Angriff, bei dem Angreifer bösartigen Skriptcode in eine ansonsten harmlose Webseite einschleusen, der im Browser anderer Nutzer ausgeführt wird.'), ('soc3c', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.'), ('soc3d', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.')],
                       validators=[DataRequired()])
     #Frage 4
     soc4 = RadioField('frage?',
                          choices=[('soc4a', 'Ja'), ('soc4b', 'Nein'), ('soc4c', 'Nein'), ('soc4d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 5
     soc5 = RadioField('Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                          choices=[('soc5a', 'Ja'), ('soc5b', 'Nein'), ('soc5c', 'Nein'), ('soc5d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 6
     soc6 = RadioField('Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?',
                           choices=[('soc6a', 'Ja'), ('soc6b', 'Nein'), ('soc6c', 'Nein'), ('soc6d', 'Nein')],
                           validators=[DataRequired()])
     #Frage 7
     soc7 = RadioField('Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                                   choices=[('soc7a', 'Ja'), ('soc7b', 'Nein'), ('soc7c', 'Nein'), ('soc7d', 'Nein')],
                                   validators=[DataRequired()])
     #Frage 8
     soc8 = RadioField('Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                                 choices=[('soc8a', 'Ja'), ('soc8b', 'Nein'), ('soc8c', 'Nein'), ('soc8d', 'Nein')],
                                 validators=[DataRequired()])
     #Frage 9
     soc9 = RadioField('Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?',
                             choices=[('soc9a', 'Ja'), ('soc9b', 'Nein'), ('soc9c', 'Nein'), ('soc9d', 'Nein')],
                             validators=[DataRequired()])
     #Frage 10
     soc10 = RadioField('Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?',
                          choices=[('soc10a', 'Ja'), ('soc10b', 'Nein'), ('soc10c', 'Nein'), ('soc10d', 'Nein')],
                          validators=[DataRequired()])
     #Einreichen
     submit = SubmitField('Fertig')

class quizmaleware(FlaskForm): 
     #Frage 1
     mal1 = RadioField('Was beschreibt eine SQL-Injection-Attacke am besten?',
                         choices=[('soc1a', 'Überlastung des Webservers durch massenhafte Anfragen'),
                                  ('soc1b', 'Einschleusen und Ausführen schädlicher SQL-Befehle in ein Web-Formular, um Datenbankinhalte auszulesen oder zu manipulieren.'),
                                  ('soc1c', 'Abfangen von Netzwerkpaketen beim Benutzer.'),
                                  ('soc1d', 'Täuschen des DNS-Systems.'),],
                         validators=[DataRequired()])
                         
     #Frage 2
     mal2 = RadioField('Was kann ein Angreifer mit einer erfolgreichen SQL-Injection meist erreichen?',
                     choices=[('mal2a', 'Er kann vertrauliche Daten aus der Datenbank auslesen oder verändern'), ('mal2b', 'Er kann den Webserver durch massenhaftes Anfragen lahmlegen.'), ('mal2c', 'Er verschickt Werbe-E-Mails an alle Kunden.'), ('mal2d', 'Er ersetzt die Webseite durch eine neue.')],
                     validators=[DataRequired()])
     
     #Frage 3
     mal3 = RadioField('Was ist Cross-Site-Scripting (XSS)?',
                       choices=[('mal3a', 'Das Aufspüren von Viren in Skriptdateien.'), ('mal3b', 'Ein Angriff, bei dem Angreifer bösartigen Skriptcode in eine ansonsten harmlose Webseite einschleusen, der im Browser anderer Nutzer ausgeführt wird.'), ('mal3c', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.'), ('mal3d', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.')],
                       validators=[DataRequired()])
     #Frage 4
     mal4 = RadioField('frage?',
                          choices=[('mal4a', 'Ja'), ('mal4b', 'Nein'), ('mal4c', 'Nein'), ('mal4d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 5
     mal5 = RadioField('Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                          choices=[('mal5a', 'Ja'), ('mal5b', 'Nein'), ('mal5c', 'Nein'), ('mal5d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 6
     mal6 = RadioField('Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?',
                           choices=[('mal6a', 'Ja'), ('mal6b', 'Nein'), ('mal6c', 'Nein'), ('mal6d', 'Nein')],
                           validators=[DataRequired()])
     #Frage 7
     mal7 = RadioField('Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                                   choices=[('mal7a', 'Ja'), ('mal7b', 'Nein'), ('mal7c', 'Nein'), ('mal7d', 'Nein')],
                                   validators=[DataRequired()])
     #Frage 8
     mal8 = RadioField('Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                                 choices=[('mal8a', 'Ja'), ('mal8b', 'Nein'), ('mal8c', 'Nein'), ('mal8d', 'Nein')],
                                 validators=[DataRequired()])
     #Frage 9
     mal9 = RadioField('Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?',
                             choices=[('mal9a', 'Ja'), ('mal9b', 'Nein'), ('mal9c', 'Nein'), ('mal9d', 'Nein')],
                             validators=[DataRequired()])
     #Frage 10
     mal10 = RadioField('Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?',
                          choices=[('mal10a', 'Ja'), ('mal10b', 'Nein'), ('mal10c', 'Nein'), ('mal10d', 'Nein')],
                          validators=[DataRequired()])
     
     #Einreichen
     submit = SubmitField('Fertig')

class quizBekoid(FlaskForm): 
     #Frage 1
     bekoid1 = RadioField('Was beschreibt eine SQL-Injection-Attacke am besten?',
                         choices=[('bekoid1a', 'Überlastung des Webservers durch massenhafte Anfragen'),
                                  ('bekoid1b', 'Einschleusen und Ausführen schädlicher SQL-Befehle in ein Web-Formular, um Datenbankinhalte auszulesen oder zu manipulieren.'),
                                  ('bekoid1c', 'Abfangen von Netzwerkpaketen beim Benutzer.'),
                                  ('bekoid1d', 'Täuschen des DNS-Systems.'),],
                         validators=[DataRequired()])
                         
     #Frage 2
     bekoid2 = RadioField('Was kann ein Angreifer mit einer erfolgreichen SQL-Injection meist erreichen?',
                     choices=[('bekoid2a', 'Er kann vertrauliche Daten aus der Datenbank auslesen oder verändern'), ('bekoid2b', 'Er kann den Webserver durch massenhaftes Anfragen lahmlegen.'), ('bekoid2c', 'Er verschickt Werbe-E-Mails an alle Kunden.'), ('bekoid2d', 'Er ersetzt die Webseite durch eine neue.')],
                     validators=[DataRequired()])
     
     #Frage 3
     bekoid3 = RadioField('Was ist Cross-Site-Scripting (XSS)?',
                       choices=[('bekoid3a', 'Das Aufspüren von Viren in Skriptdateien.'), ('bekoid3b', 'Ein Angriff, bei dem Angreifer bösartigen Skriptcode in eine ansonsten harmlose Webseite einschleusen, der im Browser anderer Nutzer ausgeführt wird.'), ('bekoid3c', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.'), ('bekoid3d', 'Eine Technik, um den Quellcode einer Webseite zu verschlüsseln.')],
                       validators=[DataRequired()])
     #Frage 4
     bekoid4 = RadioField('frage?',
                          choices=[('bekoid4a', 'Ja'), ('bekoid4b', 'Nein'), ('bekoid4c', 'Nein'), ('bekoid4d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 5
     bekoid5 = RadioField('Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                          choices=[('bekoid5a', 'Ja'), ('bekoid5b', 'Nein'), ('bekoid5c', 'Nein'), ('bekoid5d', 'Nein')],
                          validators=[DataRequired()])
     #Frage 6
     bekoid6 = RadioField('Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?',
                           choices=[('bekoid6a', 'Ja'), ('bekoid6b', 'Nein'), ('bekoid6c', 'Nein'), ('bekoid6d', 'Nein')],
                           validators=[DataRequired()])
     #Frage 7
     bekoid7 = RadioField('Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                                   choices=[('bekoid7a', 'Ja'), ('bekoid7b', 'Nein'), ('bekoid7c', 'Nein'), ('bekoid7d', 'Nein')],
                                   validators=[DataRequired()])
     #Frage 8
     bekoid8 = RadioField('Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                                 choices=[('bekoid8a', 'Ja'), ('bekoid8b', 'Nein'), ('bekoid8c', 'Nein'), ('bekoid8d', 'Nein')],
                                 validators=[DataRequired()])
     #Frage 9
     bekoid9 = RadioField('Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?',
                             choices=[('bekoid9a', 'Ja'), ('bekoid9b', 'Nein'), ('bekoid9c', 'Nein'), ('bekoid9d', 'Nein')],
                             validators=[DataRequired()])
     #Frage 10
     bekoid10 = RadioField('Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?',
                          choices=[('bekoid10a', 'Ja'), ('bekoid10b', 'Nein'), ('bekoid10c', 'Nein'), ('bekoid10d', 'Nein')],
                          validators=[DataRequired()])
     
     #Einreichen
     submit = SubmitField('Fertig')
     