
from flask import Flask, flash, redirect, render_template, url_for, request, send_file, session
from flask_bootstrap import Bootstrap5
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import func
import werkzeug

from CalculateResult import CalculateResult
from SchnellCheckForm import *
from AusführlicherCheckForm import *

from PdfGenerator import PdfGenerator

import logging

app = Flask(__name__) 
pdf_generator = PdfGenerator()
app.logger.setLevel(logging.DEBUG)  

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)
 
from db import *

bootstrap = Bootstrap5(app)

MAX_REPORTS_PER_USER = 4


@app.route('/', methods=['GET', 'POST'])  
def index():
    session.pop('form_data', default= None)
    session.pop('step', default= None)

   
    return render_template('index.html')
    
#flask run in terminal um die seite aufzurufen, flask run --reload damit man nicht immer neustarten muss
 
@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/LehrinhalteBase')
def LehrinhalteBase():
    return render_template('LehrinhalteBase.html')

@app.route('/indexCheck')
def indexCheck():
    return render_template('indexCheck.html')

@app.route('/webanwendungen')
def webanwendungen():
    return render_template('webanwendungen.html')

@app.route('/netzwerkinfrastruktur')
def netzwerkinfrastruktur():
    return render_template('netzwerkinfrastruktur.html')

@app.route('/socialengineering')
def socialengineering():
    return render_template('socialengineering.html')

@app.route('/malwarebasiert')
def malwarebasiert():
    return render_template('malwarebasiert.html')

@app.route('/bekoid')
def bekoid():
    return render_template('bekoid.html')


@app.route('/schnelltest', methods=['GET', 'POST'])
def schnelltest():
    test_type = 'schnell'
    session['test_type'] = test_type
    form = SchnellCheckForm()  # ← Neue Formklasse für IT-Sicherheit verwenden
 
    if form.validate_on_submit():
        session['form_data'] = {field.name: field.data for field in form}

        app.logger.debug(f'Form data Schnelltest: {session["form_data"]} Test Type: {test_type} -----------------------------------')

        calculator = CalculateResult(test_type, session['form_data'])
        ampelfarbe, punkte = calculator.calcResults()
        session['ampelfarbe'] = ampelfarbe

        app.logger.debug(f'Ampelfarbe result: {ampelfarbe}, session ampelfarbe: {session["ampelfarbe"]}, Punkte: {punkte} ------------------------------------------')

        user_answers = {
            'Werden Ihre Unternehmensdaten regelmäßig gesichert und offline vorgehalten?': form.backup.data,
            'Finden in Ihrem Unternehmen regelmäßige IT-Sicherheits-Schulungen für Mitarbeitende statt?': form.it_schulung.data,
            'Setzen Sie auf starke Passwörter und nutzen Sie Mehrfaktor-Authentifizierung für wichtige Accounts?': form.passwort_mfa.data,
            'Haben Sie eine Firewall im Einsatz und sind externe Zugänge (z.B. Remote Desktop) abgesichert?': form.firewall.data,
            'Wie zeitnah installieren Sie Software-Updates/Sicherheits-Patches?': form.updates.data,
            'Existiert ein IT-Notfallplan (Incident Response) und wissen Mitarbeiter, was im Ernstfall zu tun ist?': form.notfallplan.data,
            'Hosten Sie öffentliche Web-Dienste, und ist ggf. DDoS-Schutz vorhanden?': form.ddos.data,
            'Besitzen Sie eine Cyber-Versicherung, die Restschäden abdeckt?': form.cyberversicherung.data,
            'Sind Zugriffsrechte in Ihrem Netzwerk nach dem Need-to-know-Prinzip eingeschränkt?': form.zugriffsrechte.data,
            'Nutzen Sie professionelle Cloud-/Hosting-Dienste mit Sicherheitszertifizierungen?': form.cloud_dienste.data
        }

        eingaben = [{'question': frage, 'user_answer': antwort} for frage, antwort in user_answers.items()]
        session['form_eingaben'] = eingaben

        return redirect(url_for('result'))

    return render_template('schnelltest.html', form=form, test_type = session['test_type'])

