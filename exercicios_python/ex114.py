import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('O site está indisponível no momento.')

else:
    print('O site está disponível.')
    # print(site.read()) -- lê o conteúdo