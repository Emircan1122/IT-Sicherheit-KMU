from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class SchnellCheckForm(FlaskForm): 
     #Frage 1
     # --- IT-Sicherheitsfragen ---

    # Backup-Frage
     backup = RadioField('Werden Ihre Unternehmensdaten regelmäßig gesichert und offline vorgehalten?',
                         choices=[('ja', 'Ja'), ('nein', 'Nein'), ('teilweise', 'Teilweise')],
                         validators=[DataRequired()])

     # IT-Schulung
     it_schulung = RadioField('Finden in Ihrem Unternehmen regelmäßige IT-Sicherheits-Schulungen für Mitarbeitende statt?',
                              choices=[('ja', 'Ja'), ('nein', 'Nein')],
                              validators=[DataRequired()])

     # Passwort/MFA
     passwort_mfa = RadioField('Setzen Sie auf starke Passwörter und nutzen Sie Mehrfaktor-Authentifizierung für wichtige Accounts?',
                                   choices=[('ja', 'Ja'), ('nein', 'Nein')],
                                   validators=[DataRequired()])

     # Firewall/Remote
     firewall = RadioField('Haben Sie eine Firewall im Einsatz und sind externe Zugänge (z.B. Remote Desktop) abgesichert?',
                              choices=[('ja', 'Ja'), ('nein', 'Nein')],
                              validators=[DataRequired()])

     # Updates/Patches
     updates = RadioField('Wie zeitnah installieren Sie Software-Updates/Sicherheits-Patches?',
                              choices=[('zeitnah', 'Zeitnah (innerhalb weniger Tage)'), 
                                   ('verspaetet', 'Mit Verzögerung'), 
                                   ('selten', 'Selten')],
                              validators=[DataRequired()])

     # Notfallplan
     notfallplan = RadioField('Existiert ein IT-Notfallplan (Incident Response) und wissen Mitarbeiter, was im Ernstfall zu tun ist?',
                              choices=[('ja', 'Ja'), ('nein', 'Nein')],
                              validators=[DataRequired()])

     # DDoS-Schutz (optional)
     ddos = RadioField('Hosten Sie öffentliche Web-Dienste, und ist ggf. DDoS-Schutz vorhanden?',
                         choices=[('ja', 'Ja'), ('nein', 'Nein'), ('nicht_zutreffend', 'Nicht zutreffend')],
                         validators=[DataRequired()])

     # Cyber-Versicherung
     cyberversicherung = RadioField('Besitzen Sie eine Cyber-Versicherung, die Restschäden abdeckt?',
                                        choices=[('ja', 'Ja'), ('nein', 'Nein')],
                                        validators=[DataRequired()])

     # Zugriffsrechte
     zugriffsrechte = RadioField('Sind Zugriffsrechte in Ihrem Netzwerk nach dem Need-to-know-Prinzip eingeschränkt?',
                                   choices=[('ja', 'Ja'), ('nein', 'Nein')],
                                   validators=[DataRequired()])

     # Professionelle Cloud-Dienste
     cloud_dienste = RadioField('Nutzen Sie professionelle Cloud-/Hosting-Dienste mit Sicherheitszertifizierungen?',
                                   choices=[('ja', 'Ja'), ('nein', 'Nein')],
                                   validators=[DataRequired()])

     #Einreichen
     submit = SubmitField('Fertig')
     