@app.route('/quizweb', methods=['GET', 'POST'])
def quizweb(): 
    test_type = 'web'
    session['test_type'] = test_type
    form = quizwebanwendungen()
    if form.validate_on_submit():
        session['form_data'] = {field.name: field.data for field in form}  
        app.logger.debug(f'Form data Schnelltest: {session['form_data']} Test Type: {test_type}-----------------------------------')
        calculator = CalculateResult(test_type, session['form_data'])  
        app.logger.debug(f'Calculator inputs, testtype: {test_type}, form data: {session['form_data']}------------------------------------')
        ampelfarbe, punkte = calculator.calcResults() 
        session['ampelfarbe'] = ampelfarbe
        app.logger.debug(f'Ampelfarbe result: {ampelfarbe}, session ampelfarbe: {session['ampelfarbe']},  Punkte: {punkte} ------------------------------------------')
        user_answers = {
            'Was beschreibt eine klassische SQL-Injection (SQLi)?': form.web1.data,
            'Welche der folgenden Angriffsmethoden zählt NICHT zu den typischen SQL-Injection-Arten?': form.web2.data,
            'Warum sind kleine und mittlere Unternehmen (KMU) besonders gefährdet durch SQLi-Angriffe?': form.web3.data,
            'Was passiert bei einem Cross-Site Scripting (XSS)-Angriff?': form.web4.data,
            'Was ist das Ziel eines Directory Traversal Angriffs?': form.web5.data,
            'Welche Zeichenfolge wird typischerweise bei einem Directory Traversal Angriff verwendet?': form.web6.data,
            'Warum sind besonders KMU anfällig für Directory Traversal Angriffe?': form.web7.data,
            'Welche XSS-Art wird dauerhaft auf der Webseite gespeichert?': form.web8.data,
            'Warum sind KMU besonders anfällig für XSS-Angriffe?': form.web9.data,
        }
        eingaben = [] 
        for frage, user_answer in user_answers.items():
            eingaben.append({
                'question': frage, 
                'user_answer': user_answer,       
            }) 
        session['form_eingaben'] = eingaben
        return redirect(url_for('result'))
    return render_template('quizweb.html', form=form)

@app.route('/quiznet', methods=['GET', 'POST'])
def quiznet():
    test_type = 'net'
    session['test_type'] = test_type
    form = quiznetzwerk()
    if form.validate_on_submit():
        session['form_data'] = {field.name: field.data for field in form}  
        app.logger.debug(f'Form data Schnelltest: {session['form_data']} Test Type: {test_type}-----------------------------------')
        calculator = CalculateResult(test_type, session['form_data'])  
        app.logger.debug(f'Calculator inputs, testtype: {test_type}, form data: {session['form_data']}------------------------------------')
        ampelfarbe, punkte = calculator.calcResults() 
        session['ampelfarbe'] = ampelfarbe
        app.logger.debug(f'Ampelfarbe result: {ampelfarbe}, session ampelfarbe: {session['ampelfarbe']},  Punkte: {punkte} ------------------------------------------')
        user_answers = {
            'Was passiert bei einem Ransomware-Angriff typischerweise?': form.net1.data,
            'Was ist mit „Double Extortion“ in Zusammenhang mit Ransomware gemeint?': form.net2.data,
            'Warum sind KMU besonders gefährdet durch Ransomware-Angriffe?': form.net3.data,
            'Welche Schutzmaßnahmen helfen konkret gegen Ransomware?': form.net4.data,
            'Was unterscheidet einen Wurm von einem klassischen Computervirus?': form.net5.data,
            'Welches dieser historischen Beispiele war eine Kombination aus Wurm und Ransomware?': form.net6.data,
            'Warum sind Unternehmen, insbesondere KMU, besonders gefährdet durch Würmer?': form.net7.data,
            'Welche Maßnahmen helfen gegen die Ausbreitung von Würmern?': form.net8.data,
            'Was ist ein typisches Merkmal eines Trojaners?': form.net9.data,
            'Welche Schutzmaßnahmen helfen effektiv gegen Trojaner?': form.net10.data,
        }
        eingaben = [] 
        for frage, user_answer in user_answers.items():
            eingaben.append({
                'question': frage, 
                'user_answer': user_answer,       
            }) 
        session['form_eingaben'] = eingaben
        return redirect(url_for('result'))
    return render_template('quiznet.html', form=form)

