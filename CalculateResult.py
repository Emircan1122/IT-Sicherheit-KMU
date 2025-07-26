import logging

logger = logging.getLogger(__name__)

class CalculateResult:
    
    def __init__(self, test_type, form_data):
        self.test_type = test_type
        self.form_data = form_data.copy()  # arbeiten mit Kopie, damit es nicht zu schwierighkeiten kommt
        logger.debug(f'CALCULATE RESULTS CLASS Form Data: {form_data}')

        # vorher numerische Felder zu kategorien machen (AusführlicherTest)
        if self.test_type == "Ausführlich":
            self._preprocess_ausfuehrlich_data()
        
        self._build_bewertungskriterien()

    def _preprocess_ausfuehrlich_data(self):
        """Convert numerical answers to categorical ranges for scoring"""
        # Mitarbeiterzahl Kategorizieren
        mitarbeiter = self.form_data.get('mitarbeiter_zahl')
        if isinstance(mitarbeiter, int):
            if mitarbeiter <= 5:
                self.form_data['mitarbeiter_zahl'] = '1-5'
            elif 6 <= mitarbeiter <= 15:
                self.form_data['mitarbeiter_zahl'] = '6-15'
            else:
                self.form_data['mitarbeiter_zahl'] = '16+'

        # Jahresumsatz Kategorizieren
        umsatz = self.form_data.get('jahresumsatz')
        if isinstance(umsatz, int):
            if umsatz <= 50000:
                self.form_data['jahresumsatz'] = '0-50k'
            elif 50001 <= umsatz <= 250000:
                self.form_data['jahresumsatz'] = '50k-250k'
            elif 250001 <= umsatz <= 600000:
                self.form_data['jahresumsatz'] = '250k-600k'
            else:
                self.form_data['jahresumsatz'] = '600k+'

        # Umsatzsteuer Kategorizieren
        ust = self.form_data.get('umsatzsteuer')
        if isinstance(ust, int):
            if ust <= 100:
                self.form_data['umsatzsteuer'] = '0-100'
            elif 101 <= ust <= 500:
                self.form_data['umsatzsteuer'] = '101-500'
            elif 501 <= ust <= 2000:
                self.form_data['umsatzsteuer'] = '501-2000'
            elif 2001 <= ust <= 5000:
                self.form_data['umsatzsteuer'] = '2001-5000'
            else:
                self.form_data['umsatzsteuer'] = '5000+'

    def _build_bewertungskriterien(self):
        """Define scoring rules for different test types"""
        if self.test_type == "web":
            #für den SchnellCheck
            #62
            self.bewertungskriterien = [
                (self.form_data.get('web1'), ["Das Einschleusen von manipuliertem SQL-Code über Benutzereingaben"], 10),
                (self.form_data.get('web2'), ["Cross-Site Scripting (XSS)"], 10),
                (self.form_data.get('web3'), ["Ihre Systeme sind oft veraltet oder schlecht abgesichert"], 10),
                (self.form_data.get('web4'), ["Der Angreifer schleust Skripte ein, die im Browser des Nutzers ausgeführt werden"], 10),
                (self.form_data.get('web5'), ["Dateien außerhalb des vorgesehenen Verzeichnisses auszulesen"], 10),
                (self.form_data.get('web6'), ["../"], 10),
                (self.form_data.get('web7'), ["Sie nutzen oft einfache Webtools, die Eingaben nicht ausreichend prüfen"], 10),
                (self.form_data.get('web8'), ["Stored XSS"], 10),
                (self.form_data.get('web9'), ["Sie setzen oft auf dynamische Webformulare, prüfen Eingaben aber nicht ausreichend"], 10),
            ]
        elif self.test_type == "net":
            #für den SchnellCheck
            #62
            self.bewertungskriterien = [
                (self.form_data.get('net1'), ["Dateien werden verschlüsselt und ein Lösegeld wird gefordert"], 10),
                (self.form_data.get('net2'), ["Daten werden verschlüsselt und zusätzlich exfiltriert, um mit Veröffentlichung zu drohen"], 10),
                (self.form_data.get('net3'), ["Sie verfügen oft nicht über spezialisierte IT-Sicherheitsmaßnahmen"], 10),
                (self.form_data.get('net4'), ["Nutzung von MFA und Zero-Trust-Architekturen"], 10),
                (self.form_data.get('net5'), ["Ein Wurm benötigt keine Benutzereingabe und verbreitet sich selbstständig"], 10),
                (self.form_data.get('net6'), ["WannaCry"], 10),
                (self.form_data.get('net7'), ["Sie betreiben oft nicht segmentierte Netzwerke ohne Echtzeitüberwachung"], 10),
                (self.form_data.get('net8'), ["Einsatz von Intrusion Detection Systemen (IDS)"], 10),
                (self.form_data.get('net9'), ["Er tarnt sich als nützliches oder harmloses Programm"], 10),
                (self.form_data.get('net10'), ["Antiviren-Software mit Signatur- und Verhaltensanalyse"], 10),
            ]
        elif self.test_type == "soc":
            #für den SchnellCheck
            #62
            self.bewertungskriterien = [
                (self.form_data.get('soc1'), ["ja"], 10),
                (self.form_data.get('soc2'), ["ja"], 9),
                (self.form_data.get('soc3'), ["ja"], 7),
                (self.form_data.get('soc4'), ["ja"], 8),
                (self.form_data.get('soc5'), ["ja"], 10),
                (self.form_data.get('soc6'), ["ja"], 6),
                (self.form_data.get('soc7'), ["nein"], 5),
                (self.form_data.get('soc8'), ["ja"], 3),
                (self.form_data.get('soc9'), ["ja"], 4),
                (self.form_data.get('soc10'), ["ja"], 4),
            ]
        elif self.test_type == "mal":
            #für den SchnellCheck
            #62
            self.bewertungskriterien = [
                (self.form_data.get('mal1'), ["ja"], 10),
                (self.form_data.get('mal2'), ["ja"], 9),
                (self.form_data.get('mal3'), ["ja"], 7),
                (self.form_data.get('mal4'), ["ja"], 8),
                (self.form_data.get('mal5'), ["ja"], 10),
                (self.form_data.get('mal6'), ["ja"], 6),
                (self.form_data.get('mal7'), ["nein"], 5),
                (self.form_data.get('mal8'), ["ja"], 3),
                (self.form_data.get('mal9'), ["ja"], 4),
                (self.form_data.get('mal10'), ["ja"], 4),
            ]
        elif self.test_type == "bekoid":
            #für den SchnellCheck
            #62
            self.bewertungskriterien = [
                (self.form_data.get('bekoid1'), ["ja"], 10),
                (self.form_data.get('bekoid2'), ["ja"], 9),
                (self.form_data.get('bekoid3'), ["ja"], 7),
                (self.form_data.get('bekoid4'), ["ja"], 8),
                (self.form_data.get('bekoid5'), ["ja"], 10),
                (self.form_data.get('bekoid6'), ["ja"], 6),
                (self.form_data.get('bekoid7'), ["nein"], 5),
                (self.form_data.get('bekoid8'), ["ja"], 3),
                (self.form_data.get('bekoid9'), ["ja"], 4),
                (self.form_data.get('bekoid10'), ["ja"], 4),
            ]
        elif self.test_type == "schnell":
            self.bewertungskriterien = [
                (self.form_data.get('backup'), ["ja"], 10),
                (self.form_data.get('it_schulung'), ["ja"], 8),
                (self.form_data.get('passwort_mfa'), ["ja"], 10),
                (self.form_data.get('firewall'), ["ja"], 10),
                (self.form_data.get('updates'), ["zeitnah"], 9),
                (self.form_data.get('notfallplan'), ["ja"], 7),
                (self.form_data.get('ddos'), ["ja", "nicht_zutreffend"], 4),
                (self.form_data.get('cyberversicherung'), ["ja"], 3),
                (self.form_data.get('zugriffsrechte'), ["ja"], 6),
                (self.form_data.get('cloud_dienste'), ["ja"], 3),
            ]
        else:
            #für den AusführlichenCheck
            #132
            self.bewertungskriterien = [
                # Step 1: Allgemeine Informationen
                (self.form_data.get('betrieb'), ['restaurant'], 0),
                (self.form_data.get('betrieb'), ['cafe', 'hotel'], 0),
                (self.form_data.get('betrieb'), ['bar', 'catering'], 0),
                (self.form_data.get('betrieb'), ['imbiss'], 0),
                (self.form_data.get('betrieb'), ['sonstiges'], 0),
                
                (self.form_data.get('standort_zahl'), ['1'], 0),
                (self.form_data.get('standort_zahl'), ['2'], 0),
                (self.form_data.get('standort_zahl'), ['3-5'], 0),
                (self.form_data.get('standort_zahl'), ['Mehr als 5'], 0),
                
                (self.form_data.get('mitarbeiter_zahl'), ['1-5'], 0),
                (self.form_data.get('mitarbeiter_zahl'), ['6-10'], 0),
                (self.form_data.get('mitarbeiter_zahl'), ['11-20'], 0),
                (self.form_data.get('mitarbeiter_zahl'), ['21+'], 0),
                
                (self.form_data.get('jahresumsatz'), ['0-100k'], 0),
                (self.form_data.get('jahresumsatz'), ['100k-500k'], 0),
                (self.form_data.get('jahresumsatz'), ['500k+'], 3),
                
                (self.form_data.get('trennung'), ['0-25 %'], 0),
                (self.form_data.get('trennung'), ['26-50 %'], 0),
                (self.form_data.get('trennung'), ['51-75 %'], 0),
                (self.form_data.get('trennung'), ['Über 75%'], 0),

                # Step 2: Kassensystem
                (self.form_data.get('kassensystem'), ['Ja, für alle Standorte'], 10),
                (self.form_data.get('kassensystem'), ['Teilweise'], 5),
                (self.form_data.get('kassensystem'), ['Nein'], 0),
                
                (self.form_data.get('kassensytem_prüfung'), ['Innerhalb der letzen 12 Monate'], 8),
                (self.form_data.get('kassensytem_prüfung'), ['Vor mehr als 12 Monaten'], 5),
                (self.form_data.get('kassensytem_prüfung'), ['Nie'], 0),
                
                (self.form_data.get('tse1'), ['Ja'], 10),
                (self.form_data.get('tse1'), ['Unsicher'], 5),
                (self.form_data.get('tse1'), ['Nein'], 0),
                
                (self.form_data.get('beleg'), ['Ja immer'], 9),
                (self.form_data.get('beleg'), ['Teilweise'], 4),
                (self.form_data.get('beleg'), ['Nein'], 0),
                
                (self.form_data.get('belegs_anforderungen'), ['Ja'], 8),
                (self.form_data.get('belegs_anforderungen'), ['Teilweise'], 4),
                (self.form_data.get('belegs_anforderungen'), ['Nein'], 0),
                
                (self.form_data.get('kassendaten'), ['Täglich'], 7),
                (self.form_data.get('kassendaten'), ['Wöchentlich'], 6),
                (self.form_data.get('kassendaten'), ['Monatlich'], 5),
                (self.form_data.get('kassendaten'), ['Nicht regelmäßig'], 2),

                # Step 3: Buchhaltung
                (self.form_data.get('trennung_essen_trinken'), ['Ja'], 10),
                (self.form_data.get('trennung_essen_trinken'), ['Teilweise'], 4),
                (self.form_data.get('trennung_essen_trinken'), ['Nein'], 0),
                
                (self.form_data.get('buchhaltungssystem'), ['Ja, vollständig integriert'], 9),
                (self.form_data.get('buchhaltungssystem'), ['Teilweise digital'], 7),
                (self.form_data.get('buchhaltungssystem'), ['Nein, rein manuell'], 5),
                
                (self.form_data.get('einnahme_erfassung'), ['Ja, vollständig'], 8),
                (self.form_data.get('einnahme_erfassung'), ['Teilweise'], 6),
                (self.form_data.get('einnahme_erfassung'), ['Nein'], 5),
                
                (self.form_data.get('umsatzsteuer'), ['0-1000'], 0),
                (self.form_data.get('umsatzsteuer'), ['1001-5000'], 0),
                (self.form_data.get('umsatzsteuer'), ['5000+'], 0),
                
                (self.form_data.get('nachforderungen'), ['Nein'], 5),
                (self.form_data.get('nachforderungen'), ['Ja'], 0),

                # Step 4: Steuerdokumentation
                (self.form_data.get('steuererklärungen'), ['Ja, immer'], 7),
                (self.form_data.get('steuererklärungen'), ['Manchmal verspätet'], 3),
                (self.form_data.get('steuererklärungen'), ['Oft verspätet'], 1),
                
                (self.form_data.get('einkommensdokumentation'), ['Ja'], 10),
                (self.form_data.get('einkommensdokumentation'), ['Teilweise'], 5),
                (self.form_data.get('einkommensdokumentation'), ['Nein'], 0),
                
                (self.form_data.get('getrennte_steuersätze'), ['Ja'], 8),
                (self.form_data.get('getrennte_steuersätze'), ['Teilweise'], 4),
                (self.form_data.get('getrennte_steuersätze'), ['Nein'], 0),
                
                (self.form_data.get('steuerprüfung'), ['Nein'], 2),
                (self.form_data.get('steuerprüfung'), ['Ja, einmal'], 1),
                (self.form_data.get('steuerprüfung'), ['Ja, mehrmals'], 0),
                
                (self.form_data.get('nachforderungsdokumentation'), ['Detailliert im Buchhaltungssystem'], 4),
                (self.form_data.get('nachforderungsdokumentation'), ['Manuell in separaten Unterlagen'], 3),
                (self.form_data.get('nachforderungsdokumentation'), ['Keine Dokumentation'], 0),
                
                (self.form_data.get('audits'), ['Ja, monatlich'], 2),
                (self.form_data.get('audits'), ['Ja, jährlich'], 1),
                (self.form_data.get('audits'), ['Nein'], 0),

                # Step 5: Trinkgelder & Schulungen
                (self.form_data.get('trinkgelder_dokumentation'), ['Ja, vollständig'], 4),
                (self.form_data.get('trinkgelder_dokumentation'), ['Teilweise'], 2),
                (self.form_data.get('trinkgelder_dokumentation'), ['Nein'], 0),
                
                (self.form_data.get('trinkgelder_steuer'), ['Ja'], 7),
                (self.form_data.get('trinkgelder_steuer'), ['Unsicher'], 3),
                (self.form_data.get('trinkgelder_steuer'), ['Nein'], 0),
                
                (self.form_data.get('mitarbeiterschulungen'), ['Ja'], 4),
                (self.form_data.get('mitarbeiterschulungen'), ['Nein'], 0)
            ]
    def calcResults(self):
        pos_answers = sum(
            punkte 
            for wert, gültige_werte, punkte in self.bewertungskriterien 
            if wert in gültige_werte
        )
        
        logger.debug(f'Total points calculated: {pos_answers}')
        if self.test_type in ["web", "net", "soc", "mal", "bekoid"]:

            if self.test_type == "web" or "net":
                if pos_answers < 40:   
                    ampelfarbe = "rot"
                elif pos_answers < 80:
                    ampelfarbe = "gelb"
                else:
                    ampelfarbe = "grün"
        elif self.test_type == 'schnell':
            if pos_answers >= 60:
                ampelfarbe = 'A'
            elif pos_answers >= 50:
                ampelfarbe = 'B'
            elif pos_answers >= 40:
                ampelfarbe = 'C'
            elif pos_answers >= 30:
                ampelfarbe = 'D'
            elif pos_answers >= 20:
                ampelfarbe = 'E'
            else:
                ampelfarbe = 'F'
        
        return ampelfarbe, pos_answers
        
        