class quizwebanwendungen(FlaskForm): 
     #Frage 1
     web1 = RadioField('Was beschreibt eine klassische SQL-Injection (SQLi)?',
                         choices=[('Die Umgehung von Login-Feldern durch JavaScript', 'Die Umgehung von Login-Feldern durch JavaScript'),
                                  ('Das Einschleusen von manipuliertem SQL-Code über Benutzereingaben', 'Das Einschleusen von manipuliertem SQL-Code über Benutzereingaben'),
                                  ('Die Ausnutzung von DNS-Anfragen zur Datenexfiltration', 'Die Ausnutzung von DNS-Anfragen zur Datenexfiltration')],
                         validators=[DataRequired()])
             
     #Frage 2
     web2 = RadioField('Welche der folgenden Angriffsmethoden zählt NICHT zu den typischen SQL-Injection-Arten?',
                     choices=[('Authentication Bypass', 'Authentication Bypass'), ('Cross-Site Scripting (XSS)', 'Cross-Site Scripting (XSS)'), ('Blind SQLi', 'Blind SQLi')],
                     validators=[DataRequired()])
     
     #Frage 3
     web3 = RadioField('Warum sind kleine und mittlere Unternehmen (KMU) besonders gefährdet durch SQLi-Angriffe?',
                       choices=[('Sie setzen verstärkt auf künstliche Intelligenz', 'Sie setzen verstärkt auf künstliche Intelligenz'), ('Ihre Systeme sind oft veraltet oder schlecht abgesichert', 'Ihre Systeme sind oft veraltet oder schlecht abgesichert'), ('Sie entwickeln keine eigenen Webanwendungen', 'Sie entwickeln keine eigenen Webanwendungen')],
                       validators=[DataRequired()])
     #Frage 4
     web4 = RadioField('Was passiert bei einem Cross-Site Scripting (XSS)-Angriff?',
                          choices=[('Schadcode wird direkt auf dem Server des Angreifers ausgeführt', 'Schadcode wird direkt auf dem Server des Angreifers ausgeführt'), ('Der Angreifer schleust Skripte ein, die im Browser des Nutzers ausgeführt werden', 'Der Angreifer schleust Skripte ein, die im Browser des Nutzers ausgeführt werden'), ('Die Datenbank wird durch schadhafte SQL-Befehle manipuliert', 'Die Datenbank wird durch schadhafte SQL-Befehle manipuliert')],
                          validators=[DataRequired()])
     #Frage 5
     web5 = RadioField('Was ist das Ziel eines Directory Traversal Angriffs?',
                          choices=[('Schadsoftware im Arbeitsspeicher zu injizieren', 'Schadsoftware im Arbeitsspeicher zu injizieren'), ('Dateien außerhalb des vorgesehenen Verzeichnisses auszulesen', 'Dateien außerhalb des vorgesehenen Verzeichnisses auszulesen'), ('Den Benutzer zur Eingabe von Passwörtern zu verleiten', 'Den Benutzer zur Eingabe von Passwörtern zu verleiten')],
                          validators=[DataRequired()])
     #Frage 6
     web6 = RadioField('Welche Zeichenfolge wird typischerweise bei einem Directory Traversal Angriff verwendet?',
                           choices=[('--DROP', '--DROP'), ('<script>', '<script>'), ('../', '../')],
                           validators=[DataRequired()])
     #Frage 7
     web7 = RadioField('Warum sind besonders KMU anfällig für Directory Traversal Angriffe?',
                                   choices=[('Sie betreiben in der Regel keine Webanwendungen', 'Sie betreiben in der Regel keine Webanwendungen'), ('Sie nutzen oft einfache Webtools, die Eingaben nicht ausreichend prüfen', 'Sie nutzen oft einfache Webtools, die Eingaben nicht ausreichend prüfen'), ('Sie verwenden ausschließlich Cloud-Dienste ohne lokale Pfade', 'Sie verwenden ausschließlich Cloud-Dienste ohne lokale Pfade')],
                                   validators=[DataRequired()])
     
     web8 = RadioField('Welche XSS-Art wird dauerhaft auf der Webseite gespeichert?',
                           choices=[('Reflected XSS', 'Reflected XSS'), ('Stored XSS', 'Stored XSS'), ('DOM-based XSS', 'DOM-based XSS')],
                           validators=[DataRequired()])
     #Frage 7
     web9 = RadioField('Warum sind KMU besonders anfällig für XSS-Angriffe?',
                                   choices=[('Sie verwenden ausschließlich lokale Netzwerke ohne Schutzmaßnahmen', 'Sie verwenden ausschließlich lokale Netzwerke ohne Schutzmaßnahmen'), ('Sie setzen oft auf dynamische Webformulare, prüfen Eingaben aber nicht ausreichend', 'Sie setzen oft auf dynamische Webformulare, prüfen Eingaben aber nicht ausreichend'), ('Ihre Webseiten sind vollständig statisch und daher besonders gefährdet', 'Ihre Webseiten sind vollständig statisch und daher besonders gefährdet')],
                                   validators=[DataRequired()])
     #Einreichen
     submit = SubmitField('Fertig')

