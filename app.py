from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario de versículos organizados por categoría
versiculos = {
    "Fe": [
        ("Hebreos 11:1", "Es, pues, la fe la certeza de lo que se espera, la convicción de lo que no se ve."),
        ("Mateo 17:20", "Si tenéis fe como un grano de mostaza, diréis a este monte: Pásate de aquí allá, y se pasará; y nada os será imposible."),
        ("Marcos 9:23", "Jesús le dijo: Si puedes creer, al que cree todo le es posible."),
        ("Santiago 1:6", "Pero pida con fe, no dudando nada, porque el que duda es semejante a la onda del mar, que es arrastrada por el viento y echada de una parte a otra."),
        ("Mateo 21:22", "Y todo lo que pidiereis en oración, creyendo, lo recibiréis."),
        ("2 Corintios 5:7", "Porque por fe andamos, no por vista."),
    ],
    "Amor": [
        ("1 Corintios 13:4-5", "El amor es sufrido, es benigno; el amor no tiene envidia, el amor no es jactancioso, no se envanece; no hace nada indebido, no busca lo suyo, no se irrita, no guarda rencor."),
        ("Juan 3:16", "Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."),
        ("1 Juan 4:8", "El que no ama, no ha conocido a Dios; porque Dios es amor."),
        ("Romanos 13:10", "El amor no hace mal al prójimo; así que el amor es el cumplimiento de la ley."),
        ("1 Juan 4:18", "En el amor no hay temor, sino que el perfecto amor echa fuera el temor; porque el temor lleva en sí castigo, de donde el que teme no ha sido perfeccionado en el amor."),
        ("Cantares 8:7", "Las muchas aguas no podrán apagar el amor, ni los ríos lo ahogarán; si alguien diese todos los bienes de su casa por este amor, de cierto lo despreciarían."),
    ],
    "Esperanza": [
        ("Romanos 15:13", "Y el Dios de esperanza os llene de todo gozo y paz en el creer, para que abundéis en esperanza por el poder del Espíritu Santo."),
        ("Jeremías 29:11", "Porque yo sé los pensamientos que tengo acerca de vosotros, dice Jehová, pensamientos de paz, y no de mal, para daros el fin que esperáis."),
        ("1 Pedro 1:3", "Bendito sea el Dios y Padre de nuestro Señor Jesucristo, que según su grande misericordia nos hizo renacer para una esperanza viva por la resurrección de Jesucristo de los muertos."),
        ("Tito 2:13", "Esperando la bienaventurada esperanza y la manifestación gloriosa de nuestro gran Dios y Salvador Jesucristo."),
        ("Romanos 8:24", "Porque en esperanza fuimos salvos; pero la esperanza que se ve, no es esperanza; porque lo que alguno ve, ¿a qué esperarlo?"),
        ("Hebreos 10:23", "Mantengamos firme sin fluctuar la profesión de nuestra esperanza, porque fiel es el que prometió."),
    ],
    "Paz": [
        ("Filipenses 4:7", "Y la paz de Dios, que sobrepasa todo entendimiento, guardará vuestros corazones y vuestros pensamientos en Cristo Jesús."),
        ("Juan 14:27", "La paz os dejo, mi paz os doy; yo no os la doy como el mundo la da. No se turbe vuestro corazón, ni tenga miedo."),
        ("Isaías 26:3", "Tú guardarás en completa paz a aquel cuyo pensamiento en ti persevera; porque en ti ha confiado."),
        ("Colosenses 3:15", "Y la paz de Dios gobierne en vuestros corazones, a la que asimismo fuisteis llamados en un solo cuerpo; y sed agradecidos."),
        ("Mateo 5:9", "Bienaventurados los pacificadores, porque ellos serán llamados hijos de Dios."),
        ("Romanos 14:19", "Así que, sigamos lo que contribuye a la paz y a la mutua edificación."),
    ],
    "Fuerza": [
        ("Isaías 40:31", "Pero los que esperan a Jehová tendrán nuevas fuerzas; levantarán alas como las águilas; correrán, y no se cansarán; caminarán, y no se fatigarán."),
        ("Filipenses 4:13", "Todo lo puedo en Cristo que me fortalece."),
        ("Efesios 6:10", "Por lo demás, hermanos míos, fortaleceos en el Señor, y en el poder de su fuerza."),
        ("2 Corintios 12:9", "Y me ha dicho: Bástate mi gracia; porque mi poder se perfecciona en la debilidad. Por lo cual, de buena gana me gloriaré más bien en mis debilidades, para que repose sobre mí el poder de Cristo."),
        ("Josué 1:9", "Mira que te mando que te esfuerces y seas valiente; no temas ni desmayes, porque Jehová tu Dios estará contigo en dondequiera que vayas."),
        ("Nehemías 8:10", "No os entristezcáis, porque el gozo de Jehová es vuestra fuerza."),
    ],
    "Gracia": [
        ("Efesios 2:8-9", "Porque por gracia sois salvos, por medio de la fe; y esto no de vosotros, pues es don de Dios; no por obras, para que nadie se gloríe."),
        ("2 Corintios 12:9", "Y me ha dicho: Bástate mi gracia; porque mi poder se perfecciona en la debilidad. Por lo cual, de buena gana me gloriaré más bien en mis debilidades, para que repose sobre mí el poder de Cristo."),
        ("Romanos 5:8", "Pero Dios muestra su amor para con nosotros, en que siendo aún pecadores, Cristo murió por nosotros."),
        ("Tito 2:11", "Porque la gracia de Dios se ha manifestado para salvación a todos los hombres."),
        ("Romanos 6:14", "Porque el pecado no se enseñoreará de vosotros; pues no estáis bajo la ley, sino bajo la gracia."),
        ("2 Timoteo 1:9", "Quien nos salvó y llamó con llamamiento santo, no conforme a nuestras obras, sino conforme a su propósito y gracia, que nos fue dada en Cristo Jesús antes de los tiempos de los siglos."),
    ],
    "Sabiduría": [
        ("Proverbios 2:6", "Porque Jehová da la sabiduría, y de su boca viene el conocimiento y la inteligencia."),
        ("Santiago 1:5", "Y si alguno de vosotros tiene falta de sabiduría, pídala a Dios, el cual da a todos abundantemente y sin reproche, y le será dada."),
        ("Proverbios 4:7", "Sabiduría es la principal cosa; adquiere sabiduría, y con todos tus bienes adquiere inteligencia."),
        ("Colosenses 2:3", "En quien están escondidos todos los tesoros de la sabiduría y del conocimiento."),
        ("Proverbios 3:13", "Bienaventurado el hombre que halla la sabiduría, y que obtiene la inteligencia."),
        ("Eclesiastés 7:12", "Porque la sabiduría es para la vida lo mismo que la herencia es para los que la reciben; y la ventaja de la sabiduría es que da vida a quienes la poseen."),
    ],
    "Confianza": [
        ("Proverbios 3:5-6", "Fíate de Jehová de todo tu corazón, y no te apoyes en tu propia prudencia. Reconócelo en todos tus caminos, y él enderezará tus veredas."),
        ("Salmo 37:5", "Encomienda a Jehová tu camino, y confía en él; y él hará."),
        ("Isaías 26:4", "Confiad en Jehová perpetuamente, porque en Jehová el Señor está la fortaleza de los siglos."),
        ("Salmo 56:3", "El día que temo, yo en ti confío."),
        ("Salmo 118:8", "Mejor es confiar en Jehová que confiar en el hombre."),
    ]
}

@app.route('/')
def index():
    return render_template('index.html', categorias=versiculos.keys())

@app.route('/buscar', methods=['POST'])
def buscar():
    categoria = request.form.get('categoria')
    resultados = versiculos.get(categoria, [])
    return render_template('index.html', categorias=versiculos.keys(), resultados=resultados, categoria=categoria)

if __name__ == '__main__':
    app.run(debug=True)