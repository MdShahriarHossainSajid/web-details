import whois
import socket
#Enter target domain
site = str(input("Enter your site domain: ")) 

#get ip adress of that domain
def get_ip_addresses(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return [ip_address]
    except socket.gaierror as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    website = site  # Replace with the website you want to check
    ip_addresses = get_ip_addresses(website)

    if ip_addresses:
        print(f"IP addresses for {website}:")
        for ip in ip_addresses:
            print(ip)
#show other information on this domain
print(whois.whois(site))
