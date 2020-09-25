


# Regex para extraer del comentario el segundo alumno que participa en el lab
def user2(comment):
    try:
        return ((re.findall('@\w*-?\w+',comment[0]['body']))[0]).replace('@','')
    except: return None

# Regex para extraer del comentario el tercer alumno que participa en el lab    
def user3(comment):
    try:
        return ((re.findall('@\w*-?\w+',comment[0]['body']))[1]).replace('@','')
    except: return None

    
# Regex para extraer del comentario la url del meme
def url(comment):
    try:
        try:
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            z = z[1].split("'")
            return z[0]
        except: 
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            return z[0]
    except:
        return None   

# Regex para extraer el instructor
def instructor(comment):
    try:
        return comment[0]['user']['login']
    except: return None

# Regex para extraer la nota
def grade(comment):
    try:
        x = ((str(re.findall(r'grade:.*-',comment[0]['body'])).split(':'))[1]).split('-')
        return x[0]
    except: return None
    
# Regex para extraer el nombre del lab
def lab(data):
    try:
        return re.findall(r'\[(.*?)\]',data)[0]
    except: return None

