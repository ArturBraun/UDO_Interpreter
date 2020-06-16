from xml.dom import minidom

globalqwutilspath=""
script_wd = ""

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def get_qw_modeller_path(path):
    qwpaths = minidom.parse(path+"/qw-paths.xml")
    return str(getText(qwpaths.getElementsByTagName('QW-Modeller-PATH')[0].childNodes))

def get_qw_path(path):
    qwpaths = minidom.parse(path+"/qw-paths.xml")
    return str(getText(qwpaths.getElementsByTagName('QW-PATH')[0].childNodes))

def setqwutilspath(path):
    global globalqwutilspath
    globalqwutilspath = path

def getqwutilspath():
    return globalqwutilspath

def setscript_wd(cwd_):
    global script_wd
    script_wd = cwd_

def getscript_wd():
    return script_wd