@app.route('/quizsoc', methods=['GET', 'POST'])
def quizsoc():
    test_type = 'soc'
    session['test_type'] = test_type
    form = quizsocial()
    if form.validate_on_submit():
        session['form_data'] = {field.name: field.data for field in form}  
        app.logger.debug(f'Form data Schnelltest: {session['form_data']} Test Type: {test_type}-----------------------------------')
        calculator = CalculateResult(test_type, session['form_data'])  
        app.logger.debug(f'Calculator inputs, testtype: {test_type}, form data: {session['form_data']}------------------------------------')
        ampelfarbe, punkte = calculator.calcResults() 
        session['ampelfarbe'] = ampelfarbe
        app.logger.debug(f'Ampelfarbe result: {ampelfarbe}, session ampelfarbe: {session['ampelfarbe']},  Punkte: {punkte} ------------------------------------------')
        user_answers = {
            'Wie ist Ihr Gastronomiebetrieb strukturiert?': form.soc1.data,
            'Erfüllt Ihr Kassensystem die Anforderungen einer zertifizierten technischen Sicherheitseinrichtung (TSE)?': form.soc2.data,
            'Geben Sie für jede Transaktion einen Beleg aus?': form.soc3.data,
            'Wurde Ihr Kassensystem innerhalb der letzten 12 Monate geprüft oder zertifiziert?': form.soc4.data,
            'Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?': form.soc5.data,
            'Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?': form.soc6.data,
            'Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?': form.soc7.data,
            'Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?': form.soc8.data,
            'Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?': form.soc9.data,
            'Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?': form.soc10.data,
        }
        eingaben = [] 
        for frage, user_answer in user_answers.items():
            eingaben.append({
                'question': frage, 
                'user_answer': user_answer,       
            }) 
        session['form_eingaben'] = eingaben
        return redirect(url_for('result'))
    return render_template('quizsoc.html', form=form)

@app.route('/quizmal', methods=['GET', 'POST'])
def quizmal():
    test_type = 'mal'
    session['test_type'] = test_type
    form = quizmaleware()
    if form.validate_on_submit():
        session['form_data'] = {field.name: field.data for field in form}  
        app.logger.debug(f'Form data Schnelltest: {session['form_data']} Test Type: {test_type}-----------------------------------')
        calculator = CalculateResult(test_type, session['form_data'])  
        app.logger.debug(f'Calculator inputs, testtype: {test_type}, form data: {session['form_data']}------------------------------------')
        ampelfarbe, punkte = calculator.calcResults() 
        session['ampelfarbe'] = ampelfarbe
        app.logger.debug(f'Ampelfarbe result: {ampelfarbe}, session ampelfarbe: {session['ampelfarbe']},  Punkte: {punkte} ------------------------------------------')
        user_answers = {
            'Wie ist Ihr Gastronomiebetrieb strukturiert?': form.mal1.data,
            'Erfüllt Ihr Kassensystem die Anforderungen einer zertifizierten technischen Sicherheitseinrichtung (TSE)?': form.mal2.data,
            'Geben Sie für jede Transaktion einen Beleg aus?': form.mal3.data,
            'Wurde Ihr Kassensystem innerhalb der letzten 12 Monate geprüft oder zertifiziert?': form.mal4.data,
            'Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?': form.mal5.data,
            'Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?': form.mal6.data,
            'Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?': form.mal7.data,
            'Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?': form.mal8.data,
            'Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?': form.mal9.data,
            'Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?': form.mal10.data,
        }
        eingaben = [] 
        for frage, user_answer in user_answers.items():
            eingaben.append({
                'question': frage, 
                'user_answer': user_answer,       
            }) 
        session['form_eingaben'] = eingaben
        return redirect(url_for('result'))
    return render_template('quizmal.html', form=form)

