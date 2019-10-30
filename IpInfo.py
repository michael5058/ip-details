import requests
import sys
import socket




def IpDetails(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return "invaled ip"
    details = requests.get("http://ipinfo.io/"+ip+"/geo").json()
    if 'bogon' in details and details.get('bogon') == True:
       return ("bogon ip")
    organizations = requests.get("http://ipinfo.io/"+ip+"/org").text
    loc = details.get('loc').split(",")
    latitude =loc[0]
    longitude =loc[1]
    markdown_table = "**location**\n\nCountry | region | city \n--- | --- | ---\n" +  \
    details.get('ip')+" | " +details.get('region')+" | " +details.get('city')+"\n**coordinates**\n\n" + \
                     "latitude | longitude \n--- | --- \n" +  \
                     latitude+" | " +longitude + "\n**organizations**\n\n" + organizations


    return markdown_table


if __name__ == '__main__':
    if len(sys.argv)>=2:
        ip = sys.argv[1]
        print(IpDetails(ip))
    else:
        print("no ip passed")