class quiznetzwerk(FlaskForm): 
     #Frage 1
     net1 = RadioField('Was passiert bei einem Ransomware-Angriff typischerweise?',
                         choices=[('Dateien werden gelöscht und das System wird neugestartet', 'Dateien werden gelöscht und das System wird neugestartet'),
                                  ('Dateien werden verschlüsselt und ein Lösegeld wird gefordert', 'Dateien werden verschlüsselt und ein Lösegeld wird gefordert'),
                                  ('Der Browser wird umgeleitet, um Werbung anzuzeigen', 'Der Browser wird umgeleitet, um Werbung anzuzeigen'),],
                         validators=[DataRequired()])
                         
     #Frage 2
     net2 = RadioField('Was ist mit „Double Extortion“ in Zusammenhang mit Ransomware gemeint?',
                     choices=[('Es werden zwei verschiedene Systeme gleichzeitig verschlüsselt', 'Es werden zwei verschiedene Systeme gleichzeitig verschlüsselt'), 
                              ('Die Angreifer fordern zweimal Geld – zuerst für die Entschlüsselung, dann für technische Hilfe', 'Die Angreifer fordern zweimal Geld – zuerst für die Entschlüsselung, dann für technische Hilfe'), 
                              ('Daten werden verschlüsselt und zusätzlich exfiltriert, um mit Veröffentlichung zu drohen', 'Daten werden verschlüsselt und zusätzlich exfiltriert, um mit Veröffentlichung zu drohen'), ],
                     validators=[DataRequired()])
     
     #Frage 3
     net3 = RadioField('Warum sind KMU besonders gefährdet durch Ransomware-Angriffe?',
                       choices=[('Sie haben in der Regel hochsensible nationale Daten', 'Sie haben in der Regel hochsensible nationale Daten'), 
                                ('Sie verfügen oft nicht über spezialisierte IT-Sicherheitsmaßnahmen', 'Sie verfügen oft nicht über spezialisierte IT-Sicherheitsmaßnahmen'), 
                                ('Sie nutzen ausschließlich veraltete Software', 'Sie nutzen ausschließlich veraltete Software'), ],
                       validators=[DataRequired()])
     #Frage 4
     net4 = RadioField('Welche Schutzmaßnahmen helfen konkret gegen Ransomware?',
                          choices=[('Nutzung von MFA und Zero-Trust-Architekturen', 'Nutzung von MFA und Zero-Trust-Architekturen'), 
                                   ('Datenbankzugriffe direkt im Browser erlauben', 'Datenbankzugriffe direkt im Browser erlauben'), 
                                   ('Keine Backups, um weniger Angriffspunkte zu bieten', 'Keine Backups, um weniger Angriffspunkte zu bieten'),],
                          validators=[DataRequired()])
     #Frage 5
     net5 = RadioField('Was unterscheidet einen Wurm von einem klassischen Computervirus?',
                          choices=[('Ein Wurm benötigt keine Benutzereingabe und verbreitet sich selbstständig', 'Ein Wurm benötigt keine Benutzereingabe und verbreitet sich selbstständig'), 
                                   ('Ein Wurm funktioniert nur auf mobilen Geräten', 'Ein Wurm funktioniert nur auf mobilen Geräten'), 
                                   ('Ein Wurm kann nur per E-Mail übertragen werden', 'Ein Wurm kann nur per E-Mail übertragen werden'),],
                          validators=[DataRequired()])
     #Frage 6
     net6 = RadioField('Welches dieser historischen Beispiele war eine Kombination aus Wurm und Ransomware?',
                           choices=[('Morris Worm', 'Morris Worm'), 
                                    ('Code Red', 'Code Red'), 
                                    ('WannaCry', 'WannaCry'),],
                           validators=[DataRequired()])
     #Frage 7
     net7 = RadioField('Warum sind Unternehmen, insbesondere KMU, besonders gefährdet durch Würmer?',
                                   choices=[('Sie nutzen nur Linux-basierte Systeme', 'Sie nutzen nur Linux-basierte Systeme'), 
                                            ('Sie betreiben oft nicht segmentierte Netzwerke ohne Echtzeitüberwachung', 'Sie betreiben oft nicht segmentierte Netzwerke ohne Echtzeitüberwachung'), 
                                            ('Ihre Netzwerke sind ausschließlich offline', 'Ihre Netzwerke sind ausschließlich offline'),],
                                   validators=[DataRequired()])
     #Frage 8
     net8 = RadioField('Welche Maßnahmen helfen gegen die Ausbreitung von Würmern?',
                                 choices=[('Nutzung offener Ports zur besseren Verfügbarkeit', 'Nutzung offener Ports zur besseren Verfügbarkeit'), 
                                          ('Einsatz von Intrusion Detection Systemen (IDS)', 'Einsatz von Intrusion Detection Systemen (IDS)'), 
                                          ('Verzicht auf Antiviren-Software, um Netzwerkgeschwindigkeit zu erhöhen', 'Verzicht auf Antiviren-Software, um Netzwerkgeschwindigkeit zu erhöhen'),],
                                 validators=[DataRequired()])
     #Frage 9
     net9 = RadioField('Was ist ein typisches Merkmal eines Trojaners?',
                             choices=[('Er verbreitet sich selbstständig über Netzwerke', 'Er verbreitet sich selbstständig über Netzwerke'), 
                                      ('Er tarnt sich als nützliches oder harmloses Programm', 'Er tarnt sich als nützliches oder harmloses Programm'), 
                                      ('Er kann nur über USB-Sticks eingeschleust werden', 'Er kann nur über USB-Sticks eingeschleust werden'),],
                             validators=[DataRequired()])
     #Frage 10
     net10 = RadioField('Welche Schutzmaßnahmen helfen effektiv gegen Trojaner?',
                          choices=[('Nutzung von Administratorrechten für alle Anwendungen', 'Nutzung von Administratorrechten für alle Anwendungen'), 
                                   ('Antiviren-Software mit Signatur- und Verhaltensanalyse', 'Antiviren-Software mit Signatur- und Verhaltensanalyse'), 
                                   ('Ignorieren von Softwareupdates zur Stabilitätssicherung', 'Ignorieren von Softwareupdates zur Stabilitätssicherung'),],
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
     