@app.route('/quizbekoid', methods=['GET', 'POST'])
def quizbekoid():
    test_type = 'bekoid'
    session['test_type'] = test_type
    form = quizBekoid()
    if form.validate_on_submit():
        session['form_data'] = {field.name: field.data for field in form}  
        app.logger.debug(f'Form data Schnelltest: {session['form_data']} Test Type: {test_type}-----------------------------------')
        calculator = CalculateResult(test_type, session['form_data'])  
        app.logger.debug(f'Calculator inputs, testtype: {test_type}, form data: {session['form_data']}------------------------------------')
        ampelfarbe, punkte = calculator.calcResults() 
        session['ampelfarbe'] = ampelfarbe
        app.logger.debug(f'Ampelfarbe result: {ampelfarbe}, session ampelfarbe: {session['ampelfarbe']},  Punkte: {punkte} ------------------------------------------')
        user_answers = {
            'Wie ist Ihr Gastronomiebetrieb strukturiert?': form.bekoid1.data,
            'Erfüllt Ihr Kassensystem die Anforderungen einer zertifizierten technischen Sicherheitseinrichtung (TSE)?': form.bekoid2.data,
            'Geben Sie für jede Transaktion einen Beleg aus?': form.bekoid3.data,
            'Wurde Ihr Kassensystem innerhalb der letzten 12 Monate geprüft oder zertifiziert?': form.bekoid4.data,
            'Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?': form.bekoid5.data,
            'Erfassen Sie alle Einnahmen aus Barzahlungen, Kartenzahlungen und Lieferdiensten vollständig?': form.bekoid6.data,
            'Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?': form.bekoid7.data,
            'Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?': form.bekoid8.data,
            'Dokumentieren Sie Trinkgelder gemäß den steuerlichen Vorgaben?': form.bekoid9.data,
            'Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult (z.B. Kassensicherungsverordnung, Trinkgeldregelung)?': form.bekoid10.data,
        }
        eingaben = [] 
        for frage, user_answer in user_answers.items():
            eingaben.append({
                'question': frage, 
                'user_answer': user_answer,       
            }) 
        session['form_eingaben'] = eingaben
        return redirect(url_for('result'))
    return render_template('quizbekoid.html', form=form)

@app.route('/ausführlicherTest', methods=['GET', 'POST'])
def ausführlicherTest():
    session.setdefault('form_data_ausführlich', {})
    session.setdefault('step', 1)
    
    current_step = session['step']
    form_data = session['form_data_ausführlich']

    form_classes = {
        1: AusführlicherCheckForm1,
        2: AusführlicherCheckForm2,
        3: AusführlicherCheckForm3,
        4: AusführlicherCheckForm4,
        5: AusführlicherCheckForm5
    }

    if current_step not in form_classes:
        session['step'] = 1
        return redirect(url_for('ausführlicherTest'))

    form = form_classes[current_step](formdata=request.form if request.method == 'POST' else None)

    if request.method == 'POST':
        direction = request.form.get('direction')

        if direction == 'next':
            if form.validate():
                form_data.update(form.data)
                form_data.pop('csrf_token', None)
                form_data.pop('submit', None)
                session['form_data_ausführlich'] = form_data
                session['step'] = min(current_step + 1, 5)
                return redirect(url_for('ausführlicherTest'))
        elif direction == 'back':
            session['step'] = max(current_step - 1, 1)
            return redirect(url_for('ausführlicherTest'))
        elif direction == 'submit':
            if form.validate():
                form_data.update(form.data)
                form_data.pop('csrf_token', None)
                form_data.pop('submit', None)
                
                calculator = CalculateResult('Ausführlich', form_data)
                ampelfarbe, _ = calculator.calcResults()
                session['ampelfarbe'] = ampelfarbe
                
                filename = pdf_generator.generate_pdf(form_data)
                
                # wenn eingeloggt, wird das halt auf die db gesaved
                if current_user.is_authenticated:
                    with open(filename, 'rb') as f:
                        report = Report(parent_id=current_user.id, 
                                      file=f.read(),
                                      test_type='Ausführlich')
                        db.session.add(report)
                        db.session.commit()
                
                user_answers = {
                    'betrieb': 'Wie ist Ihr Gastronomiebetrieb strukturiert?',
                    'standort_zahl': 'Wie viele Standorte betreiben Sie?',
                    'mitarbeiter_zahl': 'Anzahl der Mitarbeitenden in Ihrem Betrieb (inkl. Teilzeit und Aushilfen)?',
                    'jahresumsatz': 'Wie hoch war Ihr Jahresumsatz im letzten Geschäftsjahr?',
                    'trennung': 'Wie hoch war Ihr Anteil an Barumsätzen im letzten Geschäftsjahr?',
                    'kassensystem': 'Nutzen Sie für den Verkauf Kassensysteme mit digitaler Aufzeichnungspicht (nach Kassensicherungsverordnung)?',
                    'kassensytem_prüfung': 'Wann wurde Ihr Kassensystem zuletzt geprüft oder zertiziert?',
                    'tse1': 'Erfüllt Ihr Kassensystem die Anforderungen einer zertizierten technischen Sicherheitseinrichtung (TSE)?',
                    'beleg': 'Geben Sie für jede Transaktion einen Beleg aus?',
                    'belegs_anforderungen': 'Entsprechen die Belege Ihres Kassensystems allen gesetzlichen Anforderungen (Konkret)?',
                    'kassendaten': 'Wie oft sichern Sie Ihre Kassendaten?',
                    'trennung_essen_trinken': 'Trennen Sie Speisen (7% MwSt.) und Getränke (19% MwSt.) korrekt in Ihrer Buchhaltung?',
                    'buchhaltungssystem': 'Nutzen Sie ein digitales Buchhaltungssystem?',
                    'einnahme_erfassung': 'Erfassen Sie Einnahmen aus verschiedenen Quellen (z.B. Barzahlung, Kartenzahlung, Lieferdienste) getrennt?',
                    'umsatzsteuer': 'Wie hoch war Ihre durchschnittliche monatliche Umsatzsteuerzahlung in den letzten 12 Monaten? (€)',
                    'nachforderungen': 'Haben Sie in den letzten 2 Jahren Umsatzsteuer-Nachforderungen erhalten?',
                    'steuererklärungen': 'Reichen Sie Ihre Steuererklärungen immer fristgerecht ein?',
                    'einkommensdokumentation': 'Werden die Einnahmen aus allen Quellen (z. B. Barumsatz, Kartenzahlungen, Lieferdienste) vollständig dokumentiert?',
                    'getrennte_steuersätze': 'Nutzen Sie getrennte Umsatzsteuer-Sätze für Lieferungen oder Take-Away-Geschäft?',
                    'steuerprüfung': 'Wurde Ihr Betrieb in den letzten 5 Jahren steuerlich geprüft?',
                    'nachforderungsdokumentation': 'Wie dokumentieren Sie Nachforderungen durch das Finanzsystem?',
                    'audits': 'Führen Sie regelmäßige interne Audits zu steuerlichen Anforderungen durch?',
                    'trinkgelder_dokumentation': 'Werden Trinkgelder korrekt dokumentiert?',
                    'trinkgelder_steuer': 'Sind Trinkgelder, die über das Kassensystem erfasst werden, korrekt lohnversteuert?',
                    'mitarbeiterschulungen': 'Werden Ihre Mitarbeitenden regelmäßig zu steuerlichen Vorgaben geschult?',
                }
                # damit die fragen in der richtigen Reihenfolge erscheinen statt einfach random
                question_order = [
                    'betrieb', 'standort_zahl', 'mitarbeiter_zahl', 'jahresumsatz', 'trennung',
                    'kassensystem', 'kassensytem_prüfung', 'tse1', 'beleg', 'belegs_anforderungen', 'kassendaten',
                    'trennung_essen_trinken', 'buchhaltungssystem', 'einnahme_erfassung', 'umsatzsteuer', 'nachforderungen',
                    'steuererklärungen', 'einkommensdokumentation', 'getrennte_steuersätze', 'steuerprüfung', 'nachforderungsdokumentation', 'audits',
                    'trinkgelder_dokumentation', 'trinkgelder_steuer', 'mitarbeiterschulungen'
                ] 

                eingaben = [] 
                for field in question_order:
                    if field in form_data:
                        eingaben.append({
                            'question': user_answers.get(field, field),
                            'user_answer': form_data[field]
                        })
                
                session['form_eingaben'] = eingaben
                session.pop('form_data_ausführlich', None) 
                session.pop('step', None)
                
                return redirect(url_for('result', filename=filename))

    for field in form:
        if field.name in form_data:
            field.data = form_data[field.name]

        return render_template('ausführlicherTest.html', form=form, current_step=current_step, total_steps=5)
    else: 
        return render_template('ausführlicherTest.html', form=form, current_step=current_step, total_steps=5)


@app.route("/result")
def result():  
    filename = request.args.get('filename')
    form_eingaben = session.get('form_eingaben')
 
    if not form_eingaben: 
        return "Fehler: daten nicht gefunden."
    

    else:
        return render_template("result.html", filename=filename, form_eingaben = form_eingaben, ampelfarbe = session['ampelfarbe'])

@app.route("/download/<filename>")     
def download_pdf(filename):
    return send_file(filename, as_attachment=True)

from flask import send_file, abort
import io 
   
if __name__ == "__main__":
    app.run(debug=True)    

